from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()


# from bs4 import BeautifulSoup
# import requests


# source = requests.get('http://coreyms.com').text
# soup = BeautifulSoup(source, 'lxml')
# for article in soup.find_all('article'):


#     vid_src = article.find('iframe', class_='youtube-player')['src']
#     # print(vid_src)

#     vid_id = vid_src.split('/')[4]
#     vid_id = vid_id.split('?')[0]
#     # print(vid_id)

#     yt_link = f'https://youtube.com/watch?v={vid_id}'
#     # print(yt_link)


#     # print(article.prettify())


#     summary = article.find('div', class_='entry-content').p.text
#     print(summary.prettify())
#     headline = article.h2.a.text
#     # print(headline)


# soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())
# article = soup.find('panels')
# print(article.prettify())


# with open('/Users/User/Desktop/Python (Phitron-FB)/Python Pblm/simple.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')


# for article in soup.find_all('div', class_='article'):
#     headline = article.h2.a.text
#     print(headline)
#     summary = article.p.text
#     print(summary)

#     print()


# print(match)
# match = soup.find('div', class_='footer')
# print(match)
# match = soup.title.text
# print(match)
# print(soup)
# print(soup.prettify())
# print(soup.prettify())
# match = soup.title
# print(match.text)