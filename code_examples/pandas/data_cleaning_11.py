import pandas as pd

df = pd.read_csv("data_test.csv")

# print(df.loc[:, 'Duration'])

# Drop irrelevant columns
df = df.drop(columns=["Duration"])

# print(df)

# Handle missing data
# df = df.dropna(subset=["Calories"])
df = df.fillna({"Calories": 0})

df_with_zeroes = df[df["Calories"] == 0]
# print(df_with_zeroes)


# Replace inconsistent data
df["Calories"] = df["Calories"].replace({0:"ZERO"})

print(df[df["Calories"]=="ZERO"])