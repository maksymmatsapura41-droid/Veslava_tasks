# Homework №4
# Task 14:  Inventory Discount Logic
# Topics: Loops, Nested Data, Arithmetic Operations.
items = [{"name": "Laptop", "price": 1200}, {"name": "Mouse", "price": 25}, {"name": "Monitor", "price": 300}]

def updated(insert_item):
    #[(x*0.75 if x > 500 else x*0.95) for x in insert_item]
    for item in insert_item:
        discount_rate = 0.85 if item["price"] > 500 else 0.95
        item["price"] = item["price"]*discount_rate
        #item["Mark"] = item["price"]*discount_rate #to modify key, just add new and delete old:
        #item.pop("price") #Remove the old key
        #del item["price"] #Remove old key
    return insert_item

print(updated(items))