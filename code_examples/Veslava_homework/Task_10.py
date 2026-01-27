# Homework №3
## Тask 10: Flexible Functions
def calculate_total(base_price, tax=0.05, *additional_cost, **metadata):
    #print(sum(base_price + args + base_price*tax))
    base_w_arg = sum(additional_cost) + base_price
    print(base_w_arg*(1+tax))
    print(metadata)

calculate_total(1, 0.5, 4, 6, category="New_cat")