


# import urllib.request

# url = 'https://www.exmaple.com'

# try:
#     response = urllib.request.urlopen(url)
#     data = response.read()
#     html_content = data.decode('utf-8')

#     print(html_content)

# except Exception as e:
#     print('Error fetching url: ', e)



# from lxml import html
# import requests

# url = 'https://daraz.com'

# response = requests.get(url)

# tree = html.fromstring(response.content)

# link_titles = tree.xpath('//a/text()')

# for title in link_titles:
#     print(title)




# from selenium import webdriver

# from selenium.webdriver.common.by
# import by
# from webdriver_manager.chrome import ChromeDriveManager

# element_list =[]

# for page in range(1,3,1):
#     page_url = "https://webscrapper.io/test-sites/e-commerce/static/computers/laptops?page=" + str(page) 

#     driver = webdriver.Chrome(ChromeDriveManager().install())

#     driver.get(page_url)
#     title = driver.find_elements(By.CLASS_NAME, 'title')
#     price = driver.find_elements(By.CLASS_NAME, 'price')
#     description = driver.find_elements(By.CLASS_NAME, 'description')
#     rating = driver.find_elements(By.CLASS_NAME, 'rating')

#     for i in range(len(title)):
#         element_list.append([title[i].text, price[i].text, description[i].text, rating[i].text])

#     print(element_list)

# driver.close()
# #import webriver
# from selenium import webdriver

# driver = webdriver.Firefox()

# driver.get('https://google.co.in/search?q=geeksforgeeks')





# from bs4 import BeautifulSoup
# import requests

# r = requests.get('https://www.geeksforgeeks.org/python-programming-language')

# soup  = BeautifulSoup(r.content, 'html.parser')

# s = soup.find('h2', id='first-python-program-to-learn-python-programming')

# leftbar = s.find_all('span')


# for line in leftbar:
#     print(line.text)

# soup = BeautifulSoup(r.content, 'html.parser')
# s = soup.find('div', class_='text')
# lines = s.find_all('p')
# for line in lines:
#     print(line.text)

# soup = BeautifulSoup(r.content, 'html.parser')
# s = soup.find('div', id='main')
# leftbar = s.find('ul', class_='three_dot_dropdown_content')
# content = leftbar.find_all('li')
# print(content)

# soup  = BeautifulSoup(r.content , 'html.parser')
# s = soup.find('div', id='main')
# print(s.prettify())
# s = soup.find('div', class_='text')
# lines = s.find_all('p')
# print(lines)

# print(r)
# soup = BeautifulSoup(r.content, 'html.parser')
# s = soup.find('div', class_='text')
# print(s)
# print(soup.title.text)
# print(soup.title.name)
# print(soup.title.parent.name)
