# Import connect module


from connect import *



def books_tbls():

    dbCon, dbCursor = db_access()

    dbCursor.execute(
    """
CREATE TABLE "books" (
	"BookID"	INTEGER NOT NULL UNIQUE,
	"Title"	TEXT,
	"Author" TEXT,
    "Publisher" TEXT,
    "Publication_year" INTEGER,
    "ISBN" TEXT,
	"Genre"	TEXT,
    "Language" TEXT,
    "Page_count" INTEGER,
	PRIMARY KEY("BookID" AUTOINCREMENT)
)"""
)

