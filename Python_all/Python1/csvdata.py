import csv



with open('/Users/User/Desktop/Python (Phitron-FB)/Python2/data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open('/Users/User/Desktop/Python (Phitron-FB)/Python2/data3.csv', 'w') as new_file:
        fieldNames = ['first_name', 'last_name']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldNames , delimiter='\t')
        csv_writer.writeheader()
        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
   
    # for line in csv_reader:
    #     print(line)

# with open('/Users/User/Desktop/Python (Phitron-FB)/Python2/data.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     with open('/Users/User/Desktop/Python (Phitron-FB)/Python2/NewData1.csv' , 'w') as new_file:
#         csv_writer = csv.writer(new_file,delimiter='\t')

#         for line in csv_reader:
#             csv_writer.writerow(line)

    # for line in csv_reader:
    #     print(line)


# with open('/Users/User/Desktop/Python (Phitron-FB)/Python2/NewData1.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter='\t')
#     for line in csv_reader:
#         print(line)