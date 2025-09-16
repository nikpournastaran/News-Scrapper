import sqlite3

DATABASE_NAME = "news_database.db"

def connect_db():
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_table():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS news(
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
            print("Database and Table are Created successfully.")
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
        finally:
            conn.close()
    else:
        print("Could not connect to database.")