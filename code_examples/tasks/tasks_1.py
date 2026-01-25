# Task 1:
# Create a list called raw_data = ["Alice", "", 42, None, "Bob", 0, True].
# Create a new list cleaned_data.
# Loop through raw_data and only add an item to cleaned_data if:
# The item is Truthy (not empty, not zero, not None).
# The item is NOT a boolean (use type(item) is not bool).
# Final Step: Print how many items were removed using the difference in lengths of the two lists.


# Task 2:
# The Universal Math Function
# Topics: functions, *args, loops, if-else.
# Create a function called calculate_stats(*args) that can take any number of numerical arguments.
# If no arguments are passed, the function should return the string "No data provided".
# The function should calculate the sum, the maximum value, and the average of the numbers.
# Return these three values as a dictionary with keys: "sum", "max", and "avg".


# Task 3:
# Inventory Manager (Nested Data)
# Topics: nested for loops, dictionary iteration, else in for.
# You have a warehouse inventory represented as a dictionary:
# warehouse = {
#     "Shelf A": ["Laptop", "Monitor", "Keyboard"],
#     "Shelf B": ["Mouse", "Cable"],
#     "Shelf C": ["Printer", "Scanner"]
# }
# Write a script that:
# Asks the user for an item_to_find.
# Uses nested for loops to search through every shelf.
# If the item is found, print "Found [item] on [Shelf Name]" and break out of both loops
# (Hint: you might need a flag variable or a specific loop structure).
# If the loops finish and the item was not found anywhere, use a for-else block (or logic) to print
# "Item not in stock".