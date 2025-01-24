import csv

html_output =''
names =[]

with open('/Users/User/Desktop/Python (Phitron-FB)/Python2/patron.csv', 'r') as data_file:
    csv_data= csv.DictReader(data_file)

    next(csv_data)
    next(csv_data)
    next(csv_data)
    next(csv_data)

    for line in csv_data:
        if line['FirstName'] == 'No Reward':
            break
        names.append(f"{line['FirstName']} {line['LastName']}")


html_output += f'<p>There are currently {len(names)} public contributor</p>' 
html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'
print(html_output)   


    # for item in csv_data:
    #     print(item)
    

    # We don't want the headers or first some line of bad data
#     next(csv_data)
#     next(csv_data)
#     next(csv_data)
#     next(csv_data)
    
#     for line in csv_data:
#         if line[0] == 'No Reward':
#             break
#         names.append(f'{line[0]} {line[1]}')

# html_output += f'<p>There are currently {len(names)} public contributor</p>' 
# html_output += '\n<ul>'

# for name in names:
#     html_output += f'\n\t<li>{name}</li>'

# html_output += '\n</ul>'
# print(html_output)      
# for name in names:
#     print(name)

    # print(list(csv_data))
    # print(csv_data)