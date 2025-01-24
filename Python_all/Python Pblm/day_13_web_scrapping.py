from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.daraz.com.bd/?laz_trackid=2:mm_153492401_426025736_4181025236:clkgg5r031ievqv5dlbcus&mkttid=clkgg5r031ievqv5dlbcus#?').text
soup= BeautifulSoup(source, 'lxml')

# csv_file = open('cms_scrapping.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['headline', 'summary', 'video_link'])

csv_file = open('cms_scrapping.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Summary', 'Video_Link'])




for article in soup.find('div', class_='picture-wrapper common-img'):
    try:
        img_src = article.find('img')['src']


        img_id = img_src.split('/')[5]
        img_id = img_id.split('-')[4]
        print(img_id)

        img_link = f'https://daraz.com/image?v={img_id}'
      

        print()
    except Exception as e:
        yt_link = None
    
    print(img_link)

    print()

    csv_writer.writerow(['headline', 'summary', 'vidoe_link'])
csv_file.close()

#     csv_writer.writerow(['headline', 'summary', 'video_link'])

# csv_file.close()



# vid_id = img_src.split('/')[4]
# vid_id = vid_id.split('?')[0]
# print(vid_id)



# summary = article.p
# print(summary.text)


# headline = soup.find('h1').text
# print(headline)

# article = soup.find('p').text
# print(article)


# print(soup.prettify())
# for match in soup.find('h1').text:
#     print(match)



# with open('/Users/User/Desktop/Python (Phitron-FB)/Python Pblm/simple.html') as new_file:
#     soup = BeautifulSoup(new_file, 'lxml')


# for article in soup.find_all('div', class_='article'):
#     headline = article.h2.a.text
#     print(headline)

#     summary = article.p.text
#     print(summary)

#     print()



# print(article2)
# headline = article2.h2.a.text
# print(headline)
# summary = article2.p.text
# print(summary)


# footer = soup.find('div', class_='footer')
# print(footer)
# paragraph = footer.p.text
# print(paragraph)

# article = soup.find('div', class_='article')
# print(article)
# headline = article.h2.a.text
# print(headline)
# summary= article.p.text
# print(summary)

# match = soup.find('div', class_='footer')
# print(match)

# match = soup.find('p', class_='paragraph').text
# print(match)
# match = soup.div
# print(match)
# match = soup.title.text
# print(match)   
# print(soup.prettify())
# match = soup.title.text
# print(match)
# match1 = soup.body.h1.text
# print(match1)
# match2 = soup.body.h2.text
# print(match2)
# match3= soup.body.p.text
# print(match3)
# match = soup.title
# print(match)
# print(soup.prettify())
# with open('/Users/User/Desktop/Python (Phitron-FB)/Python Pblm/simple.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify())
