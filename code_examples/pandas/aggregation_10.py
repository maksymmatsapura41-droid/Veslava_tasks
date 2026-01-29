import pandas as pd

df = pd.read_csv("data.csv")

# Statistic of whole Dataframe
print(df.mean())

# if your dataframe/file has non-numeric values you can add numeric_only argument
# to the mean function, and then you will get avg value of numeric_columns. This attribute
# is available to all aggregation functions - min, max, sum



print(df.mean(numeric_only=True))

print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
print(df.sum(numeric_only=True))

print(df.count(numeric_only=True))

# Statistic of single column
print(df["Calories"].mean(numeric_only=True))

print(df["Calories"].min(numeric_only=True))
print(df["Calories"].max(numeric_only=True))
print(df["Calories"].sum(numeric_only=True))

print(df["Calories"].count())


# Group by
group = df.groupby("Duration")
print(group["Pulse"].mean())