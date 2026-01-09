import sqlite3
import requests
API_URL = "https://openlibrary.org/subjects/science_fiction.json?limit=5"
DB_NAME = "library.db"

def init_db():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                publication_year INTEGER
            )
        ''')
        conn.commit()
        print(f"[-] Database '{DB_NAME}' ready.")
    except sqlite3.Error as e:
        print(f"[!] Database error: {e}")
    finally:
        if conn: conn.close()

def fetch_data(url):
    print(f"[-] Fetching data from {url}...")
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("works", [])
        
    except requests.exceptions.RequestException as e:
        print(f"[!] API Request failed: {e}")
        return []

def save_books(books):
    if isinstance(books, dict):
        print("[!] Warning: Received raw dictionary. Extracting 'works' list automatically.")
        books = books.get('works', [])

    if not books:
        print("[!] No book data to save.")
        return

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        data_to_insert = []
        for book in books:
            if not isinstance(book, dict):
                continue 

            title = book.get('title', 'Unknown Title')
            authors_list = book.get('authors', [])
            author_name = authors_list[0].get('name', 'Unknown') if authors_list else 'Unknown' 
            year = book.get('first_publish_year', 0)
            data_to_insert.append((title, author_name, year))

        if data_to_insert:
            cursor.executemany('''
                INSERT INTO books (title, author, publication_year) 
                VALUES (?, ?, ?)
            ''', data_to_insert)
            conn.commit()
            print(f"[-] Successfully saved {len(data_to_insert)} books.")
        else:
            print("[!] No valid book entries found to insert.")

    except sqlite3.Error as e:
        print(f"[!] Database save error: {e}")
    finally:
        if conn: conn.close()

def display_books():
    print("\n--- Books in Local Storage ---")
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, author, publication_year FROM books")
        rows = cursor.fetchall()
        
        if not rows:
            print("No books found.")
        else:
            print(f"{'ID':<5} {'Title':<40} {'Author':<25} {'Year'}")
            print("-" * 80)
            for row in rows:
                print(f"{row[0]:<5} {row[1][:38]:<40} {row[2][:23]:<25} {row[3]}")
    except sqlite3.Error as e:
        print(f"[!] Display error: {e}")
    finally:
        if conn: conn.close()

if __name__ == "__main__":
    init_db()
    book_data = fetch_data(API_URL)
    save_books(book_data)
    display_books()

