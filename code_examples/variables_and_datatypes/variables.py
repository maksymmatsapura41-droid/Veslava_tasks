# --- LEGAL NAMES ---
user_age = 25       # snake_case (standard convention)
_internal_id = 99   # Starting with underscore is allowed
item2 = "Apple"     # Numbers are allowed as long as they aren't first
TOTAL_PRICE = 100   # Used for constants

# --- ILLEGAL NAMES (Will cause SyntaxError) ---
# 2user = "Bob"     # Cannot start with a number
# user-name = "Bob" # Cannot use hyphens (Python thinks it's subtraction)
# user space = 10   # Cannot contain spaces
# global = True     # 'global' is a reserved keyword


# Case-sensitive
# These are three DIFFERENT variables (separate boxes in memory)
player = "Mario"
Player = "Luigi"
PLAYER = "Wario"

print(player) # Mario
print(Player) # Luigi
print(PLAYER) # Wario