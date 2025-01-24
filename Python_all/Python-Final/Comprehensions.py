nums = [1,2,3,4,5,6,7,8,9,10]
names =['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes =['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
my_set = [1,1,2,2,3,3,4,5,6,7,7,8,9,10,10]

# def gen_func(nums):
#     for n in nums:
#         yield n * n

# my_gen = gen_func(nums)

my_gen = (n*n for n in nums)
for i in my_gen:
    print(i)

# myset = {n for n in my_set}
# print(myset)


# my_set= set()
# for n in nums:
#     my_set.add(n)
# print(my_set)


# mydict = {name:hero for name, hero in zip(names,heroes) if name!='Peter'}
# print(mydict)

# mydict = {name: hero for name,hero in zip(names,heroes)}
# print(mydict)

# mydict = {x:u for x, u in zip(names, heroes)}
# print(mydict)


# mydict ={}
# for name, hero in zip(names, heroes):
#     mydict[name] = hero
# print(mydict)


# mydict ={}
# for name, hero in zip(names, heroes):
#     mydict[name]=hero
# print(mydict)
# mydict ={}
# for name, hero in zip(names, heroes):
#     mydict[name]= hero
# print(mydict)
# mydict = {}
# for name, hero in zip(names, heroes):
#     mydict[name]=hero
# print(mydict)

# a=zip(names, heroes)
# print(a)

# mylist =[(letter, num) for letter in 'abcd' for num in range(4)]
# print(mylist)

# mylist =[]
# for letter in 'abcd':
#     for num in range(4):
#         mylist.append(letter, num)
# print(mylist)

# mylist =[]
# for letter in 'abcd':
#     for num in range(4):
#         mylist.append(letter, num)
# print(mylist)

# mylist = filter(lambda n: n % 2 ==0, nums)
# print(mylist)

# mylist = [n for n in nums if n % 2 == 1]
# print(mylist)

# mylist = [n for n in nums if n%2==0]
# print(mylist)

# mylist = []
# for n in nums:
#     if n % 2 == 1:
#         mylist.append(n)
# print(mylist)


# mylist =[]
# for n in nums:
#     if n % 2 == 0:
#         mylist.append(n)
# print(mylist)

# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

# my_list = [n for n in nums]
# print(my_list)

# my_list =[]
# for n in nums:
#     my_list.append(n*n)
# print(my_list)

# my_list =[n*n for n in nums]
# print(my_list)

# my_list = map(lambda n: n*n, nums)
# print(my_list)