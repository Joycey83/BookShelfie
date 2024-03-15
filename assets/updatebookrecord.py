# Import connect module
from connect import *


def update_book_record():
    try:
        dbCon, dbCursor = db_access()

        book_id = int(input("Enter BookID to update a record: "))
        dbCursor.execute("SELECT * FROM books WHERE BookID = ?",(book_id,))

        row = dbCursor.fetchone()

        if row == None:# if there is no match with the book_id provided
            print(f"No record with BookID {book_id} exists in the books table")

        else:# if there is a match with the book_id provided
            num_fields = input("Enter N to update one field or Y to update all fields: ").upper()
             
        if num_fields == "Y":
                # update all fields  
            book_title = input("Update book title:")
            author_name = input("Update book author:")
            book_publisher = input("Update publisher:")
            book_pub_year = int(input("Update book publication year:"))
            isbn_number = input("Update ISBN Number:")
            book_genre = input("Update book genre:")
            book_lang = input("Update the language: ")
            book_pg_count = int(input("Update the page count: "))
            book_price = float(input("Update the price: "))

        # perform update 
        dbCursor.execute("UPDATE songs SET Title =?, Author=?, Publisher=?, Publication_year=?, ISBN=?, Genre=?, Language=?, Page_count=?, Price=? WHERE BookID =?",(book_title,author_name,book_publisher,book_pub_year,isbn_number,book_genre,book_lang,book_pg_count,book_price))
        dbCon.commit()
        print(f"All fields in the record {book_id} updated in the songs table")