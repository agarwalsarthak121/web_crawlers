import requests
from bs4 import BeautifulSoup
import pynotify
import random
from time import sleep

fw = open('.facts.txt','r')
facts = fw.read()
facts = facts.split('\n')
while True:    
    i = random.randrange(0,len(facts)-1)
    pynotify.init('test')
    n = pynotify.Notification('Fact No. '+str(i),facts[i])
    n.show()
    sleep (90)

'''
for i in range(10):
    url = 'http://www.snapple.com/real-facts/list-view/'+str(i+1)       
    sc = requests.get(url)
    soup = BeautifulSoup(sc.text,'lxml')
    fact = soup.findAll('p',{'class':'fact_detail'})
    for i in range(len(fact)):
        fw.write(fact[i].text+'\n')'''
