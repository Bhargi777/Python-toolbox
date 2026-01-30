import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [22, 25, 23],
    "City": ["NY", "LA", "Chicago"]
}

df = pd.DataFrame(data)

print(df)
print(df.head())
print(df.shape)
print(df.columns)
