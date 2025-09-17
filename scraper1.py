import requests 
from bs4 import BeautifulSoup
import sqlite3
from database1 import connect_db


#Scrapes news from apnews.com and stores them in the database
def scrape_ap_news():
    
    url = "https://apnews.com/"
    try:
        response = requests.get(url)
        response.raise_for_status() 
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        
        articles = soup.find_all('div', class_='Card')
        
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            
            for article in articles:
                try:
                    title_tag = article.find('h2', class_='CardHeadline')
                    if title_tag:
                        title = title_tag.get_text().strip()
                        news_url_tag = article.find('a', class_='Link')
                        if news_url_tag:
                            news_url = "https://apnews.com" + news_url_tag.get('href')
                            
                            image_tag = article.find('img', class_='ResponsiveImage')
                            image_url = image_tag.get('src') if image_tag else None

                            short_text_tag = article.find('p', class_='Body')
                            short_text = short_text_tag.get_text().strip() if short_text_tag else None
                            
                            # Check for duplicates before inserting
                            cursor.execute("SELECT news_url FROM news WHERE news_url = ?", (news_url,))
                            if cursor.fetchone() is None:
                                cursor.execute("""
                                    INSERT INTO news (title, short_text, image_url, news_url)
                                    VALUES (?, ?, ?, ?)
                                """, (title, short_text, image_url, news_url))
                                conn.commit()
                                print(f"Added new article: {title}")
                            else:
                                print(f"Article already exists: {title}")
                            
                except Exception as e:
                    print(f"Error processing article: {e}")
                    continue

            conn.close()
    
    except requests.exceptions.RequestException as e:
        print(f"Error making request to {url}: {e}")

if __name__ == "_main_":
    scrape_ap_news()