import os
from database1 import create_table

#create database
if __name__ == "_main1_":
    print("Attempting to create database and table...")
    
    # Check if the database file already exists
    db_path = os.path.join(os.getcwd(), "news_database.db")
    if os.path.exists(db_path):
        print("Database file already exists.")
    else:
        # If the database doesn't exist, try to create it.
        if create_table():
            print("Setup complete. You can now proceed to the next step.")
        else:
            print("Setup failed. Please check the error messages above.")