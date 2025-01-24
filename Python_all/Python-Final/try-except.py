try:
    f = open('/Users/User/Desktop/Python (Phitron-FB)/Python-Final/text.txt')
    if f.name == 'text.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('executing the finally...')