# Import SQLite3 module
import sqlite3 as sql



def db_access():

    try:

        with sql.connect("assets/bookshelfie.db") as dbCon:

            dbCursor = dbCon.cursor()

            return dbCon, dbCursor
    except sql.OperationalError as oe:
        print(f"connection failed: {oe}")


if __name__ == "__main__":
    db_access()
    