# Homework №2
## Task 7: The Library Catalog (dict & pass)
library = {"The Hobbit": True, "1984": False, "Python Basics": True}

def librarycheck(books):
    '''Shows you if the book is in the library'''
    for status in books.values():
        if status == False:
            pass
    else:
        print("Displaying: ", books.keys())

librarycheck(library)