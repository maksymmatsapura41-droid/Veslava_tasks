import pandas as pd

df = pd.read_json('data_json.json')

print(df.to_string())