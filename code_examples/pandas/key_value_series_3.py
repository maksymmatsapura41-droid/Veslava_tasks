import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

myvar.loc["day3"] += 100
myvar.loc["day4"] = 100
myvar["day5"] = 100
print(myvar)

print(myvar)


import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)