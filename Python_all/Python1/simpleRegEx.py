import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

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

pattern = re.compile(r'start', re.I)
matches = pattern.search(sentence)
print(matches)
# for match in matches:
#     print(match)



# with open('data.txt', 'r') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)

#     for match in matches:
#         print(match)


# with open('data.txt','r') as f: 
#     contents = f.read()
#     mathces = pattern.finditer(contents)
#     for match in mathces:
#         print(match)

# patter = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# pattern = re.compile(r'\BHa')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)



# pattern = re.compile(r'coreyms\.com')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)



# patter = re.compile(r'xyz')
# matches = patter.finditer(text_to_search)
# for match in matches:
#     print(match)



# pattern = re.compile(r'abc')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)




# pattern = re.compile(r'abc')
# matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)
# print(text_to_search[1:4])



# print('\tTab')
# print(r'\tTab')

