# Import connect module
from connect import *


def update_book_record():
    try:
        dbCon, dbCursor = db_access()

        book_id = int(input("Enter BookID to update a record: "))
        dbCursor.execute("SELECT * FROM books WHERE BookID = ?",(book_id,))