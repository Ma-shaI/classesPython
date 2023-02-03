import csv

# with open('data2.csv', 'r') as f:
#     print(f.read())

with open('data2.csv', 'r') as f:
    file_reader = csv.reader(f, delimiter=';')
    for i in file_reader:
        print(i)

