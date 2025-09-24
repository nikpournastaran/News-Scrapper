# scraper/core.py

import requests
from bs4 import BeautifulSoup

# scrape news
def scrape_news_site(url):
    news_list = []
    try:
        response = requests.get(url)
        response.raise_for_status() 
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: Find all news sections
        # Note: This part should be changed based on the HTML structure of your target site.
        # Use browser developer tools (F12) to find the correct tags and classes.
        news_items = soup.find_all('article', class_='news-item')

        for item in news_items:
            try:
                title = item.find('h2').text.strip()
                short_text = item.find('p', class_='summary').text.strip()
                image_link = item.find('img')['src']
                news_link = item.find('a')['href']
                
                # create a dictionary from news without extra fields
                news_data = {
                    'title': title,
                    'short_text': short_text,
                    'image_link': image_link,
                    'news_link': news_link
                }
                news_list.append(news_data)
            except (AttributeError, TypeError) as e:
                print(f"Skipping a news item due to a missing element: {e}")
                continue

    except requests.exceptions.RequestException as e:
        print(f"Error during web request: {e}")
        return []

    return news_list