import re
# A basic email pattern
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

test_email = "user@example.com"

if re.match(pattern, test_email):
    print("Valid Email!")
else:
    print("Invalid Email.")