import csv

csv_col = ['ID', 'Name', 'Country']  

# Dictionary data
dict_data = [
    {'ID': 1, 'Name': 'Alex', 'Country': 'India'},
    {'ID': 2, 'Name': 'Aleena', 'Country': 'India'},
    {'ID': 3, 'Name': 'Minu', 'Country': 'UK'},
    {'ID': 4, 'Name': 'Ebin', 'Country': 'USA'},
    {'ID': 5, 'Name': 'Jimmy', 'Country': 'India'}
]

csv_file1 = "Names.csv"  

with open(csv_file1, 'w', newline='') as file1:
    writer = csv.DictWriter(file1, fieldnames=csv_col)
    writer.writeheader()  
    for data1 in dict_data:
        writer.writerow(data1)

print("Data successfully written to CSV file.")


with open(csv_file1, 'r', newline='') as file1:
    reader = csv.DictReader(file1)
    print("\nCSV file as a dictionary:\n")
    for row in reader:
        print(row)
