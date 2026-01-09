import csv
import sqlite3
import os

CSV_FILE = 'users.csv'
DB_NAME = 'user_data.db'

def create_sample_csv():
    if not os.path.exists(CSV_FILE):
        print(f"[-] '{CSV_FILE}' not found. Creating a sample file...")
        data = [
            ['name', 'email', 'age'],
            ['Alice Smith', 'alice@example.com', 28],
            ['Bob Jones', 'bob@example.com', 34],
            ['Charlie Brown', 'charlie@test.org', 22],
            ['Diana Prince', 'diana@aws.com', 30]
        ]
        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(data)
        print("[-] Sample CSV created.")

def init_db():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                age INTEGER
            )
        ''')
        conn.commit()
        print(f"[-] Database '{DB_NAME}' ready.")
        return conn
    except sqlite3.Error as e:
        print(f"[!] Database error: {e}")
        return None

def import_csv_to_db(conn):
    if not os.path.exists(CSV_FILE):
        print(f"[!] Error: {CSV_FILE} does not exist.")
        return

    try:
        cursor = conn.cursor()
        
        with open(CSV_FILE, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            to_insert = []
            for row in reader:
                to_insert.append((
                    row['name'], 
                    row['email'], 
                    row['age']
                ))

            cursor.executemany('''
                INSERT OR IGNORE INTO users (name, email, age)
                VALUES (?, ?, ?)
            ''', to_insert)
            
            conn.commit()
            print(f"[-] Successfully processed {len(to_insert)} rows.")
            print(f"[-] Rows inserted: {cursor.rowcount} (Duplicates were ignored).")
            
    except csv.Error as e:
        print(f"[!] CSV reading error: {e}")
    except sqlite3.Error as e:
        print(f"[!] Database insertion error: {e}")

def verify_data(conn):
    print("\n--- Current Database Content ---")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    
    if rows:
        print(f"{'ID':<5} {'Name':<20} {'Email':<25} {'Age'}")
        print("-" * 60)
        for row in rows:
            print(f"{row[0]:<5} {row[1]:<20} {row[2]:<25} {row[3]}")
    else:
        print("Database is empty.")

if __name__ == "__main__":
    create_sample_csv()
    connection = init_db()
    
    if connection:
        import_csv_to_db(connection)
        verify_data(connection)
        
        connection.close()