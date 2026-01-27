# Homework №4
# Task 14:  Inventory Discount Logic
# Topics: Loops, Nested Data, Arithmetic Operations.
items = [{"name": "Laptop", "price": 1200}, {"name": "Mouse", "price": 25}, {"name": "Monitor", "price": 300}]

def updated(insert_item):
    [(x*0.75 if x > 500 else x*0.95) for x in insert_item]
    print(insert_item)
