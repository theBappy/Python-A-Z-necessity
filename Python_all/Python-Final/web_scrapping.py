from bs4 import BeautifulSoup
import csv

# Load the HTML file
with open('/Users/User/Desktop/Python (Phitron-FB)/blackbox.html') as data_file:
    soup = BeautifulSoup(data_file, 'lxml')

# Open the CSV file using a context manager
with open('/Users/User/Desktop/Python (Phitron-FB)/cms_scrap1.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Summary', 'Video_link'])

    # Find all summaries and video links
    summaries = [summary.text for summary in soup.find_all('p')]
    video_links = []

    for iframe in soup.find_all('iframe'):
        try:
            vid_src = iframe['src']
            vid_id = vid_src.split('/')[4]
            yt_link = f'https://youtube.com/watch?v={vid_id}'
            video_links.append(yt_link)
        except Exception as e:
            video_links.append(None)

    # Write to CSV
    for summary, yt_link in zip(summaries, video_links):
        csv_writer.writerow([summary, yt_link])

print("CSV file has been created successfully.")



# vid_src = soup.find('iframe', class_="yotube-player")['src']

# vid_id = vid_src.split('/')[4]

# yt_link = f'https://youtube.com/watch?v={vid_id}'
# print(yt_link)

# for summary in soup.find_all('p'):
#     headline = summary.text
#     print(headline)


# source = requests.get('https://www.thedesignmastery.com/').text
 
# soup = BeautifulSoup(source, 'lxml')

# # print(soup.prettify())

# article = soup.find('div', class_='uui-layout01_image-wrapper _2 _3')
# print(article.prettify())

# from bs4 import BeautifulSoup
# import requests

# with open('/Users/User/Desktop/Python (Phitron-FB)/simple.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')

# for article in soup.find_all('div', class_='article'):
#     headline = article.h2.a.text
#     print(headline)

#     summary = article.p.text
#     print(summary)

#     print()

# article = soup.find('div', class_='article')
# print(article)

# headline = article.h2.a.text
# print(headline)

# summary = article.p.text
# print(summary)


# paragraph = article.p.text
# print(paragraph)

# headline = article.h2.a.text
# print(headline)

# match = soup.find('div')
# print(match)


# match = soup.find('div', class_='footer')
# print(match)

# match =soup.find('div', class_='footer')
# print(match)

# match = soup.find('div', class_='footer')
# print(match)

# match = soup.div
# print(match)

# match = soup.title.text
# print(match)

# match = soup.title
# print(match.text)

# print(soup.prettify())