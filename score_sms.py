import urllib2
import cookielib
from getpass import getpass
import sys
import os
from stat import *
import requests
from bs4 import BeautifulSoup
from time import sleep



print ('Live Cricket Matches:')
print ('='*len('Live Cricket Matches:'))
url = "http://static.cricinfo.com/rss/livescores.xml"
sc = requests.get(url)
soup = BeautifulSoup(sc.text,'html5lib')

i = 1
for data in soup.findAll('item'):
    print (str(i)+'. '+data.find('description').text)
    i += 1

list_links = []    
for link in soup.findAll('item'):
    list_links.append(link.find('guid').text)

while True:
    try:
        user_input = int(input('Enter match no: '))
    except ValueError:
        print ('Enter correct input')
        continue
    if user_input < 1 or user_input > 30:
        print ('Enter correct input')
        continue
    else:
        break
loginid = raw_input('Enter login id :')
passwrd = getpass()
number = raw_input("Enter number: ")
t = raw_input('Set time interval: ')
while True:       
	url = list_links[user_input - 1]    
	sc = requests.get(url)
	soup = BeautifulSoup(sc.text,'html5lib')
	score = soup.findAll('title')
	message = score[0].text[:130]

	if __name__ == "__main__":    
		username = loginid
		passwd = passwrd
	
	message = "+".join(message.split(' '))
	
	 #logging into the sms site
	url ='http://site24.way2sms.com/Login1.action?'
	data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
	
	 #For cookies
	
	cj= cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	
	 #Adding header details
	opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
	try:
		usock =opener.open(url, data)
	except IOError:
		print "error"
	        #return()
	
	jession_id =str(cj).split('~')[1].split(' ')[0]
	send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
	send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
	opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
	try:
	        sms_sent_page = opener.open(send_sms_url,send_sms_data)
	except IOError:
	        print "error"
	        #return()
	print "success" 
	    #return ()
	sleep (int(t))
