import pandas as pd

data = {
    "Department": ["IT", "HR", "IT", "HR", "Finance"],
    "Salary": [60000, 50000, 65000, 52000, 70000]
}

df = pd.DataFrame(data)

grouped = df.groupby("Department")["Salary"].mean()

print(grouped)

