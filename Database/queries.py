from .connection import get_db_connection
import sqlite3

#create new news in database dictionary
def insert_news(news_data):
    
    conn = get_db_connection()
    if not conn:
        return False
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO news (title, short_text, image_link, news_link, scraped_at, is_active)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (news_data['title'], news_data['short_text'], news_data['image_link'],
              news_data['news_link'], news_data['scraped_at'], news_data['is_active']))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        #this news is excist already
        return False
    except sqlite3.Error as e:
        print(f"Error inserting news: {e}")
        return False
    finally:
        if conn:
            conn.close()
#last news
def get_latest_news(limit=20):
   
    conn = get_db_connection()
    if not conn:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM news ORDER BY scraped_at DESC LIMIT ?', (limit,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error fetching latest news: {e}")
        return []
    finally:
        if conn:
            conn.close()
#search in news with title and short text
def search_news(query):
   
    conn = get_db_connection()
    if not conn:
        return []
    try:
        cursor = conn.cursor()
        search_term = f'%{query}%'
        cursor.execute('''
            SELECT * FROM news WHERE title LIKE ? OR short_text LIKE ?
        ''', (search_term, search_term))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error searching news: {e}")
        return []
    finally:
        if conn:
            conn.close()

#update news
def update_news(news_id, new_data):
    
    conn = get_db_connection()
    if not conn:
        return False
    try:
        cursor = conn.cursor()
        
        
        update_parts = []
        values = []
        for key, value in new_data.items():
            update_parts.append(f"{key} = ?")
            values.append(value)
        
        if not update_parts:
            return True  

        values.append(news_id)
        
        query = f"UPDATE news SET {', '.join(update_parts)} WHERE id = ?"
        cursor.execute(query, tuple(values))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error updating news: {e}")
        return False
    finally:
        if conn:
         conn.close()