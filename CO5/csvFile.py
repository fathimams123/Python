import csv

with open('Employee.csv', 'r', newline='') as file1:
    reader1=csv.reader(file1)
    for row in reader1:
        print(row)
