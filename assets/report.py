# Import connect module
from connect import *


def report():

    try:
        dbCon, dbCursor = db_access()
        # ask for the search field
        search_field = input("Search by BookID,Title, Author, Genre, Publisher, Publisher_year,ISBN, Genre, Language, Page_count and Price: ")

        if search_field == "BookID":
            #search by SongID
            book_id = int(input("Enter BookID: "))
            dbCursor.execute("SELECT * FROM songs WHERE BookID = ?", (book_id,))
            row = dbCursor.fetchone()

            if row is None:
                print(f"No record with BookID {book_id} exists in the books table")
 