#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
from time import sleep

print ('Live Cricket news:')
print ('='*len('Live Cricket news:'))
url = "http://www.espncricinfo.com/rss/content/story/feeds/6.xml"
sc = requests.get(url)
soup = BeautifulSoup(sc.text,'lxml')

for i in range(5):
    news = soup.findAll('item')
    title = news[i].find('title')
    description = news[i].find('description')
    print ('* '+title.text)
    print ('=> '+description.text)
    print ()
