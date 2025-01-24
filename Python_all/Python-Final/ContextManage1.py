from contextlib import contextmanager
import os


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

with change_dir('/Users/User/Desktop/Python (Phitron-FB)/png'):
    print(os.listdir())
    
with change_dir('/Users/User/Desktop/Python (Phitron-FB)/json'):
    print(os.listdir())



# cwd = os.getcwd()
# os.chdir('png')
# print(os.listdir())
# os.chdir(cwd)

# cwd = os.getcwd()
# os.chdir('json')
# print(os.listdir())
# os.chdir(cwd)


# @contextmanager
# def open_file(file,mode):
#     try:
#         f = open(file, mode)
#         yield f
#     finally:
#         f.close()

# with open_file('/Users/User/Desktop/Python (Phitron-FB)/Python-Final/contextSample1.txt', 'w') as f:
#     f.write('Updated-Lorem ipsum dolor sit amet, consecteur adipiscing elit.')

# print(f.closed)



# class Open_File():

#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode 

#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
    
#     def __exit__(self, exec_type, exc_val, traceback):
#         self.file.close()

# with Open_File('/Users/User/Desktop/Python (Phitron-FB)/Python-Final/contextSample.txt', 'w') as f:
#     f.write('Testing')

# print(f.closed)       