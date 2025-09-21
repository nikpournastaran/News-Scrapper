import sqlite3
from ..config import DATABASE_NAME


#connection to database
def get_db_connection():
    
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        #with colomn names
        conn.row_factory = sqlite3.Row  
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

#create table if doesnt exist
def initialize_database():
    
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS news (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                short_text TEXT,
                image_link TEXT,
                news_link TEXT UNIQUE NOT NULL,
                scraped_at TEXT,
                is_active INTEGER DEFAULT 1
            )
        ''')
        conn.commit()
        conn.close()
        print("Database initialized successfully.")