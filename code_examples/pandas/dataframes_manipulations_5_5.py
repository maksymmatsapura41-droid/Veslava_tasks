import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# Add column
df["mark"] = ["Good", "Bad", "Excellent"]
print(df)

# Add new rows
new_rows = pd.DataFrame([{"calories":400, "duration":40, "mark":"Good"}], index = ["day4"])
df = pd.concat([df, new_rows])
print(df)
#
# print(df)
# print(df.loc["day1"])
# print(df.loc[["day2","day3"]])
