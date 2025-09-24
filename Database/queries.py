# database/queries.py

import sqlite3
from datetime import datetime
from .connection import get_db_connection

def insert_news(news_data):
    conn = get_db_connection()
    if not conn:
        return False
    try:
        cursor = conn.cursor()
        
        # تولید تاریخ و زمان فعلی و مقدار پیش‌فرض برای is_active
        scraped_at = datetime.now().isoformat()
        is_active = 1
        
        cursor.execute('''
            INSERT INTO news (title, short_text, image_link, news_link, scraped_at, is_active)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (news_data['title'], news_data['short_text'], news_data['image_link'],
              news_data['news_link'], scraped_at, is_active))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print(f"News with link {news_data['news_link']} already exists.")
        return False
    except sqlite3.Error as e:
        print(f"Error inserting news: {e}")
        return False
    finally:
        if conn:
            conn.close()