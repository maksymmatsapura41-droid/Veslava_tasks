def my_func(x, y):
    i = 0
    while i < len(x) and i < len(y):
        if x[i] < y[i]:
            return True
        elif x[i] > y[i]:
            return False
        else:
            i += 1
    return False

print(my_func((3, 2, 1, 0), (0, 1, 2, 3)))


def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user = build_profile("John", "Doe", location="Kyiv", field="Dev")
# Result: {'location': 'Kyiv', 'field': 'Dev', 'first_name': 'John', ...}


def add_numbers(*args):
    return sum(args)
print(add_numbers(1, 2, 3, 4)) # Result: 10


def greet(name="Guest"):
    print(f"Hello, {name}!")
greet()        # Hello, Guest!
greet("Bob")   # Hello, Bob!




def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet("Hamster", "Pip") # Correct
describe_pet("Pip", "Hamster") # Logical error: I have a Pip named Hamster.


# describe_pet(name="Pip", animal="Hamster") # Perfectly fine


def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")
greet("Alice")    # "Alice" is an argument
