# number = 1 + 2 * 3 / 4.0
# print(number)
# remainder = 11 % 3
# print(remainder)
# remainder = 34 % 7
# print(remainder)
# squared = 9 ** 2
# cubed = 9 ** 3
# print(squared)
# print(cubed)
# helloworld = 'hello' + ' ' +'world'
# print(helloworld)
# lotsofhellos= 'hello ' * 10
# print(lotsofhellos)
# even_numbers = [2,4,6,8]
# odd_numbers = [1,3,5,7]
# all_numbers = even_numbers + odd_numbers
# print(all_numbers)
# print([1,2,3] * 5)
x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list =x_list + y_list

print('x_list contains %d objects' % len(x_list))
print('y_list contains %d' % len(y_list))
print('big_list contains %d' % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print('almost there...')
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print('Great')