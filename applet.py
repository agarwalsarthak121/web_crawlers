#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import appindicator
import pynotify
import gtk
import random

a = appindicator.Indicator('tubecheck','/usr/share/pixmaps/debian-logo.png', appindicator.CATEGORY_APPLICATION_STATUS)
a.set_label('England19 vs Pakistan19')
a.set_status( appindicator.STATUS_ACTIVE )
m = gtk.Menu()
one = gtk.MenuItem('News')
two = gtk.MenuItem('Live score')
three = gtk.MenuItem('Quote of the day')
four = gtk.MenuItem('Word of the day')
qi = gtk.MenuItem('Quit')
m.append(one)
m.append(two)
m.append(three)
m.append(four)
m.append(qi)

a.set_menu(m)
one.show()
two.show()
three.show()
four.show()
qi.show()

def quoteshow(item):
    fw = open('quotes.txt','r')
    vocab = fw.read()
    vocab = vocab.split('\n')
    while True:
        i = random.randint(0,2002)
        if i % 2 == 0:
            if len(vocab[i]) < 118:
                pynotify.init("Test")
                notice = pynotify.Notification(vocab[i],vocab[i+1])
                notice.show()
                break
            else:
                continue
        else:
            continue

def wordshow(item):
    fw = open('vocab.txt','r')
    vocab = fw.read()
    vocab = vocab.split('\n')
    while True:
        i = random.randint(0,len(vocab)-1)
        if i % 2 == 0:
            pynotify.init("Test")
            notice = pynotify.Notification(vocab[i],vocab[i+1])
            notice.show()
            break
        else:
            continue

def livescore(item):
    try:
        sc = requests.get('http://static.cricinfo.com/rss/livescores.xml')
        soup = BeautifulSoup(sc.text,'lxml')
        matches = soup.findAll('item')
        inp = 11
        url = matches[inp - 1].find('guid').text
        sc = requests.get(url)
        soup = BeautifulSoup(sc.text,'lxml')
        team1 = soup.findAll('div',{'class':'team-1-name'})          
        score = soup.findAll('title')
        pynotify.init('test')
        n = pynotify.Notification('Live Score',score[0].text) 
        n.show()
    except requests.exceptions.ConnectionError:
        pynotify.init('test')
        n = pynotify.Notification('Connection Issue','No internet found')
        n.show()

def newsshow(item):
    try:
        sc = requests.get('http://www.ndtv.com/topic/top-10/news')
        soup = BeautifulSoup(sc.text,'lxml')
        news = soup.select('a strong')    
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


one.connect('activate',newsshow)
two.connect('activate',livescore)
three.connect('activate',quoteshow)
four.connect('activate',wordshow)

def quit(item):
	gtk.main_quit()

qi.connect('activate', quit)

gtk.main()
