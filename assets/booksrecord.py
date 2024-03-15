
# Import connect module
from connect import *


# Insert book records in the books table


def insert_record():
    try:
        dbCon, dbCursor = db_access()


        book_title = input("Enter book title:")
        author_name = input("Enter book author:")
        book_publisher = input("Enter publisher:")
        book_pub_year = int(input("Enter book publication year:"))
        isbn_number = input("Enter ISBN Number:")
        book_genre = input("Enter book genre:")
        book_lang = input("Enter the language: ")
        book_pg_count = int(input("Enter the page count: "))
        book_price = float(input("Enter the price: "))

        dbCursor.execute("INSERT INTO books (Title,Author,Publisher,Publication_year,ISBN,Genre,Language,Page_count,Price) VALUES(?,?,?,?,?,?,?,?,?)",(book_title,author_name,book_publisher,book_pub_year,isbn_number,book_genre,book_lang,book_pg_count,book_price))

        dbCon.commit()

        print(f"{book_title}, {author_name}, {book_publisher}, {book_pub_year}, {isbn_number}, {book_genre}, {book_lang}, {book_pg_count} and {book_price} inserted into the books table")
    
    
    except ValueError:
        print("You entered an invalid value. Please try again.")
    except sql.OperationalError as oe:
        print(f"failed because of {oe}")

if __name__ == "__main__":
    insert_record()

