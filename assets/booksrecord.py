
# Import connect module
from connect import *


# Insert book records in the books table


def insert_record():
    try:
        dbCon, dbCursor = db_access()


        book_title = input("Enter book title:")
        author_name = input("Enter book author:")
        book_publisher = input("Enter publisher:")
        book_pub_year = input("Enter book publication year:")
        isbn_number = input("Enter ISBN Number:")
        book_genre = input("Enter book genre:")
        book_lang = input("Enter the language: ")
        book_pg_count = input("Enter the page count: ")

        dbCursor.execute("INSERT INTO songs (Title,Author,Publisher,Publication_year,ISBN,Genre,Language,Page_count) VALUES(?,?,?,?,?,?,?,?)",(book_title,author_name,book_publisher,book_pub_year,isbn_number,book_genre,book_lang,book_pg_count))

        dbCon.commit()

