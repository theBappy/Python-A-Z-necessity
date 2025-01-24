# thislist = ["apple", "banaba", "cherry", 5, True]
# print(thislist)
# print(len(thislist))
# print(type(thislist[4]))
# print(type(thislist[3]))
# print(type(thislist))
# thislist = list(("apple", "cherry", "banana"))
# print(thislist)
# thislist = ["apple", "banana", "cherry", 5, True]
# print(thislist[1])
# print(thislist[0])
# print(thislist[-1])
# print(thislist[-2])
# print(thislist[-5])
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])
# print(thislist[2:])
# print(thislist[:3])
# print(thislist[:4])
# print(thislist[1:])
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])
# print("apple" in thislist)
# thislist = ["apple", "banana", "cherry"]
# thislist[1] ="mango"
# print(thislist)
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:2] =["jack-fruit", "coffee"]
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] =["blackcurrant", "watermelon"]
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# thislist[1:3]=["watermelon"]
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# thislist.insert(1, "jackfruit")
# thislist.insert(4, "coffee")
# thislist.insert(5, True)
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# thislist.append("watermelon")
# thislist.append("coffee")
# thislist.append("chocolate")
# thislist.append("strawberry")
# thislist.append(True)
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(0, "coffee")
# print(thislist)
# thislist.insert(0, "chocolate")
# print(thislist)
# thislist.insert(1, "black")
# print(thislist)
# thislist1 = ["apple", "cherry", "mango"]
# thislist2 =["coffee", "chocolate", "car"]
# thislist1.extend(thislist2)
# print(thislist1)
# thislist2.extend(thislist1)
# print(thislist2)
# thislist2.append(thislist1)
# print(thislist2)
# print(thislist2[9])
# thislist =["apple","cherry","mango"]
# tuple1 = ("black", "white")
# thislist.extend(tuple1)
# print(thislist)
# thislist  =["apple", "banana", "cherry", "mango", "black","coffee", "jackfruit"]
# thislist.remove("banana")
# print(thislist)
# thislist.remove("cherry")
# print(thislist)
# thislist.remove("apple")
# print(thislist)
# thislist.remove("mango")
# print(thislist)
# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)
# thislist =["apple", "cherry", "mango","banana", "coffee", "chocolate"]
# thislist.pop(1)
# print(thislist)
# thislist.pop(0)
# print(thislist)
# thislist.pop(1)
# print(thislist)
# thislist.pop(2)
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# a=thislist.pop()
# print(a)
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)
# del thislist[0]
# print(thislist)
# del thislist
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#     print(x)
# thislist = ["apple[", "banana", "cherry"]
# for i in range(len(thislist)):
#     print(thislist[i])
# thislist = [ "apple", "banana", "cherry"]
# for i in range(len(thislist)):
#     print(thislist[i])
# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i += 1
# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i += 1
# thislist = ["apple", "banana", "cherry"]
# [print(y) for y in thislist]
# [print(z) for z in thislist]
# [print(x) for x in thislist]
# thislist =["apple", "cherry", "mango", "banana"]
# [print(x) for x in thislist]
# [print(y) for y in thislist]
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist =[]
# newlist =[ x for x in fruits if "a" in x]
# print(newlist)
# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)
# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist =[x for x in fruits if "p" in x]
# print(newlist)
# newlist =[ x for x in fruits if "o" in x]
# print(newlist)
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist =[x for x in fruits if x != "apple"]
# print(newlist)
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist =[ x for x in fruits]
# newlist1= [x for x in range(10)]
# print(newlist)
# print(newlist1)
# alist =[x for x in range([1:19])]
# print(alist)
# newlist =[x for x in range(10) if x < 5]
# print(newlist)
# newlist =[x.upper() for x in fruits]
# print(newlist)
# newlist =["hello" for x in fruits]
# print(newlist)
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist =[ x if x != "banana" else "orange" for x in fruits]
# print(newlist)
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x if  x != "banana" else "jackfruit" for x in fruits]
# print(newlist)
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thisnumlist =[100,50,45,67,22]
# thisnumlist.sort(reverse=True)
# print(thisnumlist)
# thislist.sort()
# print(thislist)
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse=True)
# print(thislist)
# thislist1 = [100, 50, 65, 82, 23]
# thislist1.sort(reverse=True)
# print(thislist1)
# def myFunc(n):
#     return abs(n - 50)
# thislist =[100,50,77,33,12]
# thislist.sort(key=myFunc)
# print(thislist)
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)
# thislist.sort(key=str.lower)
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# mylist = thislist.copy()
# mylist = thislist.copy()
# mylist = thislist.copy()
# mylist = thislist.copy()
# mylist = thislist.copy()
# mylist = thislist.copy()
# print(mylist)
# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)
# mylist1 = list(mylist)
# print(mylist1)
# mylist2 = list(thislist)
# print(mylist2)
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist[:]
# mylist = thislist[:]
# mylist = thislist[:]
# mylist = thislist[:]
# mlist =thislist[:]
# print(mlist)
# mylist = thislist[:]
# print(mylist)
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1+list2
# print(list3)
# for x in list2:
#     list1.append(x)
# print(list1)
# for x in list1:
#     list2.append(x)
# print(list2)
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# list2.extend(list1)
# print(list2)