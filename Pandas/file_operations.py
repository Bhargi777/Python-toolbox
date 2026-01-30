import pandas as pd

# Read CSV
df = pd.read_csv("data.csv")

# Write CSV
df.to_csv("output.csv", index=False)

# Read Excel
# df = pd.read_excel("data.xlsx")

print(df.head())
