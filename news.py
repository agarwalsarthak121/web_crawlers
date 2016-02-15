#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import datetime
from bs4 import BeautifulSoup
import random
from time import sleep
import pynotify

while True:
    try:
        sc = requests.get('http://www.rediff.com/news/headlines')
        soup = BeautifulSoup(sc.text,'lxml')
        news = soup.select('p > a')    
        while True:
            i = random.randrange(0,len(news)-1)
            j = random.randrange(0,len(news)-1)
            if i == j:
                continue
            else:
                pynotify.init('test')
                n = pynotify.Notification('Live News','* '+news[i].text+'\n'+'* '+news[j].text)
                n.show()
                break             
    except requests.exceptions.ConnectionError:
        pynotify.init('test')
        n = pynotify.Notification('Connection Issue','No internet found')
        n.show()
    sleep(90)

