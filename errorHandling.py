
try:
    f = open('data.txt')  
    # if f.name == 'data.txt':
    #     raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print('Executing the finally...')

# try:
#     pass
# except Exception:
#     pass
# else:
#     pass
# finally: 
#     pass