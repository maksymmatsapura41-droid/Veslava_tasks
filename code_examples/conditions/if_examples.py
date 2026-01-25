# --- TRUTHINESS EXAMPLE ---
items = []

# Instead of 'if len(items) == 0:'
print(bool(items))
if not items:
    # This block runs because an empty list is Falsy
    print("The list is empty!")


# Structure: [on_true] if [expression] else [on_false]
age = 20
status = "Adult" if age >= 18 else "Minor"

print(status) # Output: Adult


# val = None
# val_1 = False
# val_3 = 0
# val_4 = [0]
#
# if val_4:
#     print("Val is True")
# else:
#     print("Val is False")