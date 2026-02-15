import os
import requests 
from services.serper_api import serper_news
from config import SERPER_API_KEY

def scrape_serper(link):
  """
  Scrapes a URL using Serper's scrape endpoint
  """
  url = "https://scrape.serper.dev"

  headers = {
      "X-API-KEY":SERPER_API_KEY,
      "Content-Type":"application/json"
  }

  payload = {
      "url":link
  }

  response = requests.request("POST", url, headers=headers, json=payload)

  return response.json()

def normalize_scrape_results(limit:  int=5):
  """
  Fetches SEC news via Serper search, scrapes and then normalizes them
  """
  serper_response = serper_news()

  articles=[]
  for i in range(len(serper_response)):

    data = scrape_serper(serper_response[i]["link"])
    if data:
        articles.append({
            "title":serper_response[i]["title"],
            "description":data.get("text","")[:3000]
        })
    if i == 2:
        break

    return articles

