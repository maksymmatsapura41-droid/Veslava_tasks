#Immutable
# --- IMMUTABLE: Integers ---
x = 100
print(f"Initial x: {x}, ID: {id(x)}")

x = x + 1
# Python creates a NEW object '101' and moves the name 'x' to it
print(f"Updated x: {x}, ID: {id(x)}") # ID will be DIFFERENT

# --- IMMUTABLE: Strings ---
text = "Hello"
print(f"\nInitial text: {text}, ID: {id(text)}")

text += " World"
# The original "Hello" box cannot be changed. A new "Hello World" box is created.
print(f"Updated text: {text}, ID: {id(text)}") # ID will be DIFFERENT


#Mutable
# --- MUTABLE: Lists ---
my_list = [1, 2, 3]
print(f"Initial list: {my_list}, ID: {id(my_list)}")

my_list.append(4)
# The box remains the same, we just added an item inside
print(f"Updated list: {my_list}, ID: {id(my_list)}") # ID will be THE SAME

# --- MUTABLE: Dictionaries ---
user_data = {"name": "Alice"}
print(f"\nInitial dict ID: {id(user_data)}")

user_data["age"] = 25
# We added a key-value pair, but the object identity is unchanged
print(f"Updated dict ID: {id(user_data)}") # ID will be THE SAME