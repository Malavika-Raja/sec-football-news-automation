import os
import requests
from config import SERPER_API_KEY


def serper_news(query="SEC college football news",num_results=10):
  url ="https://google.serper.dev/news"
  headers = {"X-API-KEY":SERPER_API_KEY,"Content-Type":"application/json"}
  payload = {"q":query, "tbs":"qdr:w"}

  response = requests.request("POST",url, headers=headers, json=payload)

  data = response.json()

  articles_list=[]

  for article in data["news"]:
    article_title = article["title"]
    article_description = article["snippet"]
    article_pub_date = article["date"]
    article_link = article["link"]

    articles ={
      'title':article_title,
      'description':article_description,
      'date': article_pub_date,
      'link':article_link
    }

    articles_list.append(articles)

  return articles_list

