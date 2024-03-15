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
            
            else:
                print("*" * 140)
                print(f"{'BookID':<5}|{'Title':<30}|{'Author':<20}|{'Publisher':<10}|{'Publication_year':<15}|{'ISBN':<14}|{'Genre':<10}|{'Language':<10}|{'Page_count':<10}|{'Price':<5}")
                print("*" * 140)
                print(f"{row[0]:<5}|{row[1]:<30}|{row[2]:<20}|{row[3]:<10}|{row[4]:<15}|{row[5]:<14}|{row[6]:<10}|{row[7]:<10}|{row[8]:<10}|{row[9]:<5}")
                print("-" * 140)
            
        elif search_field.title() in ["Title", "Author", "Publisher","Publication_year","ISBN","Genre","Language","page_count","Price"]:
            #Search by Title or Artist or Genre
            str_input = input(f"Enter the value for the field {search_field}: ")
           
            dbCursor.execute(f"SELECT * FROM songs WHERE {search_field} LIKE ?", (f'%{str_input}%',))

            rows = dbCursor.fetchall()

            if not rows:
                print(f"No record with field {search_field} matching {str_input} in the books table")
            else:
                # display all matched records from the books table
                print("*" * 140)
                print(f"{'BookID':<5}|{'Title':<30}|{'Author':<20}|{'Publisher':<10}|{'Publication_year':<15}|{'ISBN':<14}|{'Genre':<10}|{'Language':<10}|{'Page_count':<10}|{'Price':<5}")
                print("*" * 140)
                for records in rows:
                    print(f"{records[0]:<5}|{records[1]:<30}|{records[2]:<20}|{records[3]:<10}|{records[4]:<15}|{records[5]:<14}|{records[6]:<10}|{records[7]:<10}|{records[8]:<10}|{records[9]:<5}")
                print("-" * 140)
                 
        else:
            print(f"Search field {search_field} Invalid! ")
    except sql.OperationalError as e:
        print(f"Search error: {e}")
if __name__ == "__main__":
    report()
 