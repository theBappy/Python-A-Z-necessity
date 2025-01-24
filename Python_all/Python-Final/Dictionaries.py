# print(thisdict)
# print(thisdict["brand"])
# print(thisdict["year"])
# print(thisdict["model"])
# thisdict ={
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964,
#     "electric": False,
#     "color": ["red","green","blue"],
# }
# thisdict1 = dict(name="John", age=45, married=True)
# print(thisdict1)
# print(type(thisdict1))
# print(len(thisdict1))
# print(thisdict1["married"])
# print(thisdict1["age"])
# print(len(thisdict))
# print(type(thisdict))
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # print(thisdict["model"])
# # print(thisdict["year"])
# x = thisdict.get("year")
# print(x)
# y = thisdict.get("brand")
# z = thisdict.get("age")
# print(y, z)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.keys()
# y = thisdict.values()
# print(x)
# print(y)
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.keys()
# print(x)
# car["color"] = "white"
# print(x)
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.values()
# print(x)
# car["brand"]="Non-Ford"
# print(x)
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.values()
# print(x)
# car['color'] = 'red'
# print(x)
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.items()
# print(x)
# car["color"]="blue"
# print(x)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#     print("yes")
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year":2020, "color": "red"})
# print(thisdict)
# thisdict["year"] =2000
# print(thisdict)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = 'red'
# print(thisdict)
# thisdict.update({"origin":"hungary"})
# print(thisdict)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# thisdict.popitem()
# thisdict.popitem()
# thisdict.popitem()
# thisdict.popitem()
# print(thisdict)
# x=thisdict.pop("model")
# print(thisdict)
# print(x)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)
# thisdict.clear()
# print(thisdict)
# for x in thisdict:
#   print(x)
#   print(thisdict[x])
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict:
#     print(x)
#     print(thisdict[x])
# for y in thisdict:
#     print(y)
#     print(thisdict[y])
# for x in thisdict:
#     print(x)
#     print(thisdict[x])
# for x in thisdict.values():
#     print(x)
# for x in thisdict.keys():
#     print(x)
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for a, b in thisdict.items():
#     print(a,b)
# for key, value in thisdict.items():
#     print(key, value)
# for x, y in thisdict.items():
#     print(x,y)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict)
# copieddict = thisdict.copy()
# print(copieddict)
# myfamily ={
#     "child1": {
#         "name":"Emil",
#         "year": 2004,
#     },
#     "child2": {
#         "name": "John",
#         "year": 2005,
#     },
#     "child3": {
#         "name": "David",
#         "year": 2009,
#     },
# }
# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }
# myfamily ={
#     "child1": child1,
#     "child2": child2,
#     "child3": child3,
# }
# print(myfamily["child2"]["name"])
# print(myfamily["child2"]["year"])
# print(myfamily["child1"]["name"])
# print(myfamily["child1"]["year"])
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
# for x, obj in myfamily.items():
#     print(x)
    # for y in obj:
    #     print(y + ":" , obj[y])
# for x , obj in myfamily.items():
#     print(x)
#     for y in obj:
#         print(y+ ":" , obj[y])
# for x, obj in myfamily.items():
#     print(x)
#     for y in obj:
#         print(y + ":", obj[y])
