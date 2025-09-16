import sqlite3
DATABASE_NAME = "news_database.db"

#connect SQLite to Database
def connect_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

#Create table for news
def create_table():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS news(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                short_text text,
                image_url text,
                news_url TEXT NOT NULL UNIQUE,
                is_active INTEGER DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        conn.close()
        print("Database and Table are Created")


