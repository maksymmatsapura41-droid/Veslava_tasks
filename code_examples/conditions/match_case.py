# --- MATCH-CASE EXAMPLE ---
def handle_command(command):
    match command.split():
        case ["quit"]:
            print("Goodbye!")
        case ["load", filename]:
            print(f"Loading {filename}...")
        case ["move", x, y] if int(y) > 0: # Case with a 'Guard' (extra if)
            print(f"Moving to {x}, {y}")
        case _:
            print("Unknown command")

handle_command("load data.txt")
handle_command("move 10 20")