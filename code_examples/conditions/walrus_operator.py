# --- WALRUS EXAMPLE ---
# We assign the length to 'n' AND check it at the same time
if (n := len([10, 20, 30])) < 2:
    print(f"List is too long with {n} elements")

print(n)