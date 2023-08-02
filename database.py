import sqlite3

connection = sqlite3.connect("data.db")

# title, author, year, isbn, number of pages, edition, publisher, language, genre, description, image
CREATE_BOOKS_TABLE = """CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    year INTEGER,
    isbn TEXT,
    pages INTEGER,
    edition TEXT,
    publisher TEXT,
    language TEXT,
    genre TEXT,
    description TEXT,
    image TEXT
);"""
CREATE_READERS_TABLE = """CREATE TABLE IF NOT EXISTS readers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    age INTEGER,
);"""
CREATE_READED_TABLE = """CREATE TABLE IF NOT EXISTS readed (
    reader_id INTEGER,
    book_id INTEGER,
    FOREIGN KEY (reader_id) REFERENCES readers(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);"""
INSERT_BOOKS = """INSERT INTO books (title, author, year, isbn, pages, edition, publisher, language, genre, description, image) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
INSERT_READERS = """INSERT INTO readers (name, surname, age) VALUES (?, ?, ?);"""
SELECT_ALL_BOOKS = "SELECT * FROM books;"
SELECT_BOOK_BY_TITLE = "SELECT * FROM books WHERE title = ?;"
SELECT_BOOK_BY_AUTHOR = "SELECT * FROM books WHERE author = ?;"
SELECT_BOOK_BY_YEAR = "SELECT * FROM books WHERE year = ?;"
SELECT_BOOK_BY_ISBN = "SELECT * FROM books WHERE isbn = ?;"
SELECT_BOOK_BY_PUBLISHER = "SELECT * FROM books WHERE publisher = ?;"
SELECT_BOOK_BY_LANGUAGE = "SELECT * FROM books WHERE language = ?;"
SELECT_BOOK_BY_GENRE = "SELECT * FROM books WHERE genre = ?;"
SELECT_READED_BOOKS = "SELECT * FROM readed WHERE reader_name = ?;"
#SELECT_NOT_READED_BOOKS = "SELECT * FROM books WHERE readed = 0;"
DELETE_BOOK_BY_TITLE = "DELETE FROM books WHERE title = ?;"
INSERT_READED_BOOK = "INSERT INTO readed (reader_id, book_id) VALUES (?, ?);"
SET_BOOK_READED = "UPDATE books SET readed = 1 WHERE title = ?;"
DELETE_READER_BY_ID = "DELETE FROM readers WHERE id = ?;"

def create_tables():
    with connection:
        connection.execute(CREATE_BOOKS_TABLE)
        connection.execute(CREATE_READERS_TABLE)
        connection.execute(CREATE_READED_TABLE)


def add_book(title, author, year, isbn, pages, edition, publisher, language, genre, description, image):
    with connection:
        connection.execute(INSERT_BOOKS, (title, author, year, isbn, pages, edition, publisher, language, genre, description, image))


def add_reader(name, surname, age):
    with connection:
        connection.execute(INSERT_READERS, (name, surname, age,))


def get_books():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_BOOKS)
        return cursor.fetchall()


def read_book(reader_id, book_id):
    with connection:
        connection.execute(INSERT_READED_BOOK, (reader_id , book_id,))


def get_readed_books(reader_name):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_READED_BOOKS, (reader_name,))
        return cursor.fetchall()


def delete_book(title):
    with connection:
        connection.execute(DELETE_BOOK_BY_TITLE, (title,))


def delete_reader(user_id):
    with connection:
        connection.execute(DELETE_READER_BY_ID, (user_id,))
