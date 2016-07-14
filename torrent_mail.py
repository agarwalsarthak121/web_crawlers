import imaplib,random
imaplib._MAXLINE = 1000000
import pprint
import imapclient
import pyzmail
import os
from time import sleep
import requests
from bs4 import BeautifulSoup
from twilio.rest import TwilioRestClient
from getpass import getpass

imapObj = imapclient.IMAPClient('imap.gmail.com',ssl=True)
username = input('Enter username: ')
passwrd = getpass()
imapObj.login(username,passwrd)
print ('Login Successful')
imapObj.select_folder('INBOX',readonly=False)
print ('To download torrent just send a mail to your mail id with subject "torrent <movie/tv series name>"')

while True:

	UIDs = imapObj.search('ALL')
	rawMessages = imapObj.fetch(UIDs[-1:], ['BODY[]'])
	message = pyzmail.PyzMessage.factory(rawMessages[UIDs[-1]][b'BODY[]'])
	m = message.get_subject()
	if 'torrent' in m.lower():
		search = m[8:]
		url = 'https://kickass.unblocked.li/usearch/'+search
		source_code = requests.get(url)
		soup = BeautifulSoup(source_code.text,'html5lib')  
		search_item = soup.findAll('a',{'class':'cellMainLink'})
		url = 'https://kickass.unblocked.li'+search_item[0].get('href')
		source_code = requests.get(url)
		soup = BeautifulSoup(source_code.text,'html5lib')
		imapObj.delete_messages(UIDs[-1])
		imapObj.expunge()
		for magnet in soup.findAll('a',{'class':'kaGiantButton '}):
			os.system('qbittorrent '+magnet.get('href'))
	else:
		print ('Nothing found')
