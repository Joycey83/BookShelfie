# Import all CRUD modules
import booksrecord, readbooksrecord, updatebookrecord, deletebookrecord, report


# Create a function to read from a text file
def read_file(file_path):# file_path is the parameter
    try:
        with open(file_path) as open_file:
            #read the file content and save it in a variable called rf
            rf = open_file.read()# read()reads the content of the file
 
            return rf
    except FileNotFoundError as not_found:
        print(f"File not found {not_found}")