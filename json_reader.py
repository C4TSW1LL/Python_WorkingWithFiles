import json

with open("users.json", "r") as f:
    users = json.loads(f.read())

json_data = []
for i in range(len(users)):
    users_data = {'name': users[i]['name'], 'gender': users[i]['gender'], 'address': users[i]['address'], 'age': users[i]['age']}
    json_data.append(users_data)
print(len(json_data))

# with open('result.json', 'w') as result_file:
#     s = json.dumps(json_data, indent=4)
#     result_file.write(s)

# for user in users:
#     print(user)