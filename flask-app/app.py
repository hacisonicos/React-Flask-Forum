from datetime import datetime
import atexit
from pygooglenews import GoogleNews
from flask import Flask
from flask_restful import Api, Resource, fields, marshal_with  # reqparse, abort,
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler
from newspaper import Article
from time import mktime


app = Flask(__name__, static_folder='../build', static_url_path='/')
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
gn = GoogleNews(lang='tr', country='TR')


class NewsModel(db.Model):
    '''
        DataBase class for news data.
    '''
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.UnicodeText())
    description = db.Column(db.UnicodeText())
    text = db.Column(db.UnicodeText())
    image_url = db.Column(db.Text())
    date = db.Column(db.DateTime())
    url = db.Column(db.Text(), unique=True)
    section = db.Column(db.Text())

    def __repr__(self):
        return f"__repr__ test: {self.url}"


# db.create_all()  # To create sqllite database. Creates from tables to engine.


def articles_todatabase(articles, sections, dates):
    """Takes links of articles as input. Sections and dates comes from pygooglenews so added independent of newspaperv3
    Uses NewsPlease to retrieve articles and adds to database.True if successful else False
    """

    entries = []

    for i, article in enumerate(articles):
        try:
            article = Article(article)

            article.download()
            article.parse()

            entries.append(dict(
                title=article.title,
                description=article.meta_description,
                text=article.text,
                image_url=article.meta_img,
                date=dates[i],
                url=article.canonical_link,
                section=sections[i],
            ))

        except KeyboardInterrupt:
            print("CTRL+C!")
            return False
        except:
            continue

    insert_command = NewsModel.__table__.insert(
    ).prefix_with('OR IGNORE').values(entries)

    db.session.execute(insert_command)
    db.session.commit()

    return True


def news_data():
    print(f"Database update has started! Time: {datetime.now().time()}")

    links = []
    sections = []
    dates = []
    topics = ['WORLD', 'NATION', 'BUSINESS', 'TECHNOLOGY',
              'ENTERTAINMENT', 'SCIENCE', 'SPORTS', 'HEALTH', 'HOME']

    for topic in topics:
        if topic == "HOME":
            data = gn.top_news()
        else:
            data = gn.topic_headlines(topic, proxies=None, scraping_bee=None)

        for entry in data["entries"]:
            links.append(entry.link)
            sections.append(topic)
            dates.append(datetime.fromtimestamp(
                mktime(entry["published_parsed"])))

    print("Got news links")

    if articles_todatabase(links, sections, dates):
        print("Success!")
    else:
        print("Fail!")


resource_fields = {
    'title': fields.String,
    'description': fields.String,
    'text': fields.String,
    'image_url': fields.String,
    'date': fields.DateTime,
    'url': fields.String,
    'section': fields.String,
}


class News(Resource):
    '''
        Api for news data. Added to resources after. Input is a flask_restful class.
    '''

    @ marshal_with(resource_fields)
    def get(self, topic):
        # Order by time and get latest 10 news.
        result = NewsModel.query.filter_by(
            section=topic.upper()).order_by(NewsModel.date.desc()).limit(10).all()

        return result

    def post(self):
        pass


api.add_resource(News, "/news/<string:topic>")

# Scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(func=news_data, trigger="interval", minutes=10)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())
