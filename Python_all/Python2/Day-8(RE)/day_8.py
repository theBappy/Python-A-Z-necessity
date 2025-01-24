# Regular Expression

import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234


Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

'''

sentence = 'Start a sentence and then bring it to an end'
sentence1 = 'Quick brown fox jumps over the lazy dog'


# pattern = re.compile(r'start' , re.I)
pattern = re.compile(r'start', re.IGNORECASE)

matches = pattern.search(sentence)

print(matches)


# for match in matches:
#     print(match)

# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

# matches = pattern.findall(text_to_search)

# for match in matches:
#     print(match)

# with open('/Users/User/Desktop/Python (Phitron-FB)/Python2/data.txt', 'r') as f:
#     contents = f.read()

#     matches = pattern.finditer(contents)

#     for match in matches:
#         print(match)

# pattern = re.compile(r'.')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

# pattern = re.compile(r'abc')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

# print(text_to_search[1:4])






