# Import connect module
from connect import *


def read_all_books():
    try:
        dbCon, dbCursor = db_access()

        dbCursor.execute("SELECT * FROM books")