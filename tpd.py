#! /usr/bin/python3

import requests,os
from bs4 import BeautifulSoup


url = input('Enter url of the tutorial to download: ')
name = input('Create new folder: ')
os.makedirs(name,exist_ok=True)
res = requests.get(url)
soup = BeautifulSoup(res.text,'html5lib')
ul = soup.findAll('ul',{'class':'nav nav-list primary left-menu'})
print (len(ul))

for i in range(len(ul)):
	li = ul[i].find_all('li')
	for j in range(1,len(li)):
		href = li[j].find('a').get('href')
		new_url = 'http://www.tutorialspoint.com'+href
		res = requests.get(new_url)
		soup = BeautifulSoup(res.text,'html5lib')
		pdf = soup.select('.pdf-btn a')
		if len(pdf) != 0:
			url_pdf = 'http://www.tutorialspoint.com'+pdf[0].get('href')
			res = requests.get(url_pdf)
			print ('Downloading page '+str(j))
			pdffile = open(os.path.join(name,os.path.basename(url_pdf)),'wb')
			pdffile.write(res.content)
			pdffile.close()
		else:
			continue
print ('Download Complete')
