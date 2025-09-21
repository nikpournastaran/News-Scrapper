import requests
from bs4 import BeautifulSoup
import datetime

#scrape news
def scrape_news_site(url):
   
    news_list = []
    try:
        response = requests.get(url)
        response.raise_for_status() 
        soup = BeautifulSoup(response.text, 'html.parser')

        # مثال: پیدا کردن تمام بخش‌های خبری
        # توجه: این قسمت باید بر اساس ساختار HTML سایت مورد نظر شما تغییر کند.
        # از ابزارهای توسعه‌دهنده مرورگر (F12) برای پیدا کردن تگ‌ها و کلاس‌ها استفاده کنید.
        news_items = soup.find_all('article', class_='news-item')

        for item in news_items:
            try:
                title = item.find('h2').text.strip()
                short_text = item.find('p', class_='summary').text.strip()
                image_link = item.find('img')['src']
                news_link = item.find('a')['href']
                
                # create dics from news
                news_data = {
                    'title': title,
                    'short_text': short_text,
                    'image_link': image_link,
                    'news_link': news_link,
                    'scraped_at': datetime.datetime.now().isoformat(),
                    'is_active': 1
                }
                news_list.append(news_data)
            except (AttributeError, TypeError) as e:
                print(f"Skipping a news item due to missing element: {e}")
                continue

    except requests.exceptions.RequestException as e:
        print(f"Error during web request: {e}")
        return []

    return news_list