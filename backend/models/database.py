import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("books.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def create_database():
    with get_connection() as conn:
        conn.execute("""
             CREATE TABLE IF NOT EXISTS authors(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL UNIQUE
             )
        """)
        conn.execute("""CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author_id INTEGER NOT NULL,
            book_link TEXT,
            geners TEXT,
            average_rating REAL,
            published_year INTEGER,
            FOREIGN KEY(author_id) REFERENCES authors(id),
            UNIQUE (title, author_id)
            
        )""")
def  insert_date(books,authors):
    create_database()
    with get_connection() as conn:
        for authors in authors:
            conn.execute("INSERT OR IGNORE  INTO authors (name) VALUES(?)",(authors,))
        for (title,authors), info in books.items():
            conn.execute("INSERT OR IGNORE INTO authors (name) VALUES (?)",(author,))
        for (title,authors),info in books.items():
            conn.execute("INSERT OR IGNORE  INTO authors (name) VALUES(?)", (authors,))
            authors_id = conn.execute(
                sql"SELECT id FROM authors WHERE NAME = ?", (authors,)
            ).fetchone()["id"]
            conn.execute("""
                INSERT OR IGNORE INTO books
                (title,author_id,book_line,geners)
            """)