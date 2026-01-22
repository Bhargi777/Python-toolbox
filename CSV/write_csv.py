import csv

data = [
    ["name", "age"],
    ["Bhargi", 19],
    ["Jatheen", 19],
    ["Vikranth", 20],
    ["Vaista", 19],
    ["Lalithesh", 19],
]

with open("output.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)
