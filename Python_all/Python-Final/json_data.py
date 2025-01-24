import json

from urllib.request import urlopen

with urlopen("https://jsonplaceholder.typicode.com/users") as response:
    source = response.read()
data = json.loads(source)

usd_rate = dict()

# print(source)

# data = json.loads(source)
# for item in data['zipcode']:
#     print(item)

# for item in data['ids']['username']:
#     print(item)

# print(json.dumps(data, indent=2))
# print(len(data['id']['name']))

# print(len(data))

# import json

# with open('/Users/User/Desktop/Python (Phitron-FB)/states.json') as f:
#     data = json.load(f)

# for state in data['states']:
#     # print(state['name'], state['abbreviation'])
#     del state['area_codes']

# with open('/Users/User/Desktop/Python (Phitron-FB)/new_states.json', 'w') as f:
#     json.dump(data, f, indent=2, sort_keys=True)


# people_string = '''{
#   "people": [
#     {
#       "name": "Alice Johnson",
#       "phone": "555-1234",
#       "email": ["alice.johnson@example.com", "alice2.johnson@example.com"],
#       "has_license": true
#     },
#     {
#       "name": "Bob Smith",
#       "phone": "555-5678",
#       "email": null,
#       "has_license": false
#     },
#     {
#       "name": "Charlie Brown",
#       "phone": "555-8765",
#       "email": "charlie.brown@example.com",
#       "has_license": true
#     },
#     {
#       "name": "Diana Prince",
#       "phone": "555-4321",
#       "email": "diana.prince@example.com",
#       "has_license": true
#     },
#     {
#       "name": "Ethan Hunt",
#       "phone": "555-1357",
#       "email": "ethan.hunt@example.com",
#       "has_license": false
#     },
#     {
#       "name": "Fiona Gallagher",
#       "phone": "555-2468",
#       "email": "fiona.gallagher@example.com",
#       "has_license": true
#     },
#     {
#       "name": "George Costanza",
#       "phone": "555-3579",
#       "email": "george.costanza@example.com",
#       "has_license": false
#     },
#     {
#       "name": "Hannah Baker",
#       "phone": "555-8642",
#       "email": "hannah.baker@example.com",
#       "has_license": true
#     },
#     {
#       "name": "Ian Malcolm",
#       "phone": "555-9513",
#       "email": "ian.malcolm@example.com",
#       "has_license": true
#     },
#     {
#       "name": "Julia Roberts",
#       "phone": "555-7531",
#       "email": "julia.roberts@example.com",
#       "has_license": false
#     }
#   ]
# }'''


# data = json.loads(people_string)

# for person in data['people']:
#     # print(person['name'])
#     del person['phone']

# new_string = json.dumps(data,indent=2, sort_keys=True)
# print(new_string)

# new_string = json.dumps(data, indent=2, sort_keys=True)
# print(new_string)


# data = json.loads(people_string)
# print(type(data))
# print(type(data['people']))
# print(data['people'])
# for person in data['people']:
#     print(person['name'])
    # print(person['name'])
    # print(person['phone'])


# data = json.loads(people_string)
# print(type(data['people']))

# for person in data['people']:
#     print(person['phone'])
    # print(person['name'])
    # print(person['email'])


# data = json.loads(people_string)

# print(type(data['people']))
# print(data)
# data = json.__loader__(people_string)
# print(type(data))