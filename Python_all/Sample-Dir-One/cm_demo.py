import os
from contextlib import contextmanager

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield 
    finally:
        os.chdir(cwd)
    
with change_dir('Sample-Dir-One'):
    print(os.listdir())

with change_dir('Sample-Dir-Two'):
    print(os.listdir())


# cwd = os.getcwd()
# os.chdir('Sample-Dir-One')
# print(os.listdir())
# os.chdir(cwd)

# cwd = os.getcwd()
# os.chdir('Sample-Dir-Two')
# print(os.listdir())
# os.chdir(cwd)




# from contextlib import contextmanager

# @contextmanager
# def open_file(file, mode):
#     try:
#         f = open(file, mode)
#         yield f
#     finally: 
#         f.close()

# with open('sampleNew.txt', 'w') as f:
#     f.write('Lorem ipsum dolor sit amet, consectur adipiscing alit.')

# print(f.closed)


# class Open_File():

#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode

#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file

#     def __exit__(self, exc_type, exc_val, traceback):
#         self.file.close()

# with Open_File('sample.txt', 'w') as f:
#     f.write('Testing')

# print(f.closed)