import json
x ={
    "name": "John",
    "age": 23,
    "married": False,
    "isRich": True,
    "children": ('Anna', 'Jenn'),
    "pets": None,
    "cars": [
        {
            "model": "BMW", "mpg": 27.5,
        },
        {
            "model": "Ford", "mpg": 24.5,
        }
    ]
}
print(json.dumps(x, indent=4, separators=(". ", "= "), sort_keys=True))



# import json

# print(json.dumps({"name": "john", "age": 23}))
# print(json.dumps(['apple', 'cherry']))
# print(json.dumps(('apple', 'banana')))
# print(json.dumps('hello'))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))
# print(json.dumps(34.34))
# print(json.dumps(42))
# print(json.dumps(-79))


# import json

# x = {
#     "name": "John", 
#     "age": 23, 
#     "city": "New York"
# }

# y = json.dumps(x)
# print(y)


# data = '{"name":"John", "age":23, "city":"New York"}'
# y = json.loads(data)
# print(y["city"])

# x = '{ "name":"John", "age":30, "city":"New York"}'

# y = json.loads(x)

# print(y["age"])
