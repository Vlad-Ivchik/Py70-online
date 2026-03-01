import sqlite3
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Book:
    id: int = None
    title: str = ""
    author: str = ""
    year: int = 0
    status: str = "available"


@dataclass
class Reader:
    id: int = None
    name: str = ""
    age: int = 0


class Library:
    def __init__(self, db_name="library.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER,
                status TEXT DEFAULT 'available'
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS readers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS borrowed_books (
                reader_id INTEGER,
                book_id INTEGER,
                borrow_date TEXT,
                FOREIGN KEY (reader_id) REFERENCES readers (id),
                FOREIGN KEY (book_id) REFERENCES books (id),
                PRIMARY KEY (book_id)
            )
        ''')

        self.conn.commit()

    def add_book(self, title, author, year):
        self.cursor.execute('''
            INSERT INTO books (title, author, year, status)
            VALUES (?, ?, ?, 'available')
        ''', (title, author, year))
        self.conn.commit()
        return self.cursor.lastrowid

    def add_reader(self, name, age):
        self.cursor.execute('''
            INSERT INTO readers (name, age)
            VALUES (?, ?)
        ''', (name, age))
        self.conn.commit()
        return self.cursor.lastrowid

    def borrow_book(self, reader_id, book_id):
        self.cursor.execute('SELECT id FROM readers WHERE id = ?', (reader_id,))
        reader = self.cursor.fetchone()
        if not reader:
            print(f"Читатель с ID {reader_id} не найден")
            return False

        self.cursor.execute('SELECT status FROM books WHERE id = ?', (book_id,))
        book = self.cursor.fetchone()

        if not book:
            print(f"Книга с ID {book_id} не найдена")
            return False

        if book[0] == 'borrowed':
            print(f"Книга с ID {book_id} уже выдана")
            return False

        borrow_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.cursor.execute('''
            INSERT INTO borrowed_books (reader_id, book_id, borrow_date)
            VALUES (?, ?, ?)
        ''', (reader_id, book_id, borrow_date))

        self.cursor.execute('''
            UPDATE books SET status = 'borrowed' WHERE id = ?
        ''', (book_id,))

        self.conn.commit()
        print(f"Книга успешно выдана читателю {reader_id}")
        return True

    def return_book(self, book_id):
        self.cursor.execute('''
            SELECT book_id FROM borrowed_books WHERE book_id = ?
        ''', (book_id,))

        borrowed = self.cursor.fetchone()
        if not borrowed:
            print(f"Книга с ID {book_id} не была выдана")
            return False

        self.cursor.execute('''
            DELETE FROM borrowed_books WHERE book_id = ?
        ''', (book_id,))

        self.cursor.execute('''
            UPDATE books SET status = 'available' WHERE id = ?
        ''', (book_id,))

        self.conn.commit()
        print(f"Книга с ID {book_id} успешно возвращена")
        return True

    def search_books(self, keyword):
        self.cursor.execute('''
            SELECT id, title, author, year, status FROM books
            WHERE title LIKE ? OR author LIKE ?
        ''', (f'%{keyword}%', f'%{keyword}%'))

        results = self.cursor.fetchall()
        books = []

        for row in results:
            book = Book(id=row[0], title=row[1], author=row[2], year=row[3], status=row[4])
            books.append(book)

        return books

    def get_borrowed_books(self):
        self.cursor.execute('''
            SELECT 
                b.title,
                b.author,
                r.name as reader_name,
                bb.borrow_date
            FROM borrowed_books bb
            JOIN books b ON bb.book_id = b.id
            JOIN readers r ON bb.reader_id = r.id
            ORDER BY bb.borrow_date DESC
        ''')

        return self.cursor.fetchall()

    def get_statistics(self):
        self.cursor.execute('''
            SELECT 
                COUNT(CASE WHEN status = 'available' THEN 1 END) as available,
                COUNT(CASE WHEN status = 'borrowed' THEN 1 END) as borrowed,
                COUNT(*) as total
            FROM books
        ''')

        stats = self.cursor.fetchone()
        return {
            'available': stats[0],
            'borrowed': stats[1],
            'total': stats[2]
        }
