import requests
import bs4
import lxml

res = requests.get('https://www.example.com')

# read from res with lxml to create soup, which can be analyzed
soup = bs4.BeautifulSoup(res.text, 'lxml')
print(soup.select('title'))

# Print out title of example.com
title_tag_list = soup.select('title')
print(title_tag_list[0].getText())

res = requests.get('https://en.wikipedia.org/wiki/Room_641A')
soup = bs4.BeautifulSoup(res.text, 'lxml')

# Grab element h1 and print out
h1_list = soup.select('h1')
print(h1_list[0].getText())

for item in soup.select('.mw-headline'):
    print(item.text)


# web scrape images
# if I want a specific image -> cannot use <img> tag
res = requests.get('https://en.wikipedia.org/wiki/Cicada_3301')
soup = bs4.BeautifulSoup(res.text, 'lxml')

image_info = soup.select('.thumbimage')

# grab object from that list and make dic
cicada = image_info[0]
print(cicada['src'])

# create an image link to get img
image_link = 'http:'+cicada['src']

cicada_image = requests.get(image_link, 'lxml')
# will give back 200 if ok
print(cicada_image)

# open new file and write img to it (in curr folder)
f = open('cicada_image_new.jpg', 'wb')
f.write(cicada_image.content)
f.close()
