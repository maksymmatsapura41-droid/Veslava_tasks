with open("data.txt", "w") as file:
    file.write("Hello World")
# File is automatically closed here, even if an error occurs inside the block


'''
'r': Read (default). Error if file doesn't exist.
'w': Write. Creates new or overwrites existing.
'a': Append. Adds to the end of the file.
'b': Binary mode (for images/PDFs).
'''