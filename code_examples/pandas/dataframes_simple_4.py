import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

# print(myvar)
# print(myvar.loc[0]) # returns Series
print(myvar.loc[[0]]) # returns Dataframe