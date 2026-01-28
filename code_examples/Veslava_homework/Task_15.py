# Homework №4
## Task 15:  Matrix Integrity Checker
### Topics: Nested Loops, Conditions, Booleans.



# # Nested Comprehension
# flat = [num for row in matrix for num in row if num > 10]

# # Is equivalent to:
# for row in matrix:
#     for num in row:
#         if num > 10:
#             flat.append(num)
list_multidimensional = [[1,2],[3,4]] 

def is_valid_matrix(twodtocheck):
