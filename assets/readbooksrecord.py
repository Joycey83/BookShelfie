# Import connect module
from connect import *


def read_all_books():
    try:
        dbCon, dbCursor = db_access()

        dbCursor.execute("SELECT * FROM books")

        all_books = dbCursor.fetchall()

        if all_books:
           print("*" * 100)
           #fortmat output BookID, Title, Author, Publisher etc
           print(f"BookID{'':<3}|Title{'':<25}|Author{'':<24}|Publisher{'':24}|Publication_year{'':<15}|ISBN{'':<15}|Genre{'':<15}|Language{'':<20}|Page_count{'':<15}|Price{'':<15}")
           print("*" * 100)