# List
fruits = ["apple", "banana"]
fruits.append("cherry")  # Adding a new item
fruits[0] = "pear"       # Modifying the first item in-place
print(fruits)
# --------------------------------------------------------------------


#Tuple
coordinates = (10, 20)
# coordinates[0] = 15  # ERROR! Tuples cannot be modified after creation
# --------------------------------------------------------------------

#String
name = "Python"
# name[0] = "J"        # ERROR! Strings are immutable
new_name = "J" + name[1:] # We create a BRAND NEW string: "Jython"
# --------------------------------------------------------------------

#Dict
user = {
    "id": 1,
    "name": "Alex",
    "is_admin": True
}
# Accessing a value by its key is extremely fast
print(user["name"])
# --------------------------------------------------------------------

# Set
numbers = {1, 2, 2, 3, 3, 3}
# Output will be {1, 2, 3} because duplicates are automatically removed
print(numbers)

my_set = {"banana", "apple", "cherry"}
# Output is unordered
print(my_set)
# --------------------------------------------------------------------