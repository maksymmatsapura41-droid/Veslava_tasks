# Homework №3
## Тask 10: Flexible Functions
def calculate_total(base_price, tax=0.05, *args, **kwargs):
    print(sum(base_price, base_price*tax, *args))