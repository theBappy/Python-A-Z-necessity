import sqlite3
from contextlib import contextmanager

create_table_sql_statement = 'CREATE TABLE IF NOT EXISTS books(title TEXT, author TEXT)'
insert_into_table_sql_statement = "INSERT INTO books VALUES ('If Tomorrow Comes', 'Sidney Sheldon'), ('The Lincoln Lawyer', 'Michael Connelly')"
select_from_table_sql_statement = 'SELECT * FROM books'

@contextmanager
def database(path: str):
    connection = sqlite3.connect(path)
    try:
        cursor = connection.cursor()
        yield{'connection': connection, 'cursor': cursor}
    except Exception as e:
        print(f'an error occurred: ', {e})
    finally:
        connection.close()

def main():
    database_path = ':memory:'

    with database(database_path) as db:
        db.get('cursor').execute(create_table_sql_statement)
        db.get('connection').commit()

        db.get('cursor').execute(insert_into_table_sql_statement)
        db.get('connection').commit()

        db.get('cursor').execute(select_from_table_sql_statement)

        print(db.get('cursor').fetchall())

if __name__ == '__main__':
    main()

# import sqlite3

# create_table_sql_statement = 'CREATE TABLE IF NOT EXISTS books(title TEXT, author TEXT)'
# insert_into_table_sql_statement = "INSERT INTO books VALUES ('If Tomorrow Comes', 'Sidney Sheldon'), ('The Lincoln Lawyer', 'Michael Connelly')"
# select_from_table_sql_statement = 'SELECT * FROM books'



# class Database:
#     def __init__(self, path: str):
#        self.path = path
#     def __enter__(self):
#         self.connection = sqlite3.connect(self.path)
#         self.cursor = self.connection.cursor()
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is not None:
#             print(f'an error occurrd: {exc_val}')
#         self.connection.close()

# def main():
#     with Database(':memory:') as db:
#         db.cursor.execute(create_table_sql_statement)
#         db.connection.commit()

#         db.cursor.execute(insert_into_table_sql_statement)
#         db.connection.commit()

#         db.cursor.execute(select_from_table_sql_statement)

#         print(db.cursor.fetchall())

# if __name__ == '__main__':
#     main()


# import sqlite3

# create_table_sql_statement = 'CREATE TABLE IF NOT EXISTS books(title TEXT, author TEXT)'
# insert_into_table_sql_statement = "INSERT INTO books VALUES ('If Tomorrow Comes', 'Sidney Sheldon'), ('The Lincoln Lawyer', 'Michael Connelly')"
# select_from_table_sql_statement = 'SELECT * FROM books'

# def main():
#     database_path = ':memory:'

#     connection = sqlite3.connect(database_path)
#     cursor = connection.cursor()

#     try:
#         cursor.execute(create_table_sql_statement)
#         connection.commit()

#         cursor.execute(insert_into_table_sql_statement)
#         connection.commit()

#         cursor.execute(select_from_table_sql_statement)

#         print(cursor.fetchall())
#     except Exception as e:
#         print(f"read or write action to the database failed: {e}")
#     finally:
#         connection.close()
# if __name__ == '__main__':
#     main()   



# def main():
#     with open('books.txt', 'w') as my_file:
#         my_file.write('with context manager')
# if __name__ == '__main__':
#     main()


# def main():
#     my_file = open('books.txt', 'w')
#     try:
#         my_file.write('this is the collection of books')
#     except Exception as e:
#         print(f'writing to file failed: {e}')
#     finally:
#         my_file.close()
# if __name__ == '__main__':
#     main()

# def main():
#     my_file = open('books.txt', 'w')
#     my_file.write('If tomorrow comes by sidney sheldon')
#     my_file.close()

# if __name__ == '__main__':
#     main()


# from pymongo import MongoClient

# class MongoDBConnectionManager():
#     def __init__(self, hostname, port):
#         self.hostname = hostname
#         self.port = port
#         self.connection = None
#     def __enter__(self):
#         self.connection = MongoClient(self.hostname, self.port)
#         return self.connection
#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         self.connection.close()

# with MongoDBConnectionManager('localhost', '27017') as mongo:
#     collection = mongo.connection.SampleDb.test
#     data = collection.find({'_id': 1})
#     print(data.get('name'))

# import os
# os.remove('/Users/User/Desktop/Python (Phitron-FB)/Python-Final/cat2_copy.jpg')

# class FileManager():
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#         self.file = None
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         self.file.close()

# with FileManager('/Users/User/Desktop/Python (Phitron-FB)/Python-Final/filemanager.txt', 'w') as f:
#     f.write('creating  and writing a file with the filemanager class')
# print(f.closed)


# class FileManager():
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#         self.file = None
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         self.file.close()

# with open('/Users/User/Desktop/Python (Phitron-FB)/Python-Final/test.txt', 'w') as f:
#     f.write("Testing the geeksforgeeks")
# print(f.closed)



# class ContextManager():
#     def __init__(self):
#         print("init method called")
#     def __enter__(self):
#         print('enter method called')
#         return self
#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         print('Exit method called')
# with ContextManager() as manager:
#     print('with statement block')


# with open('/Users/User/Desktop/Python (Phitron-FB)/Python-Final/test1.txt') as f:
#     data = f.read()

# file_descriptors = []
# for x in range(100000):
#     file_descriptors.append(open('/Users/User/Desktop/Python (Phitron-FB)/Python-Final/testfile.txt','w'))