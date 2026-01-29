import pandas as pd

a = [1, 7, 2]
myvar = pd.Series(a)

# print(myvar)
#
# print(myvar[0])


myvar_labels = pd.Series(a, index = ["x", "y", "z"])

# print(myvar_labels)
#
print(myvar_labels["y"])
print(myvar_labels.loc["x"])
print(myvar_labels.iloc[0])


# Filtering
print(myvar_labels[myvar_labels > 4])