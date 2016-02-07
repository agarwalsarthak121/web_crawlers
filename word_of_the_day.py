#! /usr/bin/python3

import requests
from bs4 import BeautifulSoup

dict_url = ['http://dictionary.reference.com/','http://dictionary.cambridge.org/','http://www.merriam-webster.com/']

source_code = requests.get(dict_url[0])
plain_text = source_code.text
soup = BeautifulSoup(plain_text,'lxml')

fw = open('word.txt','w')

for word in soup.findAll('a',{'class':'wotd'}):
    for word_meaning in soup.findAll('a',{'class':'wotd_txt'}):
        fw.write('Word of the day: ')
        fw.write(word.text+' - '+word_meaning.text+'\n')

source_code = requests.get(dict_url[1])
plain_text = source_code.text
soup = BeautifulSoup(plain_text,'lxml')
i = 1
for word_meaning in soup.findAll('div',{'class':'cdo-fbox-body'}):
    for word in soup.findAll('h3',{'class':'wotdHeadword'}):
        while i:
            fw.write('Word of the day: ')
            fw.write(word.text+' - '+word_meaning.find('p').text+'\n')
            i = 0
            
source_code = requests.get(dict_url[2])
plain_text = source_code.text
soup = BeautifulSoup(plain_text,'lxml')

for word in soup.findAll('h4',{'class':'wh-word'}):
    for word_meaning in soup.findAll('p',{'class':'wh-def-text'}):
        fw.write('Word of the day: ')
        fw.write(word.find('a').text+' - '+word_meaning.text+'\n')
        
        
