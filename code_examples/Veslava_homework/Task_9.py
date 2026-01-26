# Homework №3
## Task 9: Logic and Loops
def loop_exercise():
    for item in range(21):
        if item % 3 == 0:
            print("Fix")
        elif item % 5 == 0:
            continue
        elif item == 17:
            break

print(loop_exercise())
