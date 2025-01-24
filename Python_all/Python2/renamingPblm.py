# Problem Solving
import os
os.chdir('/Users/User/Desktop/Python (Phitron-FB)/Image')
# print(os.getcwd())
for f in os.listdir():
    # print(f)
    fname, f_ext = os.path.splitext(f)
    # print(filename)
    f_title, f_course, f_num = fname.split('-')
    f_title =    f_title.strip()
    f_course =    f_course.strip()
    f_num =    f_num.strip()[1:].zfill(2)
    # print(f_title)
    # print(f_num)
    new_name = '{}-{}{}'.format(f_num,f_title, f_ext)
    os.rename(f, new_name)