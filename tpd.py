#! /usr/bin/python3

import requests,os
from bs4 import BeautifulSoup


url = input('Enter url of the tutorial to download: ')
name = input('Create new folder: ')
os.makedirs(name,exist_ok=True)
res = requests.get(url)
soup = BeautifulSoup(res.text)
ul = soup.findAll('ul',{'class':'nav nav-list primary left-menu'})

if len(ul) == 2:
	li = ul[0].find_all('li')
	for i in range(1,len(li)):
		href = li[i].find('a').get('href')
		new_url = 'http://www.tutorialspoint.com'+href
		res = requests.get(new_url)
		soup = BeautifulSoup(res.text,'lxml')
		pdf = soup.select('.pdf-btn a')
		url_pdf = 'http://www.tutorialspoint.com'+pdf[0].get('href')
		res = requests.get(url_pdf)
		print ('Downloading page '+str(i))
		pdffile = open(os.path.join(name,os.path.basename(url_pdf)),'wb')
		pdffile.write(res.content)
		pdffile.close()
elif len(ul) == 3:
	li = ul[0].find_all('li')
	li1 = ul[1].find_all('li')
	for i in range(1,len(li)):
		href = li[i].find('a').get('href')
		new_url = 'http://www.tutorialspoint.com'+href
		res = requests.get(new_url)
		soup = BeautifulSoup(res.text,'lxml')
		pdf = soup.select('.pdf-btn a')
		url_pdf = 'http://www.tutorialspoint.com'+pdf[0].get('href')
		res = requests.get(url_pdf)
		print ('Downloading page '+str(i))
		pdffile = open(os.path.join(name,os.path.basename(url_pdf)),'wb')
		pdffile.write(res.content)
		pdffile.close()
	for i in range(1,len(li1)):
		href = li1[i].find('a').get('href')
		new_url = 'http://www.tutorialspoint.com'+href
		res = requests.get(new_url)
		soup = BeautifulSoup(res.text,'lxml')
		pdf = soup.select('.pdf-btn a')
		url_pdf = 'http://www.tutorialspoint.com'+pdf[0].get('href')
		res = requests.get(url_pdf)
		print ('Downloading page '+str(i))
		pdffile = open(os.path.join(name,os.path.basename(url_pdf)),'wb')
		pdffile.write(res.content)
		pdffile.close()

elif len(ul) == 4:
	li = ul[0].find_all('li')
	li1 = ul[1].find_all('li')
	li2 = ul[2].find_all('li')
	for i in range(1,len(li)):
		href = li[i].find('a').get('href')
		new_url = 'http://www.tutorialspoint.com'+href
		res = requests.get(new_url)
		soup = BeautifulSoup(res.text,'lxml')
		pdf = soup.select('.pdf-btn a')
		url_pdf = 'http://www.tutorialspoint.com'+pdf[0].get('href')
		res = requests.get(url_pdf)
		print ('Downloading page '+str(i))
		pdffile = open(os.path.join(name,os.path.basename(url_pdf)),'wb')
		pdffile.write(res.content)
		pdffile.close()
	for i in range(1,len(li1)):
		href = li1[i].find('a').get('href')
		new_url = 'http://www.tutorialspoint.com'+href
		res = requests.get(new_url)
		soup = BeautifulSoup(res.text,'lxml')
		pdf = soup.select('.pdf-btn a')
		url_pdf = 'http://www.tutorialspoint.com'+pdf[0].get('href')
		res = requests.get(url_pdf)
		print ('Downloading page '+str(i))
		pdffile = open(os.path.join(name,os.path.basename(url_pdf)),'wb')
		pdffile.write(res.content)
		pdffile.close()
	for i in range(1,len(li2)):
		href = li2[i].find('a').get('href')
		new_url = 'http://www.tutorialspoint.com'+href
		res = requests.get(new_url)
		soup = BeautifulSoup(res.text,'lxml')
		pdf = soup.select('.pdf-btn a')
		url_pdf = 'http://www.tutorialspoint.com'+pdf[0].get('href')
		res = requests.get(url_pdf)
		print ('Downloading page '+str(i))
		pdffile = open(os.path.join(name,os.path.basename(url_pdf)),'wb')
		pdffile.write(res.content)
		pdffile.close()
