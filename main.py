from services.sec_api import sec_news
from services.serper_api import serper_news
from services.scraper import scrape_serper, normalize_scrape_results
from services.summarizer import generate_summary
from utils.date_filter import filter_last_7_days
from services.email_sender import send_email

def main():
    sec_articles =  sec_news()

    serper_results = normalize_scrape_results()
    

    recent_articles = filter_last_7_days(sec_articles)

    combined = recent_articles + serper_results

    combined_text = "\n\n".join(article["description"] for article in combined)

    summary = generate_summary(combined_text)

    send_email(summary)


if __name__ == "__main__":
    main()