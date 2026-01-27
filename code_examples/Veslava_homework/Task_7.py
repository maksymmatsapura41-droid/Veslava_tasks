# Homework №2
## Task 7: The Library Catalog (dict & pass)
library = {"The Hobbit": True, "1984": False, "Python Basics": True}

def librarycheck(books):
    '''Shows you if the book is in the library'''
    for title, status in books.items():
        if status == False:
            continue
        else:
            print("Displaying: ", title)

librarycheck(library)