import requests
from datetime import datetime, timedelta

def sec_news():

    url = "https://www.secsports.com/api/articles/?filter%5Bcategories%5D=2&filter%5Bsports.id%5D=6&filter%5Btype%5D=default%2Cvideo&sort=sort%2C-published_at&include=postScheduleEvents.firstOpponent%2CpostScheduleEvents.secondOpponent&per_page=20&page=1"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    articles_list=[]

    for article in data['data']:
      article_title = article["title"]
      article_description = article["short_description"]
      article_pub_date = article["published_at"]

      articles ={
          'title':article_title,
          'description':article_description,
          'date': article_pub_date
      }

      articles_list.append(articles)

    return articles_list