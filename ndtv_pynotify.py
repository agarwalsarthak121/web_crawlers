#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import datetime
from bs4 import BeautifulSoup
import random
from time import sleep
import pynotify

def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return

sock=requests.get("http://www.ndtv.com/top-stories")
htmlSrc=sock.text
soup=BeautifulSoup(htmlSrc,'lxml')
'''print ("NDTV News\n")
today = datetime.date.today()
print (today.strftime('Today\'s date %d, %b %Y'))
print ()'''

while True:
    div = soup.findAll('div',{'class':'nstory_header'})
    i = random.randrange(0,len(div)-1)
    sendmessage('Live News',div[i].text)
    sleep (15)
    


