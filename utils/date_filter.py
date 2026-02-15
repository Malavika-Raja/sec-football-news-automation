from datetime import datetime, timedelta

def filter_last_7_days(articles):
  one_week_ago = datetime.utcnow() - timedelta(days=7)
  filtered=[]
  for article in articles:
    published_date = datetime.fromisoformat(article['date'].replace("Z",""))
    if published_date>=one_week_ago:
      filtered.append(article)
  return filtered