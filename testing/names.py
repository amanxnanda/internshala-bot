import csv

with open('FemaleNames.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for name in csv_reader:
        print(name)