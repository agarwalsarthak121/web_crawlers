#! /usr/bin/python3

import requests
from bs4 import BeautifulSoup
import pyperclip
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
select = int(select)
        
if select == 1:
    print ('Enter search term:',end=' ')
    search = input()
    url = 'https://thepiratebay.se/search/'+search+'/0/99/0'

    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.text,'lxml')

    list = []
    i = 0
    j = 1
    for search_item in soup.findAll('a',{'class':'detLink'}):
        list.append(search_item.get('href'))
        seeds = soup.findAll('td',{'align':'right'})
        leeches = soup.findAll('td',{'align':'right'})
        print (str(j)+'. '+search_item.text,seeds[i].text,leeches[i+1].text)
        i += 2
        j += 1

    print ('Select :')
    user_input = int(input())

    url = 'https://thepiratebay.se'+list[user_input - 1]
    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.text,'lxml')

    magnet = soup.findAll('a',{'title':'Get this torrent'})
    pyperclip.copy(magnet[0].get('href'))
    print ('Magnet Link Copied')

elif select == 2:
    url = 'https://kickass.unblocked.li/usearch/'
    print ('Enter search term:')
    search = input()
    url = url+search

    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.text,'lxml')

    list = []   
    i = 1
    for search_item in soup.findAll('a',{'class':'cellMainLink'}):
        list.append(search_item.get('href'))
        size = soup.findAll('td',{'class':'nobr center'})
        seeds = soup.findAll('td',{'class':'green center'})
        leeches = soup.findAll('td',{'class':'red lasttd center'})
        print (str(i)+'. '+search_item.text,size[i-1].text,seeds[i-1].text,leeches[i-1].text)
        i += 1

    print ('Select :')
    user_input = int(input())

    url = 'https://kickass.unblocked.li'+list[user_input - 1]
    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.text,'lxml')

    for magnet in soup.findAll('a',{'class':'kaGiantButton '}):
        pyperclip.copy(magnet.get('href'))
        print ('Magnet link Copied')

elif select == 3:
    print ('Enter search term:')
    search = input()
    url = 'http://extratorrent.date/search/?search='+search+'&new=1&x=0&y=0'
    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.text,'lxml')

    list = []   
    i = 1
    for search_item in soup.findAll('td',{'class':'tli'}):
        list.append(search_item.find('a').get('href'))
        seeds = soup.findAll('td',{'class':'sy'})
        leeches = soup.findAll('td',{'class':'ly'})
        if len(search_item.find_all('a')[0].text) < 4:
            search_item = search_item.find_all('a')[1].text
        else:
            search_item = search_item.find_all('a')[0].text
        print (str(i)+'. '+search_item,seeds[i-1].text,leeches[i-1].text)
        i += 1
        if i > 20:
            break
    
    print ('Select :')
    user_input = int(input())

    url = 'http://www.extratorrent.date'+list[user_input - 1]
    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.text,'lxml')

    for magnet in soup.findAll('a',{'title':'Magnet link'}):
        pyperclip.copy(magnet.get('href'))
        print ('Magnet link Copied')
