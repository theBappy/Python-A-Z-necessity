# import os
# print(dir(os))
# print(os.getcwd())
# print(os.getcwd('\Users\User\Desktop\Python (Phitron-FB)'))
# os.chdir(os.getcwd())
# import os
# print(os.listdir())
# import os 
# os.mkdir('pyhthon-2/python-2sub')
# print(os.listdir())
# import os
# print(os.listdir())
# os.mkdir('Python3/subPython3')
# os.makedirs('Python3/subPython3')
# os.mkdir('Python-333')
# os.makedirs('Python444/subPython444')
# os.rmdir('Python-333')
# os.removedirs('Python444/subPython444')
# os.rename('test.txt', 'demo.txt')
# os.rename('demo.txt','rename.txt')
# os.rename('rename.txt', 'test.txt')
# os.rename('test.txt', 'demo.txt')
# import os
# print(os.stat('demo.txt').st_mtime)
# print(os.stat('demo.txt'))
# print(os.stat('demo.txt').st_size)
# print(os.stat('demo.txt').st_uid)
# print(os.stat('demo.txt').st_atime)
# print(os.stat('demo.txt').st_mtime)
# print(os.stat('demo.txt').st_mtime_ns)
# import os 
# from datetime import datetime
# mod_time = os.stat('demo.txt').st_mtime
# print(datetime.fromtimestamp(mod_time))
# os.environ.get('HOME')
# for dirpath, dirnames, filenames in os.walk('/Users/User/Desktop/Python/Python1 (Phitron-FB)'):
#     print("Current path: ", dirpath)
#     print('Directories: ', dirnames)
#     print('Files:' , filenames)
# print(os.environ)
# print(os.getcwd())
# 'test.txt'
# file_path = os.environ.get('/Users/User/Desktop/Python (Phitron-FB)') + 'test.txt'
# file_path = os.path.join('/Users/User/Desktop/Python (Phitron-FB)', 'text.txt')
# print(file_path)
# import os
# from datetime import datetime
# print(os.path.basename('/tmp/test.txt'))
# print(os.path.basename('/venv/test1.txt'))
# print(os.path.basename('/enn/index.html'))
# print(os.path.dirname('/tmp/test.txt'))
# print(os.path.split('/tmp/test.txt'))
# print(os.path.split('/tmp1/test.txt'))
# print(os.path.split('/tmp2/test.txt'))
# print(os.path.exists('/tmp/test.txt'))
# print(os.path.exists('/demo.txt'))
# print(os.path.isdir('Python1'))
# print(os.path.isdir('Date Model'))
# import os
# print(os.path.isfile('demo.txt'))
# print(os.path.split('/envfolder/envfile.txt'))
# print(os.path.splitext('/envfolder/envfile.txt'))
# print(os.path.splitext('/envfolder/envfile.html'))
# print(os.path.splitext('/envfolder/envfile.css'))
# import os
# print(dir(os.path))
# tday = datetime.date.today()
# print(tday)
# tday = datetime.date.today()
# prind(tday)
# tdday = datetime.date.today()
# tdda = datetime.date.today()
# tda = datetime.date.today()
# tday = datetime.date.today()
# print(tday)
# d = datetime.date(2020,12,12)
# print(d)
# d = datetime.date(2020,4,12)
# print(d)
# d = datetime.date(2020, 7, 12)
# print(d)
# import datetime
# tday = datetime.date.today()
# tdelta = datetime.timedelta(days=7)
# print(tday + tdelta)
# print(tday)
# print(tday.year)
# print(tday.month)
# print(tday.day)
# print(tday.weekday())
# print(tday.isoweekday())
# print(tday + tdelta)
# print(tday - tdelta)
# date2 = date1 + timedelta
#timedelta = date1 + date2
# import datetime
# tday = datetime.date.today()
# tdelta = datetime.timedelta(days=10)
# bday = datetime.date(2025,10,19)
# till_bday = bday - tday
# print(till_bday.days)
# print(till_bday.total_seconds())
# import datetime
# t = datetime.time(12, 20, 30, 30000)
# print(t)
# print(t.hour)
# print(t.minute)
# print(t.second)
# import datetime
# td = datetime.datetime(2020,12,12, 12,12,12, 100000)
# print(td)
# print(td.date())
# print(td.time())
# print(td.year)
# print(td.hour)
# print(td.day)
# import datetime
# td = datetime.datetime(2020,12,12, 12,12,12, 100000)
# tdelta = datetime.timedelta(hours=12)
# print(td + tdelta)
# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()
# print(dt_today)
# print(dt_now)
# print(dt_utcnow)
# import datetime
# import pytz
# dt = datetime.datetime(2016,7,27,12,30,45, tzinfo=pytz.utc)
# print(dt)
# import datetime
# import pytz
# dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)
# dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
# print(dt_mtn)
# for tz in pytz.all_timezones:
#     print(tz)
# File objects
# f = open('demo.txt', 'r')
# print(f.name)
# f.close()
# print(f.name)
# print(f.mode)
# f = open('/Users/User/Desktop/Python (Phitron-FB)/test.txt', 'r')
# f.close()
    # f_contents = f.readline()
    # print(f_contents, end='')
    # f_contents = f.readline()
    # print(f_contents, end='')
    # f_contents = f.readline()
    # print(f_contents, end='')
    # f_contents = f.readline()
    # print(f_contents, end='')
    # f_contents = f.readline()
    # print(f_contents, end='')
    # for line in f:
    #     print(line, end='')
    # f_contents = f.read(20)
    # print(f_contents, end='')
    # f_contents = f.read(20)
    # print(f_contents, end='') 
    # f_contents = f.read(20)
    # print(f_contents, end='')
# with open('/Users/User/Desktop/Python (Phitron-FB)/test.txt', 'r') as f:
#     size_to_read = 10
#     f_contents = f.read(size_to_read)
#     print(f_contents, end='')

#     f.seek(0)

#     f_contents = f.read(size_to_read)
#     print(f_contents)
    
    # print(f.tell())
    # while len(f_contents) > 0:
    #     print(f_contents, end='*')
    #     f_contents = f.read(size_to_read)
# with open('/Users/User/Desktop/Python (Phitron-FB)/test2.txt', 'w') as f:
#     f.write('Test')
#     f.seek(0)
#     f.write('R')
# with open('/Users/User/Desktop/Python (Phitron-FB)/roadmap.jpg', 'rb') as rf:
#     with open('/Users/User/Desktop/Python (Phitron-FB)/roadmap_copy.jpg', 'wb') as wf:
#       chunk_size = 1024
#       rf_chunk = rf.read(chunk_size)
#       while len(rf_chunk) > 0:
#          wf.write(rf_chunk)
#          rf_chunk = rf.read(chunk_size)
# value = random.uniform(1,10)
# print(value)
# value = random.uniform(int(1,100))
# print(value)
# value = random.uniform(1,10)
# print(value)
# print(random.uniform(1,20))
# value = random.uniform(1,10)
# print(value)
# value = random.uniform(1,10)
# print(value)
# value = random.random()
# print(value)
# value = random.random()
# print(value)
# value = random.random()
# print(value)
# import random
# value = random.uniform(1,10)
# print(value)
# print(random.randint(1,6))
# value = random.randint(1,6)
# prit(value)
# value =random.randint(1,6)
# print(value)
# value = random.randint(1,6)
# print(value)
# value = random.randint(1.7)
# print(value)
# import random
# value = random.randint(1,10)
# print(value)
# import random
# value = random.randint(0,1)
# print(value)
# import random
# greetings = ['Hi', 'Hey', 'Good Morning', "Good Noon", 'Good Night']
# value = random.choices(greetings)
# print()
# value = random.choice(greetings)
# print(value + ' Bappy')
# import random
# colors = ['red', 'green', 'blue']
# value = random.choices(colors, weights =[18, 18, 2], k=10)
# print(value)
# import random
# deck = list(range(1, 53))
# random.shuffle(deck)
# print(deck)
# import random
# deck = list(range(1,53))
# hand = random.sample(deck, k=5)
# print(hand)
# import random
# deck = list(range(1,53))
# hand = random.sample(deck, k = 5)
# print(hand)
# import random
# deck = list(range(1,53))
# hand = random.sample(deck , k = 5)
# print(hand)






          












