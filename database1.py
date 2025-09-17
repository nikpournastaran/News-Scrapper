import sqlite3
import os

DATABASE_NAME = "news_database.db"


#Connects to the SQLite database
def connect_db():

    conn = sqlite3.connect(os.path.join(os.getcwd(), DATABASE_NAME))
    return conn
   
#Creates the 'news' table
def create_table():
   
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS news (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    short_text TEXT,
                    image_url TEXT,
                    news_url TEXT NOT NULL UNIQUE,
                    is_active INTEGER DEFAULT 1,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
            print("Database and 'news' table created successfully.")
            return True
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
        finally:
            conn.close()
    else:
        print("Could not connect to database.")
        return False