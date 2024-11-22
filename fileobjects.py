# File objects

# f = open('Python/test.txt', 'r')
# print(f.mode)
# f.close()

# f = open('Python/test.txt', 'r')
# print(f.name)
# print(f.mode)
# f.close()

# f = open('Python/test.txt', 'r')
# print(f.name)
# print(f.mode)
# f.close()

# with open('Python/test.txt', 'r') as f:
#     f_contents = f.read()
#     print(f_contents)

# with open('Python/test.txt', 'r') as f:
#     f_contents = f.read()
#     print(f_contents)

# with open('Python/test.txt', 'r') as f:
#     f_contents = f.readline()
#     print(f_contents, end='')

#     f_contents = f.readline()
#     print(f_contents)

   # f_contents = f.readline()
    # print(f_contents, end='')

    # f_contents = f.readline()
    # print(f_contents)
#   for line in f:
#         print(line,end='')
        

# with open('Python/test.txt', 'r') as f:
#     size_to_read =10

#     f_contents = f.read(size_to_read)
#     print(f_contents, end='')

#     f.seek(0)

#     f_contents = f.read(size_to_read)
#     print(f_contents)

    # print(f.tell())


    # while len(f_contents) > 0:
    #     print(f_contents, end='*')
    #     f_contents = f.read(size_to_read)

# with open('Python/test3.txt', 'w') as f:
#     f.write('test')
#     f.seek(0)
#     f.write('r')

# with open('Python/test.txt', 'r') as rf:
#     with open('Python/test_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

# with open('Python/png.png' , 'rb') as rf:
#     with open('Python/png_copy.png', 'wb') as wf:
#         for line in rf:
#             wf.write(line)

# with open('Python/png.png', 'rb') as rf:
#     with open('Python/png1.png', 'wb') as wf:
#             chunk_size = 4096
#             rf_chunk = rf.read(chunk_size)
#             while len(rf_chunk) > 0:
#                   wf.write(rf_chunk)
#                   rf_chunk = rf.read(chunk_size)

# f = open('Python/test.txt', 'rt')
# print(f.read())

# f = open('Python/test.txt', 'rt')
# print(f.read())

# f = open('Python/test.txt', 'r')
# print(f.read())

# f = open('Python/test.txt', 'r')
# print(f.read(5))

# f = open('Python/test.txt', 'r')
# print(f.readline())

# f = open('Python/test.txt', 'r')
# print(f.readline(), end='')
# print(f.readline())

# f = open('Python/test.txt', 'r')
# for x in f:
#     print(x, end='*')

# f = open('Python/test.txt', 'r')
# print(f.readline())
# f.close()

# f = open('Python/test2.txt', 'w')
# f.write('Now the file has less content')
# f.close()

# f = open('Python/test2.txt', 'w')
# f.write('Woops! I have overwrite the content')
# f.close()

# f = open('Python/test2.txt', 'r')
# print(f.read())

# f = open('Python/crete.txt', 'x')

# import os
# os.remove('Python/test2.txt')

# import os
# if os.path.exists('test.txt'):
#     os.remove('test.txt')
# else:
#     print('the file does not exist')


# import os 
# os.rmdir('delete')









   
  
 

   
