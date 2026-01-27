# Homework №4
## Task 13: Advanced Password Validator

#Topics: Conditions, String Methods, Ternary Operators.
password_new = "2026Ten"
def passwordcheck(stringpass):
    if len(stringpass) >= 10 and any(x.isdigit() for x in stringpass) and any(x.isupper() for x in stringpass):
        return "Valid Password"
    else:
        return "High risk" if len(stringpass) < 6 else "Evaluation Required"

print(passwordcheck(password_new))