import sqlite3

connection = sqlite3.connect("data.db")

# title, author, year, isbn, number of pages, edition, publisher, language, genre, description, image, readed
CREATE_BOOKS_TABLE = """CREATE TABLE IF NOT EXISTS books (
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
    image TEXT,
    readed INTEGER
);
"""
INSERT_BOOKS = """INSERT INTO books (title, author, year, isbn, pages, edition, publisher, language, genre, description, image, readed) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0);"""

SELECT_ALL_BOOKS = "SELECT * FROM books;"
SELECT_BOOK_BY_TITLE = "SELECT * FROM books WHERE title = ?;"
SELECT_BOOK_BY_AUTHOR = "SELECT * FROM books WHERE author = ?;"
SELECT_BOOK_BY_YEAR = "SELECT * FROM books WHERE year = ?;"
SELECT_BOOK_BY_ISBN = "SELECT * FROM books WHERE isbn = ?;"
SELECT_BOOK_BY_PUBLISHER = "SELECT * FROM books WHERE publisher = ?;"
SELECT_BOOK_BY_LANGUAGE = "SELECT * FROM books WHERE language = ?;"
SELECT_BOOK_BY_GENRE = "SELECT * FROM books WHERE genre = ?;"
SELECT_READED_BOOKS = "SELECT * FROM books WHERE readed = 1;"
SELECT_NOT_READED_BOOKS = "SELECT * FROM books WHERE readed = 0;"
DELETE_BOOK_BY_TITLE = "DELETE FROM books WHERE title = ?;"
SET_BOOK_READED = "UPDATE books SET readed = 1 WHERE title = ?;"


def create_tables(create_table_query=CREATE_BOOKS_TABLE):
    with connection:
        connection.execute(create_table_query)


def add_book(title, author, year, isbn, pages, edition, publisher, language, genre, description, image):
    with connection:
        connection.execute(INSERT_BOOKS, (title, author, year, isbn, pages, edition, publisher, language, genre, description, image))


def get_books():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_BOOKS)
        return cursor.fetchall()


def read_book(title):
    with connection:
        connection.execute(SET_BOOK_READED, (title,))


def get_readed_books():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_READED_BOOKS)
        return cursor.fetchall()


def get_not_readed_books():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_NOT_READED_BOOKS)
        return cursor.fetchall()


def delete_book(title):
    with connection:
        connection.execute(DELETE_BOOK_BY_TITLE, (title,))
