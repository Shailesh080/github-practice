import csv

marks = []

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        marks.append(float(row["marks"]))

average = sum(marks) / len(marks)

print("Average Marks:", average)
