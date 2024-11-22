import random

first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria']

last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']

street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park', 'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill']

fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale', 'Bedrock', 'South Park', 'Atlantis', 'Mordor', 'Olympus', 'Dawnstar', 'Balmora', 'Gotham', 'Springfield', 'Quahog', 'Smalltown', 'Epicburg', 'Pythonville', 'Faketown', 'Westworld', 'Thundera', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria', 'Winterfell', 'Braavos‎', 'Lakeview']

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

for num in range(100):
    first = random.choice(first_names)
    last = random.choice(last_names)

    phone = f'{random.randint(100, 999)}-555-{random.randint(1000, 9999)}'

    street_num = random.randint(100, 999)
    street = random.choice(street_names)
    city = random.choice(fake_cities)
    state = random.choice(states)
    zip_code = random.randint(10000, 99999)

    address = f'{street_num} {street} St., {city} {state} {zip_code}'

    email = first.lower() + last.lower() + '@bogusemail.com'

    print(f'{first} {last}\n{phone}\n{address}\n{email}\n')

























# deck = list(range(1, 53))
# hand = random.sample(deck, k =5 )
# print(hand)

# deck = list(range(1, 53))
# hand = random.sample(deck, k =10)
# print(hand)

# deck = list(range(1, 53))
# hand = random.sample(deck, k=5)
# print(hand)

# deck = list(range(1, 53))
# random.shuffle(deck)
# print(deck)

# deck = list(range(1, 53))
# random.shuffle(deck)
# print(deck)

# deck = list(range(1, 53))
# random.shuffle(deck)
# print(deck)


# colors = ['Red','Black','Green']
# value = random.choices(colors, weights=[18,18,2], k=10)
# print(value)



# value = random.choices(colors, weights=[18,18,2], k=10)
# print(value)

# greetings = ['hi', 'hello', 'good nigth', 'good morning', 'good noon']



# value = random.choice(greetings)
# print(value + ', Bappy!')


# greetings = ['hi', 'hello', 'good nigth', 'good morning', 'good noon']
# value = random.choice(greetings)
# print(value)


# value = random.choice(greetings)
# print(value)


# value = random.choice(greetings)
# print(value)

# value = random.choice(1,234,56,34)
# print(value)
# value = random.randint(0,1)
# print(value)

# value = random.randint(1, 100)
# print(value)

# value2 = random.uniform(1,100)
# print(value2)
# value = random.random()
# print(value)

# value1 = random.uniform(1,50)
# print(value1)

# value = random.random()
# print(value)

# value = random.uniform(1,50)
# print(value)

# value = random.uniform(1,100)
# print(value)

# value = random.random()
# print(value)