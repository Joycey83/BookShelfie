# Import connect module
from connect import *


def delete_book_record():
    try:
        dbCon, dbCursor = db_access()
       # check if songID exist
        book_id = int(input("Enter the book ID to delete the record: "))
        dbCursor.execute("SELECT * FROM books WHERE BookID = ?",(book_id,))

        row = dbCursor.fetchone()

        if row == None: # is a singleton object that checks if a value exist
           print(f"No record with {book_id} exists!")
        else: # if there is a match with the song id provide
           dbCursor.execute("DELETE from books WHERE BookID = ?", (book_id,))
           dbCon.commit()

           print(f"The record with the book ID {book_id} deleted!!")
    except  sql.OperationalError as oe:
          print(f"Failed to read because: {oe}")