# import os
# print(os.path.dirname(os.path.realpath(__file__)))
import camelcase
c = camelcase.CamelCase()
txt = 'hello'
print(c.hump(txt))