import csv

html_output =''
names =[]

with open('Python/patrons.csv', 'r') as file_data:
    csv_reader = csv.DictReader(file_data)

    next(csv_reader)

    for line in csv_reader:
        if line ['FirstName'] == 'No Reward':
            break
        names.append(f'{line["FirstName"]} {line["LastName"]}')


html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'
print(html_output)




# import csv

# html_output = ''
# names =[]

# with open('Python/patrons.csv', 'r') as file_data:
#     csv_data = csv.DictReader(file_data)

#     next(csv_data)

#     for line in csv_data:
#         if line['FirstName'] == 'No Reward':
#             break
#         names.append(f'{line['FirstName']} {line['LastName']}')

# html_output += f'<p>There are currently {len(names)} public contributor. Thank You!</p>'

# html_output += '\n<ul>'

# for name in names:
#     html_output += f'\n\t<li>{name}</li>'

#     html_output += '\n</ul>'
# print(html_output)



# import csv

# html_output =''
# names =[]

# with open('Python/patrons.csv', 'r') as data_file:
#     csv_data = csv.DictReader(data_file)

#     for item in csv_data:
#         print(item)
    
#     # We don't want first line bad data
#     next(csv_data)

#     for line in  csv_data:
#         if line['FirstName'] =='No Reward':
#             break
#         names.append(f"{line['FirstName']} {line['LastName']}")

# html_output += f'<p>Thera are currently {len(names)} public contributors. Thank You!</p>'

# html_output += '\n<ul>'

# for name in names:
#     html_output += f'\n\t<li>{name}</li>'

# html_output += '\n</ul>'

# print(html_output)

