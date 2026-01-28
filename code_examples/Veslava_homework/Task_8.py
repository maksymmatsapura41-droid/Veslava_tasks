# Homework №3
## Task 8: Data Processing (Comprehensions):

#List comprehension
prices = [100, 250, 45, 80, 120]
discounted_prices = [x*0.9 if x > 100 else x for x in prices]
print(discounted_prices)

#Dictionary comprehension
products = ['Laptop', 'Mouse', 'Monitor'] 
stock = [5, 20, 10]

#{key_expr: value_expr for item in iterable if condition}
inventory = {item: item1 for item, item1 in zip(products,stock)} #tuple unpacking through for-loop using two temp variables(item, item2)
print(inventory)
print(list(zip(products, stock)))

#Set comprehension
fruit_string = "apple banana apple orange banana"
unique_words = {x for x in fruit_string.split() if len(x)>5}
print(unique_words)