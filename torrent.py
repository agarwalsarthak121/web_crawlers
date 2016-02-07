#! /usr/bin/python3

import requests
from bs4 import BeautifulSoup
import pyperclip

'''
print ('Select your torrent search engine:')
print ('Enter 1 to search on pirate bay')
print ('Enter 2 to search on kickass')
print ('Enter 3 to search on extratorrent')
while True:
    select = input()
    if select != '1' and select != '2' and select != '3':
        print ('Enter correct input')
        continue
    else:
        break
select = int(select)'''
      

print ('Enter search term:',end=' ')
search = input()
list = []

print ('Piratebay:')   
print () 
url = 'https://thepiratebay.se/search/'+search+'/0/99/0'
source_code = requests.get(url)
soup = BeautifulSoup(source_code.text,'lxml')
i = 0
j = 1
for search_item in soup.findAll('a',{'class':'detLink'}):
    list.append(search_item.get('href'))
    seeds = soup.findAll('td',{'align':'right'})
    leeches = soup.findAll('td',{'align':'right'})
    print (str(j)+'. '+search_item.text,seeds[i].text,leeches[i+1].text)
    i += 2
    j += 1
    if j > 10:
        break

print ()
print ('Kickass Torrents')
print ()
url = 'https://kickass.unblocked.li/usearch/'+search
source_code = requests.get(url)
soup = BeautifulSoup(source_code.text,'lxml')  
i = 1
for search_item in soup.findAll('a',{'class':'cellMainLink'}):
    list.append(search_item.get('href'))
    size = soup.findAll('td',{'class':'nobr center'})
    seeds = soup.findAll('td',{'class':'green center'})
    leeches = soup.findAll('td',{'class':'red lasttd center'})
    print (str(j)+'. '+search_item.text,size[i-1].text,seeds[i-1].text,leeches[i-1].text)
    i += 1
    j += 1
    if j > 20:
        break

print ()
print ('Extratorrent')
print ()
url = 'http://extratorrent.date/search/?search='+search+'&new=1&x=0&y=0'
source_code = requests.get(url)
soup = BeautifulSoup(source_code.text,'lxml')
i = 1
for search_item in soup.findAll('td',{'class':'tli'}):
    list.append(search_item.find('a').get('href'))
    seeds = soup.findAll('td',{'class':'sy'})
    leeches = soup.findAll('td',{'class':'ly'})
    if len(search_item.find_all('a')[0].text) < 4:
        search_item = search_item.find_all('a')[1].text
    else:
        search_item = search_item.find_all('a')[0].text
    print (str(j)+'. '+search_item,seeds[i-1].text,leeches[i-1].text)
    i += 1
    j += 1
    if j > 30:
        break

while True:
    try:
        user_input = int(input('Enter the number of the file to download: '))
    except ValueError:
        print ('Enter correct input')
        continue
    if user_input < 1 or user_input > 30:
        print ('Enter correct input')
        continue
    else:
        break

if 1 <= user_input <= 10:
    url = 'https://thepiratebay.se'+list[user_input - 1]
    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.text,'lxml')
    magnet = soup.findAll('a',{'title':'Get this torrent'})
    pyperclip.copy(magnet[0].get('href'))
    print ('Magnet Link Copied')
    
elif 11 <= user_input <= 20:
    url = 'https://kickass.unblocked.li'+list[user_input - 1]
    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.text,'lxml')
    for magnet in soup.findAll('a',{'class':'kaGiantButton '}):
        pyperclip.copy(magnet.get('href'))
        print ('Magnet link Copied')
elif 20 <= user_input <= 30:
    url = 'http://www.extratorrent.date'+list[user_input - 1]
    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.text,'lxml')
    for magnet in soup.findAll('a',{'title':'Magnet link'}):
        pyperclip.copy(magnet.get('href'))
        print ('Magnet link Copied')
