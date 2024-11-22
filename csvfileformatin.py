# import csv 

# with open('Python/names.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     with open('Python/new_names.csv', 'w') as new_file:
#             fieldNames = ['first_names', 'last_names']
#             csv_writer = csv.DictWriter(new_file, fieldnames=fieldNames, delimiter='\t')

#             csv_writer.writeheader()

#             for line in csv_reader:
#                 csv_writer.writerow(line)


# with open('Python/new_names.csv','r' ) as csv_file:
#     csv_reader= csv.reader(csv_file, delimiter='\t')

#     for line in csv_reader:
#         print(line)

# with open('Python/names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)





# import csv 
# with open('Python/names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     next(csv_reader)

#     for line in csv_reader:
#         print(line[2])


# import csv

# with open('Python/names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     next(csv_reader)

#     for line in csv_reader:
#         print(line[2])



# import csv

# with open('Python/names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
    
#     for line in csv_reader:
#         print(line)