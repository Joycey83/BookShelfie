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