import csv
from csv import DictReader

with open('books.csv', newline='') as book:
    reader = DictReader(book)

    for row in reader:
        print(row)