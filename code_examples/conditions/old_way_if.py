# User input usually comes as a string, so we convert it to an int
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age! You haven't been born yet.")
elif age < 13:
    print("You are a Child.")
elif age < 20:
    # This runs only if age is NOT < 13 but IS < 20
    print("You are a Teenager.")
elif age < 65:
    print("You are an Adult.")
else:
    # This runs if NONE of the above were True
    print("You are a Senior.")