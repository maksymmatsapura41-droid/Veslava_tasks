import pandas as pd

df = pd.read_csv("data.csv")

# Get intensive training

high_intensive_training = df[df["Pulse"] > 140]
print(high_intensive_training)

long_and_high_intensive_training = df[(df["Pulse"] > 140) & (df["Duration"] > 25)]

print(long_and_high_intensive_training)