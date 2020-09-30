import datetime
from newsplease import NewsPlease
from pygooglenews import GoogleNews
from app import db, NewsModel


gn = GoogleNews(lang='tr', country='TR')


def articles_todatabase(articles):
    """Takes links of articles as input.
    Uses NewsPlease to retrieve articles and adds to database.True if successful else False"""

    assert(articles) == 'list'

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
        f"Database update has started! Time: {datetime.datetime.now().time()}")
    top = gn.top_news()
    links = []

    for entry in top["entries"]:
        links.append(entry.link)

    articles_todatabase(links)
