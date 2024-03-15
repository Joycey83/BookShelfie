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

    # display the contents held in the menu_choices repeatedly
    while option not in optionsList:
        print(menu_choices)
 
        # re-assign the options variable to accept string user input
        option = input("Enter an option from the menu choices above: ") # "1"/"2"/"4.5..6.."
 
        # check if the value entred and stored in the option variable is in the optionsList
        if option not in optionsList:
            print(f"{option} is not a valid choice! ")
    return option

main_program = True # can be toggle to False if required(to exit the loop below)
 
while main_program: #same as while True
    # call/invoke invoke the books_menu() funcion and assign it to a variable
 
    menu_options = books_menu() # books_menu() returns = "1"/"2"/"4.5..6.."
 
    # check if "1"/"2"/"4.5..6.." =="1"
    if menu_options == "1":
        # call the file name readrecords and the function read_all_books()
        readbooksrecord.read_all_books()
 
        # check if "1"/"2"/"4.5..6.." =="2"
    elif menu_options == "2":
        # call the filename booksrecord and the function insert_record()
        booksrecord.insert_record()
    elif menu_options == "3":
        updatebookrecord.update_book_record()
    elif menu_options == "4":
        deletebookrecord.delete_books()
    elif menu_options == "5":
        report.report()
    else: #re-assign the value to False to exit the loop
        main_program = False
input("Press enter to exit: ")