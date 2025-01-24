import json
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

# Replace 'YOUR_API_KEY' with your actual Fixer.io API key
API_KEY = '4269165ab637f1b25eeae242a24cec65'
url = f"http://data.fixer.io/api/latest?access_key={API_KEY}&base=USD"

try:
    with urlopen(url) as response:
        source = response.read()
    data = json.loads(source)

    # Check if the request was successful
    if data['success']:
        # Print the exchange rates
        usd_rates = data['rates']
        
        # Example: Print the exchange rate for EUR
        print(f"Exchange rate for USD to EUR: {usd_rates['EUR']}")
    else:
        print(f"Error: {data['error']['info']}")

except HTTPError as e:
    print(f'HTTP error: {e.code} - {e.reason}')
except URLError as e:
    print(f'URL error: {e.reason}')
except Exception as e:
    print(f'An error occurred: {e}')
# import json

# with  open('/Users/User/Desktop/Python (Phitron-FB)/json/states.json') as f:
#     data = json.load(f)

# for state in data['states']:
#     print(state['name'], state['abbreviation'])
#     del state['area_codes']
    
# with open('newStatesname.json', 'w') as f:
#     json.dump(data, f, indent=2)


# with open('/Users/User/Desktop/Python (Phitron-FB)/json/states.json') as  f:
#     data = json.load(f)
# for state in data['states']:
#     print(state['name'], state['abbreviation'])
#     del state['area_codes']
  
# with open('new_states.json', 'w') as f:
#     json.dump(data, f)





# people_string = '''
# {
#   "people": [
#     {
#       "name": "Alice Johnson",
#       "phone": "555-1234",
#       "email": ["johnsmith@gmail.com", "john.smith@company.com"],
#       "has_license": true
#     },
#     {
#       "name": "Bob Smith",
#       "phone": "555-5678",
#       "email": null,
#       "has_license": false
#     }
#   ]
# }
# '''
# data = json.loads(people_string)
# print(type(data['people']))
# print(data)
# for person in data['people']:
#     print(person['name'])
#     del person['phone']
# new_string= json.dumps(data, indent=2, sort_keys=True)
# print(new_string)




