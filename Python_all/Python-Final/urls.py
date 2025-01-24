import re

urls = '''
https://www.google.com
http://coreyms.com
http://thebappy.in
https://youtube.com
https://www.nasa.gov
'''
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# Back-references
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)

# matches =  pattern.finditer(urls)



# for match in matches:
    # print(match)
    # print(match.group(3))
