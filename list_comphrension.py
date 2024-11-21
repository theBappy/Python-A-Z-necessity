# nums = [1,2,3,4,5,6,7,8,9,10]



# my_list =[(letter,num) for letter in 'abcd' for num in range(4)]
# print(my_list)

# my_list = [(x,y) for x in 'abc' for y in range(3)]
# print(my_list)

# my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
# print(my_list)

# my_list =[]
# for letter in 'abcd':
#     for num in range(5):
#         my_list.append((letter,num))
# print(my_list)

# my_list =[]
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter,num))
# print(my_list)

# my_list =[]
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter,num))
# print(my_list)

# my_list =[]
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter,num))
# print(my_list)

# my_list =filter(lambda n: n%2 ==0 , nums)
# print(my_list)

# mylist =[n for n in nums if n%2==1]
# print(mylist)
# mylist =[n for n in nums if n%2==0]
# print(mylist)

# mylist =[]
# for n in nums:
#     if n%2 ==1:
#         mylist.append(n)
# print(mylist)

# my_list =[]
# for n in nums:
#     if n%2 == 0:
#         my_list.append(n)
# print(my_list)

# my_list =map(lambda n: n*n, nums)
# print(my_list)

# my_list = map(lambda n: n*n , nums)
# print(my_list)

# my_list =[n/n for n in nums]
# print(my_list)
# my_list1 = [n*n for n in nums]
# print(my_list1)
# my_list =[n*n for n in nums]
# print(my_list)

# my_list =[]
# for n in nums:
#     my_list.append(n*n)
# print(my_list)

# my_list =[]
# for n in nums:
#     my_list.append(n*n)
# print(my_list)



# my_list =[]
# for n in nums:
#     my_list.append(n)
# print(my_list)

# my_list1 = [n for n in nums]
# print(my_list1)

# my_list =[]
# for n in nums:
#     my_list.append(n)
# print(my_list)

# my_list1= [n for n in nums]
# print(my_list)

# my_list = []
# for n in nums: 
#     my_list.append(n)
# print(my_list)
# my_list =[]
# for n in nums:
#     my_list.append(n)
# print(my_list)

# names =['bruce', 'clark', 'peter', 'logan', 'wade']
# heros = ['batman', 'superman', 'spiderman', 'wolverin', 'deadpool']

# my_dict ={name: hero for name, hero in zip(names,heros) if name != 'logan'}
# print(my_dict)


# my_dict={name: hero for name, hero in zip(names,heros) if name != 'peter'}
# print(my_dict)

# my_dict ={name: hero for name, hero in zip(names,heros)}
# print(my_dict)
# my_dict={name: hero for name, hero in zip(names, heros)}
# print(my_dict)


# my_dict ={name: hero for name, hero in zip(names,heros)}
# print(my_dict)

# my_dict ={}
# for name, hero in zip(names,heros):
#     my_dict[name] = hero
# print(my_dict)


# my_dict ={}
# for name, hero in zip(names,heros):
#     my_dict[name] = hero
# print(my_dict)


# my_dict ={}
# for name,hero in zip(names, heros):
#     my_dict[name]=hero
# print(my_dict)


# my_dict ={}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
# print(my_dict)



# x = zip(names, heros)
# print(list(x))
# x= zip(names, heros)
# print(tuple(x))
# x = zip(names, heros)
# print(list(x))


# nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,8,7,9,9]

#  Generator Expressions
# my_gen =(n/n for n in nums)
# for i in my_gen:
#     print(i)
# my_gen =(n*n for n in nums)
# for i in my_gen:
#     print(i)
# my_gen =(n*n for n in nums)
# for i in my_gen:
#     print(i)
# def gen_func(nums):
#     for n in nums:
#         yield n * n
# my_gen = gen_func(nums)
# for i in my_gen:
#     print(i)

# def gen_func(nums):
#     for n in nums:
#         yield n*n
# my_gen = gen_func(nums)
# for i in my_gen:
#     print(i)

# def gen_func(nums):
#     for n in nums:
#         yield n*n
# my_gen =gen_func(nums)
# for i in my_gen:
#     print(i)



# def gen_func(nums):
#     for n in nums:
#         yield n*n
# my_gen = gen_func(nums)
# for i in my_gen:
#     print(i) 

# my_set ={n for n in nums}
# print(my_set)

# my_set = {n for n in nums}
# print(my_set)

# my_set = {n for n in nums}
# print(my_set)

# my_set = {n for n in nums}
# print(my_set)

# my_set = set()
# for n in nums: 
#     my_set.add(n)
# print(my_set)

# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)

# my_set = set()
# for n in nums: 
#     my_set.add(n)
# print(my_set)

# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)

# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)