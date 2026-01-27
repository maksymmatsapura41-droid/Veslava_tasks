# Homework №4
## Task 12: The Multi-Type Processor
###Topics: Functions, List Comprehensions, Type Checking.

list1= [2, "cat", 3.0, 5, False]
def clean_and_transform(listinsert):
    newlist = ["even" if isinstance(x) and x % 2 ==0 else "odd" for x in listinsert]
    return newlist
print(clean_and_transform(list1))