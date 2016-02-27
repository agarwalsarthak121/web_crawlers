#! /usr/bin/python3

import requests
from bs4 import BeautifulSoup
import os
import re
import threading
import time

#Search for the desired manga
search = input('Enter name of anime: ')
print ()
search = search.split()
search = ('+').join(search)
search_url = 'http://manga.animea.net/series_old.php?title_range=0&title='+search+'&author_range=0&author=&artist_range=0&artist=&completed=0&yor_range=0&yor=&type=3&genre%5BAction%5D=0&genre%5BAdventure%5D=0&genre%5BComedy%5D=0&genre%5BDoujinshi%5D=0&genre%5BDrama%5D=0&genre%5BEcchi%5D=0&genre%5BFantasy%5D=0&genre%5BGender_Bender%5D=0&genre%5BHarem%5D=0&genre%5BHistorical%5D=0&genre%5BHorror%5D=0&genre%5BJosei%5D=0&genre%5BMartial_Arts%5D=0&genre%5BMature%5D=0&genre%5BMecha%5D=0&genre%5BMystery%5D=0&genre%5BPsychological%5D=0&genre%5BRomance%5D=0&genre%5BSchool_Life%5D=0&genre%5BSci-fi%5D=0&genre%5BSeinen%5D=0&genre%5BShotacon%5D=0&genre%5BShoujo%5D=0&genre%5BShoujo_Ai%5D=0&genre%5BShounen%5D=0&genre%5BShounen_Ai%5D=0&genre%5BSlice_of_Life%5D=0&genre%5BSmut%5D=0&genre%5BSports%5D=0&genre%5BSupernatural%5D=0&genre%5BTragedy%5D=0&genre%5BYaoi%5D=0&genre%5BYuri%5D=0&input=Search'

#Getting search results and links
sc0 = requests.get(search_url)
soup0 = BeautifulSoup(sc0.text,'lxml')
search_li = []
search_result = soup0.findAll('ul',{'class':'mangalisttext'})
k = 1
for i in range(len(search_result)):
    res = search_result[i].find_all('a')
    for j in range(len(res)):
        print (str(k)+'. '+res[j].text)
        search_li.append(res[j].get('href'))
        k += 1
print ()

#Select the desired search result
user_input = int(input('Enter your choice number: '))
url_sel = 'http://manga.animea.net'+search_li[user_input-1]
x = len(res[user_input - 1].text)
sc = requests.get(url_sel)
soup = BeautifulSoup(sc.text,'lxml')
chap_list = soup.select('.col2 a')
chap_list.reverse()
link_list = []

#Creating directory and Getting chapters
os.makedirs(search+'_Manga', exist_ok=True)
os.chdir('./'+search+'_Manga')
source = os.listdir(os.getcwd())
print ('No. of chapters in your selected manga :',len(chap_list))
for i in range(len(chap_list)):
    link_list.append(chap_list[i].get('href'))
chap_no = []
chap_name = re.compile(r'\d+(.)?\d*')
for li in chap_list:
    mo = chap_name.search(li.text[x+1:])
    mo1 = mo.group()
    chap_no.append(mo1)
print (chap_no)


sample = input('Enter 1 for full download & Enter 2 for sample: ')
if sample == '1':
    star = 0
    end = len(chap_list)
if sample == '2':
    star = 0
    end = star + 2
        

startTime = time.time()
#Downloading Images
for chap in range(star,end):
    url_sel = 'http://manga.animea.net'+link_list[chap]
    sc1 = requests.get(url_sel)
    soup1 = BeautifulSoup(sc1.text,'lxml')
    opt = soup1.findAll('option')
    chap_pages = int(opt[-1].text)
    print ('Pages in chapter '+chap_no[chap]+' '+str(chap_pages))
    page = 1
    while True:
        if page > chap_pages:
            break
        try:
            for fi in source:
                if fi == 'C'+chap_no[chap]+'P'+str(page)+image_url[-4:] :
                    print ('Skipping...')
                    page += 1
                    break
            else:
                sc2 = requests.get(url_sel[:-5]+'-page-'+str(page)+'.html')
                soup2 = BeautifulSoup(sc2.text,'lxml')
                img = soup2.select('td img')
                image_url = img[0].get('src')
                sc3 = requests.get(image_url)
                print ('Downloading page '+str(page))
                with open('C'+chap_no[chap]+'P'+str(page)+image_url[-4:], 'wb') as file:
                    file.write(sc3.content)
                page += 1
        except requests.exceptions.ConnectionError:
            continue

#Noting End time
endTime = time.time()
print ('Done in '+str(endTime - startTime))
