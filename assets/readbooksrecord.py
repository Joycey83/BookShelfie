# Import connect module
from connect import *


def read_all_books():
    try:
        dbCon, dbCursor = db_access()

        dbCursor.execute("SELECT * FROM books")

        all_books = dbCursor.fetchall()



        if all_books:
            print("*" * 100)
            # format output BookID, Title, Author, Publisher etc
            print(f"{'BookID':<6}|{'Title':<15}|{'Author':<15}|{'Publisher':<15}|{'Publication_year':<15}|{'ISBN':<15}|{'Genre':<15}|{'Language':<10}|{'Page_count':<10}|{'Price':<10}")
            print("*" * 100)

            for aBook in all_books:
                print(f"{aBook[0]:<9}|{aBook[1]:<30}|{aBook[2]:<10}|{aBook[3]:<10}|{aBook[4]:<10}|{aBook[5]:<10}|{aBook[6]:<10}|{aBook[7]:<10}|{aBook[8]:<10}|{aBook[9]:<10}")
                print("-" * 300)
            
            dbCon.commit()

        else:
            print("No books found in the books table")
    except sql.OperationalError as oe:
        print(f"Failed to read because: {oe}")

if __name__ == "__main__":
    read_all_books()
