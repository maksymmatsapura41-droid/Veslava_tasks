def divide_numbers(a, b):
    try:
        if b == 0:
            raise IndexError
        # Code that might cause an error
        result = a / b
    except ZeroDivisionError:
        # Runs if division by zero occurs
        print("Error: Division by zero is not allowed!")
    except TypeError:
        # Runs if arguments are not numbers
        print("Error: Please provide numbers only!")
    except Exception:
        print("General exception occurred!")
    else:
        # Runs ONLY if NO exceptions were raised
        print(f"Success! The result is: {result}")
    finally:
        # Runs ALWAYS, regardless of what happened above
        print("Cleanup: Operation finished.")

# Testing the function
divide_numbers(10, 2)   # Success case
divide_numbers(10, 0)   # Triggers ZeroDivisionError
divide_numbers(10, "5") # Triggers TypeError


