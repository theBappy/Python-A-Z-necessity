import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] | ( )

thebappy.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234


Mr. Bappy
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

'''

sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

pattern = re.compile(r'start', re.I)

matches = pattern.search(sentence)

print(matches)

# for match in matches:
#     print(match)

# with open('/Users/User/Desktop/Python (Phitron-FB)/Python-Final/data111.txt', 'r', encoding='UTF-8') as f:
#     contents = f.read()

#     matches = pattern.finditer(contents)

#     for match in matches:
#         print(match)


# print(text_to_search[221:222])

# print(text_to_search[1:4])

