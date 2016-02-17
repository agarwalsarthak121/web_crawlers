import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import pynotify
from time import sleep
import os
from pySmartDL import SmartDL
import wget

j = 0

while True:
    ep_no = 7
    url = 'http://animeshow.tv/Boku-dake-ga-Inai-Machi/'
    sc = requests.get(url)
    soup = BeautifulSoup(sc.text,'lxml')
    ep = soup.select('a h2')
    li = soup.select('td a')
    for i in range(4,len(ep)+4):
        if ep[i-4].text == 'Boku dake ga Inai Machi Episode '+str(ep_no):
            pynotify.init('test')
            n = pynotify.Notification('Episode '+str(ep_no)+' released','Firefox Will open Automatically and download will begin shortly')
            n.show()            
            url = 'http://9xbuddy.com/download?url='+li[i].get('href')
            driver = webdriver.Firefox()
            driver.get(url)
            sleep (30)
            down = driver.find_element_by_link_text('Download Now')
            href = down.get_attribute('href')
            wget.download(href)
            '''
            dest = '~/Downloads/'
            obj = SmartDL(href,dest)
            obj.start()
            # [*] 0.23 Mb / 0.37 Mb @ 88.00Kb/s [##########--------] [60%, 2s left]
            path = obj.get_dest()
            
            link.click()
            sc = requests.get(url)
            soup = BeautifulSoup(sc.text,'lxml')
            li = soup.findAll('li',{'class':'download-link-download lbcolor'})
            print li
            href = li[0].find('a')['href']
            download.down(href)
            '''
            j += 1
            break       
    if j == 0:
        print 'Not released yet'
        sleep (90)
    elif j == 1:
        pynotify.init('test')
        n = pynotify.Notification('Notfication','Episode Downloaded')
        n.show()
        break    
