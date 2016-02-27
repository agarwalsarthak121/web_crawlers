#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import pynotify
from time import sleep
import sys

def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return

print 'Live Cricket Matches:'
print '='*len('Live Cricket Matches:')
url = "http://static.cricinfo.com/rss/livescores.xml"
sc = requests.get(url)
soup = BeautifulSoup(sc.text,'lxml')

i = 1
for data in soup.findAll('item'):
    print str(i)+'. '+data.find('description').text
    i += 1

list_links = []    
for link in soup.findAll('item'):
    list_links.append(link.find('guid').text)

print 'Enter match no. or enter 0 to exit:'
while True:
    try:
        user_input = int(input())
    except NameError:
        print 'Enter correct input'
        continue
    except SyntaxError:
        print 'Enter correct input'
    if user_input < 0 or user_input > 30:
        print 'Enter correct input'
        continue
    elif user_input == 0:
        sys.exit()      
    else:
        break
url = list_links[user_input - 1]
sc = requests.get(url)
soup = BeautifulSoup(sc.text,'lxml')  

while True:
    url = list_links[user_input - 1]
    sc = requests.get(url)
    soup = BeautifulSoup(sc.text,'lxml') 
    score = soup.findAll('title')       
    try:
        sc.raise_for_status()
    except Exception as exc:
        print ('Connection Issue')
        continue    
    sendmessage('Live Score',score[0].text)
    sleep (30)
    

