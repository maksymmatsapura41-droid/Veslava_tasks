def register_user(username, age):
    if age < 18:
        # Manually triggering a ValueError
        raise ValueError("User must be at least 18 years old.")

    print(f"User {username} registered successfully.")


try:
    register_user("Alice", 16)
except ValueError as error:
    print(f"Access Denied: {error}")

'''
try: "Try this code."
except: "If it breaks, do this."
else: "If it didn't break, do this."
finally: "No matter what, do this."
raise: "I'm calling the police (triggering an error)!"
'''