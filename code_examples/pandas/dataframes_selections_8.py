import pandas as pd

df = pd.read_csv("data.csv", index_col="Duration")

print(df.to_string())

# Selection by column
# print(df["Duration"])
# print(df[["Calories","Pulse"]])

# print(df)

# # selection by row
# result = df.loc[60, "Calories"]
# print(result.to_string())

# selection by indexes, second argument is how many columns you want
print(df.iloc[0:10:2, 0:2])
