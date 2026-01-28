# Homework №3
## Task 11: The Grade Analytics System
scores = [45, 88, 72, 91, 55, 60, 30, 99]

passed_scores = [x for x in scores if x >= 60]
print(passed_scores)

#Dictionary
##{key_expr: value_expr for item in iterable if condition}
#base solution
#dict_status = {score: "Excellent" if score > 90 else "Pass" for score in scores}
#Ternary Operator
#ternary_operator_showoff = "Excellent" if score > 90 else "Pass"
dict_status = {score: ("Excellent" if score > 90 else "Pass") for score in scores}

print(dict_status)
#Function
#{expression for item in iterable if condition}
# def process_data(*args, threshold=70):
#     return {x for x in args if x > threshold}

# print(process_data(*scores, threshold=50))
new_string = "newtext"
a, b, c, d, *e = new_string #packing creates a list
print(a, b, e) 
def process_data(*args, threshold=70):
    return {x for x in args if x > threshold}

print(process_data(*scores, threshold=50))