from ..scraper.core import scrape_news_site
from ..database.queries import insert_news, get_latest_news, search_news, update_news
from ..config import NEWS_SITE_URL

#scrape news and save in database
def run_scraper_job():
   
    print("Running scraper job...")
    news_items = scrape_news_site(NEWS_SITE_URL)
    if not news_items:
        print("No new news items scraped.")
        return

    inserted_count = 0
    for news_data in news_items:
        if insert_news(news_data):
            inserted_count += 1
            
    print(f"Scraped {len(news_items)} items. Inserted {inserted_count} new items.")

#20 latest news
def get_20_latest_news():
    
    return get_latest_news(limit=20)
#search in news by title and text
def search_news_by_query(query):
    
    return search_news(query)
#update news
def edit_news_item(news_id, new_data):
    
    return update_news(news_id, new_data)