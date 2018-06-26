#!/usr/bin/env python3

from win10toast import ToastNotifier
import requests
import datetime
import os
from bs4 import BeautifulSoup
from time import sleep
import ctypes

while True:
    dt = datetime.datetime.now()
    cd = str(dt.year)+'0'+str(dt.month)+str(dt.day)
    if(dt.hour == 12 and dt.minute < 30):
        url = "https://bingwallpaper.com/"
        sc = requests.get(url)
        soup = BeautifulSoup(sc.text,'lxml')
        os.makedirs('Bing',exist_ok=True)
        ul = soup.find('ul',{'class':'filmstrip'})

        li = ul.findAll('li')

        imageUrl =li[0].find('img').get('src')
        res = requests.get(imageUrl)
        with open(os.path.join('Bing',cd+'.jpg'),'wb') as file:
            file.write(res.content)

        path = r'C:\Users\sal13\Desktop\Bing\\'+cd+'.jpg'
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)


'''
i = 1
for data in soup.findAll('item'):
    print (str(i)+'. '+data.find('description').text)
    i += 1

list_links = []    
for link in soup.findAll('item'):
    list_links.append(link.find('guid').text)

toaster = ToastNotifier()
user_input = 1

 
while True:       
    url = list_links[user_input - 1]    
    sc = requests.get(url)
    soup = BeautifulSoup(sc.text,'lxml')
    score = soup.findAll('title')
    toaster.show_toast("India Vs Afghanistan",
                   score[0].text,
                   icon_path=None,
                   duration=10)
    sleep (150)
'''
