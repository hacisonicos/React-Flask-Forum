from app import news_data
import requests

BASE = "http://127.0.0.1:5000/"

#response = requests.get(BASE + "news")
# print(response.json()[-1]["text"])


news_data()
