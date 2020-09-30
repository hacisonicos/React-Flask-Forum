from datetime import datetime
import atexit
from newsplease import NewsPlease
from pygooglenews import GoogleNews
from flask import Flask
from flask_restful import Api, Resource, fields, marshal_with  # reqparse, abort,
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler


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
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.UnicodeText())
    description = db.Column(db.UnicodeText())
    text = db.Column(db.UnicodeText())
    image_url = db.Column(db.Text())
    date = db.Column(db.DateTime())
    url = db.Column(db.Text())

    def __repr__(self):
        return f"__repr__ test: {self.url}"


def articles_todatabase(articles):
    """Takes links of articles as input.
    Uses NewsPlease to retrieve articles and adds to database.True if successful else False"""

    news_dict = NewsPlease.from_urls(articles)

    for key in news_dict:
        data_point = NewsModel(
            title=news_dict[key].title,
            description=news_dict[key].description,
            text=news_dict[key].maintext,
            image_url=news_dict[key].image_url,
            date=news_dict[key].date_publish,
            url=news_dict[key].url,
        )

        db.session.add(data_point)

    db.session.commit()

    return True


def news_data():
    print(
        f"Database update has started! Time: {datetime.now().time()}")
    top = gn.top_news()
    links = []

    for entry in top["entries"]:
        links.append(entry.link)

    if articles_todatabase(links):
        print("Success")


# db.create_all()  # To create sqllite database. Creates from tables to engine.


resource_fields = {
    'title': fields.String,
    'description': fields.String,
    'text': fields.String,
    'image_url': fields.String,
    'date': fields.DateTime,
    'url': fields.String,
}


class News(Resource):
    '''
        Api for news data. Added to resources after. Input is a flask_restful class.
    '''

    @marshal_with(resource_fields)
    def get(self):
        result = NewsModel.query.order_by(
            NewsModel.date.desc()).limit(10).all()  # Order by time and get latest 10 news.
        return result

    def post(self):
        pass


api.add_resource(News, "/news")

# Scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(func=news_data, trigger="interval", minutes=3)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())
