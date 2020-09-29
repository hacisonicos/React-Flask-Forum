from app import db, News
from newsplease import NewsPlease
from pygooglenews import GoogleNews
import pandas as pd
gn = GoogleNews(lang='tr', country='TR')


def get_articles_v2(articles):
    assert type(articles) == list, "Articles' urls must be in list."

    news_dict = NewsPlease.from_urls(articles)

    output_dict = {
        "title": [],
        "description": [],
        "text": [],
        "image_url": [],
        "date": [],
        "url": [],
    }

    for key in news_dict:
        try:
            output_dict["title"].append(news_dict[key].title)
            output_dict["description"].append(
                news_dict[key].description)
            output_dict["text"].append(news_dict[key].maintext)
            output_dict["image_url"].append(news_dict[key].image_url)
            output_dict["date"].append(news_dict[key].date_publish)
            output_dict["url"].append(news_dict[key].url)

        except KeyboardInterrupt:
            print("CTRL+C!")
            break
        except:
            continue

   # df = pd.DataFrame(data=output_dict)
   # df = df.sort_values(by="date", ascending=False).reset_index(drop=True)

    # for i in range(len(df)):
    #    df.loc[i,]

    #df.to_sql('users', if_exists="append", con=db.engine, index=False)

    return df


top = gn.top_news()

links = []

for entry in top["entries"]:
    links.append(entry.link)

df = get_articles_v2(links)
