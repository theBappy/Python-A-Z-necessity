import os

os.chdir('/Users/User/Desktop/Python (Phitron-FB)/png/700')

# print(os.getcwd())

for f in os.listdir():
    # print(f)
    f_name, f_ext = os.path.splitext(f)
    f_title , f_num = f_name.split('_')
    f_title= f_title.strip()
    f_num= f_title.strip()


    new_name = '{}{}'.format(f_num, f_ext)
    print(new_name)
    os.rename(f, new_name)
    