import mechanize
from bs4 import BeautifulSoup
from twilio.rest import Client
from time import sleep

def getShareList():
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.open("https://procapital.mohdfaiz.com/login.php")	   #Url that contains signin form
	br.select_form(nr=1)
	br['loginid'] = "agarwalsarthak121@gmail.com"	#see what is the name of txt input in form
	br['pass'] = <password>
	result = br.submit().read()

	equity = br.open('https://procapital.mohdfaiz.com/equity-swing-trading.php').read()

	soup = BeautifulSoup(equity,'lxml')
	currentShareList = []
	listOfShares = soup.find('table',{'id':'myTable'}).find('tbody').findAll('tr')
	for i in range(0,3):
		currentShareList.append(listOfShares[i].findAll('td')[2].findAll('strong')[0].text)
	
	return currentShareList

	
prevShareList = []
while(True):
	print('Checking for updates')
	currentShareList = getShareList()
	accountSid = 'AC935014984024ae40fcbf3411edb30bd6'
	authToken = '2f163e61c39124da4a1f3060e271b143'
	client = Client(accountSid, authToken)
	
	if(prevShareList != currentShareList):
		print('Update found')
		print('Sending whatsapp message')
		for i in range(0,len(currentShareList)):
			message = client.messages.create( 
									  from_='whatsapp:+14155238886',  
									  body=currentShareList[i],      
									  to='whatsapp:+919739309478' 
								  ) 
	prevShareList = currentShareList
