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

def books_menu():
    option = 0 # create an integer variable call option
    # create a list data structure hold string items/values and assign it to optionsList
    optionsList = ["1","2","3","4","5","6"]
 
    # call/invoke invoke the read_file funcion and assign it to a variable
    menu_choices = read_file("assets/dbmenu.txt")