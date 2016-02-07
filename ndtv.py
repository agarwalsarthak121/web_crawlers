#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import datetime
from bs4 import BeautifulSoup


#proxies = {'http':'http://172.21.48.1:8080/'}
#sock = urllib.urlopen('http://www.thehindu.com/', proxies=proxies).read()

sock=requests.get("http://www.ndtv.com/top-stories")
htmlSrc=sock.text
soup=BeautifulSoup(htmlSrc,'lxml')
print ("NDTV News\n")
today = datetime.date.today()
print (today.strftime('Today\'s date %d, %b %Y'))
print ()

for div in soup.findAll('div',{'class':'nstory_header'}):
    print ('* '+div.find('a').text.lstrip())
    print ()


