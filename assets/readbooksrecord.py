# Import connect module
from connect import *


def read_all_books():
    try:
        dbCon, dbCursor = db_access()

        dbCursor.execute("SELECT * FROM books")

        all_books = dbCursor.fetchall()



        if all_books:
            print("*" * 300)
           #fortmat output BookID, Title, Author, Publisher etc
            print(f"{'BookID':<6}|{'Title':<25}|{'Author':<24} | {'Publisher':<24}| {'Publication_year':<15}|{'ISBN':<15}|{'Genre':<15}|{'Language':<20}| {'Page_count':<15}|{'Price':<15}")
            print("*" * 300)

        
            for aBook in all_books:
               
               print(f"{aBook[0]:<9}|{aBook[1]:<30}|{aBook[2]:<30}|{aBook[3]:<25} | {aBook[4]:<25}|{aBook[5]:<20} | {aBook[6]:<25}|{aBook[7]:<20}|{aBook[8]:<15}|{aBook[9]:<15}")
               print("-" * 300)


        else:
           print("No books found in the books table")
    except  sql.OperationalError as oe:
        print(f"Failed to read because: {oe}")

if __name__ == "__main__":
    read_all_books()