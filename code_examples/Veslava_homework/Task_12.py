# Homework №4
## Task 12: The Multi-Type Processor
###Topics: Functions, List Comprehensions, Type Checking.

list1= [2, "cat", 3.0, 5, False]
def clean_and_transform(listinsert):
    newlist = [x for x in listinsert if isinstance(x, (float, int)) and not isinstance(x, bool)]
    newlist = [x*x if x % 2 ==0 else x*10 for x in newlist]
    return newlist
print(clean_and_transform(list1))