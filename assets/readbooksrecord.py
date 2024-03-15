# Import connect module
from connect import *


def read_all_books():
    try:
        dbCon, dbCursor = db_access()

        dbCursor.execute("SELECT * FROM books")

        all_books = dbCursor.fetchall()



        if all_books:
            print("*" * 140)
            # format output BookID, Title, Author, Publisher etc
            print(f"{'BookID':<5}|{'Title':<30}|{'Author':<20}|{'Publisher':<10}|{'Publication_year':<10}|{'ISBN':<10}|{'Genre':<10}|{'Language':<10}|{'Page_count':<10}|{'Price':<10}")
            print("*" * 140)

            for aBook in all_books:
                aBook = [value if value is not None else '' for value in aBook]
                print(f"{aBook[0]:<5}|{aBook[1]:<30}|{aBook[2]:<20}|{aBook[3]:<10}|{aBook[4]:<15}|{aBook[5]:<14}|{aBook[6]:<10}|{aBook[7]:<5}|{aBook[8]:<10}|{aBook[9]:<5}")
                print("-" * 140)
            
            dbCon.commit()

        else:
            print("No books found in the books table")
    except sql.OperationalError as oe:
        print(f"Failed to read because: {oe}")

if __name__ == "__main__":
    read_all_books()
