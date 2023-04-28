import json
import csv
from csv import DictReader



with open("users.json", "r") as f:
    users = json.loads(f.read())

json_data = []
for i in range(len(users)):
    json_data.append({'name': users[i]['name'],
                      'gender': users[i]['gender'],
                      'address': users[i]['address'],
                      'age': users[i]['age'],
                      'books': []})

with open('books.csv', newline='') as book_csv:
    reader = DictReader(book_csv)
    books = []
    for row in reader:
        books.append({'Title': row['Title'],
                  'Author': row['Author'],
                  'Genre': row['Genre']})

    for i, book in enumerate(books):
        json_data[i % len(json_data)]['books'].append(book)


with open('result.json', 'w') as result_file:
    s = json.dumps(json_data, indent=4)
    result_file.write(s)
