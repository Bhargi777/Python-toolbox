import csv

with open("data.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if int(row["age"]) > 16:
            print(row)
