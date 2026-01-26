# Homework №2
## Task 6: Selective Data Aggregation (continue & set)
readings = [25, -1, 30, 0, 25, 42, -5, 30]

def checkreading(list_w_readings):
    '''Cleans up the readings'''
    newset = set()
    for item in list_w_readings:
        if item <= 0:
            continue
    else:
        newset = {item for item in list_w_readings}
    print(newset)

checkreading(readings)