import csv

html_output =''
names = []

with open('/Users/User/Desktop/Python (Phitron-FB)/Python-Final/patrons.csv' , 'r') as data_file:
    csv_data = csv.DictReader(data_file)

    # for item in csv_data:
    #     print(item)


    # We don't want headers and first some lines of bad data
    next(csv_data)
    next(csv_data)
    # next(csv_data)
    # next(csv_data)

    for line in  csv_data:
        if line['FirstName'] == 'No Reward':
            break
        names.append(f'{line['FirstName']} {line['LastName']}')

html_output += f'<p>There are currently {len(names)} as public contributors. Thank You!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)

# for name in names:
#     print(name)

    # print(list(csv_data))

    # for line in csv_data:
    #     print(line)

    # print(csv_data)


















# import csv

# with open('/Users/User/Desktop/Python (Phitron-FB)/Python-Final/data.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     with open('/Users/User/Desktop/Python (Phitron-FB)/Python-Final/new_data1.csv', 'w') as new_file:
#             fieldNames =['first_name', 'last_name']
#             csv_writer = csv.DictWriter(new_file, fieldnames=fieldNames, delimiter='\t')

#             csv_writer.writeheader()

#             for line in csv_reader:
#                 del line['email']
#                 csv_writer.writerow(line)


    # for line in csv_reader:
    #     print(line['email'])




# with open('/Users/User/Desktop/Python (Phitron-FB)/Python-Final/new_data.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter='\t')

#     for line in csv_reader:
#         print(line)



# with open('/Users/User/Desktop/Python (Phitron-FB)/Python-Final/data.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)


#     with open('/Users/User/Desktop/Python (Phitron-FB)/Python-Final/new_data.csv', 'w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='\t')


        
#         for line in csv_reader:
#             csv_writer.writerow(line)

    # next(csv_reader)

    # for line in csv_reader:
    #     print(line[2])