# Homework №3
## Task 9: Logic and Loops
def loop_exercise():
    for item in range(1,21):
        if item == 17:
            break
        elif item % 5 == 0:
            continue
        elif item % 3 == 0:
            print("Fix")

loop_exercise()
#print([x for x in range(1,21) if x % 3 == 0])