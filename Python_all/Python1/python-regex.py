# import re
# txt = 'The rain in Spain'
# x = re.search('^The.*Spanin$', txt)
# print(x)
# import re
# txt = 'The rain in Spain'
# x = re.search('^The.*Spain$', txt)
# if x: 
#     print('Yes, we found the match')
# else:
#     print('No match')
# [] A set of characters "[a-m]"
# import re
# txt = 'The rain in Spain'
# x = re.findall("[a-m]", txt)
# print(x)
# import re
# txt = 'That will be 59 dollars'
# x = re.findall("\d", txt)
# print(x)
# import re
# txt = 'hello planet'
# x =re.findall("he..o", txt)
# print(x)
# import re
# txt = 'hello planet'
# x = re.search('^hello', txt)
# if x:
#     print('match')
# else:
#     print('no mtach')
# import re
# txt = 'hello planet'
# x = re.findall('planet$', txt)
# if x: 
#     print('match')
# else:
#     print('no match')
# import re
# txt = 'the rain in spain falls mainly in the plain'
# x = re.search('falls|stays', txt)
# print(x)
# if x: 
#     print('yes')
# else: 
#     print('no')
# x = re.findall("he.{2}o", txt)
# print(x)
# x = re.findall('he.{2}.o', txt)
# print(x)
# x = re.findall('he.?o', txt)
# print(x)
# x = re.findall('he.+o', txt)
# print(x)
# x = re.findall('he.*o', txt)
# print(x)
# import re
# txt = 'the rain in spain'
# x = re.findall('norway',txt)
# print(x)
# import re
# txt = 'the rain in spain'
# x = re.search('\s', txt)
# print('the first white-space character is located in position: ', x.start())
# import re
# txt = 'the rain in spain'
# x = re.search('portugal', txt)
# print(x)
# import re
# txt = 'the rain in spain'
# x = re.split('\s', txt)
# print(x)
# import re 
# txt = 'the rain in spain'
# x = re.split('\s', txt ,4)
# print(x)
# import re 
# txt = 'the rain in spain'
# x = re.sub('\s', '9', txt)
# print(x)
# import re 
# txt = 'the rain in spain'
# x = re.sub('\s', '9', txt, 2)
# print(x)
# import re 
# txt = 'the rain in spain'
# x = re.search('ai', txt)
# print(x)
# import re 
# txt = 'the rain in spain'
# x = re.search(r'\bs\w+' , txt)
# print(x.span())
# import re 
# txt = 'the rain in spain'
# x = re.search(r'\bs\w+', txt)
# print(x.string)
# import re

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.group())