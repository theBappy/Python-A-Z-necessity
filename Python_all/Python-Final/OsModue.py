# import os
# from datetime import datetime

# print(dir(os.path))

# print(os.path.splitext('PIL_demo.py'))

# print(os.path.splitext('/tmp/test.txt'))

# print(os.path.splitext('/tmp/test.txt'))


# print(os.path.basename('/tmp/test.txt'))
# print(os.path.dirname('/tmp/test.txt'))
# print(os.path.split('/tmp/test.txt'))
# print(os.path.exists('/tmp/test.txt'))
# print(os.path.isdir('PIL_demo.py'))
# print(os.path.isfile('PIL_demo.py'))


# print(os.environ.get('/Users/User/Desktop/Python (Phitron-FB)'))


# file_path =os.path.join(os.environ.get('/Users/User/Desktop/Python (Phitron-FB)'),'PIL_demo.py')
# print(file_path) 

# with open(file_path , 'w') as f:
    

# print(os.environ.get('HOME'))

# for dirpath, dirnames, filenames in os.walk('/Users/User/Desktop/Python (Phitron-FB)'):
#     print('Current Path:', dirpath)
#     print('Direcotories: ' , dirnames)
#     print('Files:' , filenames)
#     print()


# print(os.stat('PIL_demo.py').st_size)
# mod_time =os.stat('PIL_demo.py').st_mtime
# print(datetime.fromtimestamp(mod_time))

# print(os.listdir())

# os.rename('pil_demo.py', 'PIL_demo.py')

# os.rmdir('Python_Practice')
# os.removedirs('Python_practice2')

# os.mkdir('Python_Practice/sub_dir')
# os.makedirs('Python_practice2/sub_dir1')


# print(os.getcwd())

# os.chdir('/Users/User/Desktop/Python (Phitron-FB)')
# print(os.getcwd())


# print(dir(os))