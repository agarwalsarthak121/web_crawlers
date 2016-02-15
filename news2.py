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
        li = ['india-news','world-news','sports','movies']
        k = random.randint(0,3)
        sc = requests.get('http://www.abplive.in/'+li[k])
        soup = BeautifulSoup(sc.text,'lxml')
        head = soup.select('h1 > a')
        basic = soup.select('h5 > a')
        news = head + basic
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

