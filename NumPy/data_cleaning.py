import pandas as pd

data = {
    "Name": ["A", "B", "C", "D"],
    "Score": [90, None, 85, None]
}

df = pd.DataFrame(data)


print(df.isnull())

df["Score"] = df["Score"].fillna(df["Score"].mean())

print(df)
