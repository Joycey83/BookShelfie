# Import connect module
from connect import *


def delete_book_record():
    try:
       dbCon, dbCursor = db_access()
       # check if songID exist
    book_id = int(input("Enter the book ID to delete the record: "))
    dbCursor.execute("SELECT * FROM books WHERE BookID = ?",(book_id,))