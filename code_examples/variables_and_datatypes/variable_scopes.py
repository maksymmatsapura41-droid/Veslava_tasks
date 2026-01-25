# Local Scope

def my_function():
    local_var = "I'm inside" # Created inside the function
    print(local_var)

my_function()
# print(local_var) # ERROR! The variable died when the function finished

# -----------------------------------------------------------

#Enclosing (Non-local) Scope
def outer_function():
    outer_var = "I'm in the outer box"

    def inner_function():
        # The inner function can see the outer_var
        outer_var = "other"
        print(f"Inner sees: {outer_var}")

    inner_function()

outer_function()

# -----------------------------------------------------------

global_var = "I'm everywhere"

def check_global():
    # We can read the global variable inside the function
    print(f"Function sees: {global_var}")

check_global()
print(f"Main script sees: {global_var}")