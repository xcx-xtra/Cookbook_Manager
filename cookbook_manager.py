# Author: Webster Boeing
# Date: 2/20/2025
# Description: A Python script to manage a SQLite database of hipster cookbooks and track borrowing records.


import sqlite3
from sqlite3 import Error
from datetime import datetime

def create_connection():
    """ Create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect('hipster_cookbooks.db')
        print(f"Successfully connected to SQLite {sqlite3.version}")
        return conn
    except Error as e:
        print(f"Error establishing connection with the void: {e}")
        return None

def create_tables(conn):
    """ Create tables for storing cookbooks and borrowing records """
    try:
        cursor = conn.cursor()
        # Create cookbooks table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS cookbooks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year_published INTEGER,
            aesthetic_rating INTEGER,
            instagram_worthy BOOLEAN,
            cover_color TEXT
        );''')
        
        # Create borrowed cookbooks table to track lending
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS borrowed_cookbooks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cookbook_id INTEGER NOT NULL,
            friend_name TEXT NOT NULL,
            date_borrowed TEXT NOT NULL,
            date_returned TEXT,
            FOREIGN KEY (cookbook_id) REFERENCES cookbooks (id)
        );''')
        
        print("Successfully created tables.")
    except Error as e:
        print(f"Error creating tables: {e}")

def track_borrowed_cookbook(conn, cookbook_id, friend_name, date_borrowed):
    """Track which friend borrowed your cookbook and when"""
    if not friend_name or not date_borrowed:
        print("Friend name and borrow date are required!")
        return
    
    try:
        cursor = conn.cursor()
        # Insert new borrowing record
        cursor.execute("""
        INSERT INTO borrowed_cookbooks (cookbook_id, friend_name, date_borrowed)
        VALUES (?, ?, ?)""", (cookbook_id, friend_name, date_borrowed))
        conn.commit()
        print(f"{friend_name} borrowed cookbook ID {cookbook_id} on {date_borrowed}.")
    except Error as e:
        print(f"Error tracking borrowed cookbook: {e}")

def create_photoshoot_plan(conn, cookbook_id):
    """Generate Instagram-worthy photo layout suggestions based on cover_color and aesthetic_rating"""
    try:
        cursor = conn.cursor()
        # Retrieve cookbook details
        cursor.execute("SELECT title, aesthetic_rating, cover_color FROM cookbooks WHERE id = ?", (cookbook_id,))
        book = cursor.fetchone()
        if not book:
            print("Cookbook not found!")
            return
        
        title, aesthetic_rating, cover_color = book
        print(f"\n📸 Photoshoot Plan for {title} 📸")
        
        # Suggested photo angles based on aesthetic rating
        angles = ["Flat Lay", "Close-up Shot", "Side Profile", "Over-the-Shoulder"]
        
        # Props recommendations based on cover color
        props = {"Forest Green": "Wooden Table, Fresh Herbs", "Beige": "Neutral Linen, Vintage Plates", 
                 "Denim": "Rustic Backdrop, Mason Jars", "Retro Orange": "70s Decor, Funky Plates"}
        
        # Suggested hashtags for social media
        hashtags = ["#FoodPhotography", "#AestheticEats", "#CookbookLove", "#InstaChef"]
        
        print(f"🎨 Suggested Photo Angles: {', '.join(angles[:aesthetic_rating])}")
        print(f"🌿 Recommended Props: {props.get(cover_color, 'Minimalist Background, Soft Lighting')}")
        print(f"📢 Hashtags: {', '.join(hashtags)}")
        print("----------------------------")
    except Error as e:
        print(f"Error creating photoshoot plan: {e}")

def main():
    """Main function to establish connection and manage database operations"""
    conn = create_connection()
    if conn is not None:
        create_tables(conn)
        
        print("\nTracking a borrowed cookbook...")
        track_borrowed_cookbook(conn, 2, "Willow", datetime.now().strftime("%Y-%m-%d"))
        
        print("\nGenerating a photoshoot plan...")
        create_photoshoot_plan(conn, 3)
        
        conn.close()
        print("\nDatabase connection closed.")
    else:
        print("Error! Unable to establish a database connection.")

if __name__ == '__main__':
    main()
