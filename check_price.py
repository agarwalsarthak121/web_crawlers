#! /usr/bin/python3

from win10toast import ToastNotifier
from time import sleep
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import pyperclip
from time import sleep


url = 'https://www.amazon.in/Song-Ice-Fire-Thrones-Complete/dp/0007477155/ref=sr_1_1?ie=UTF8&qid=1528800191&sr=8-1&keywords=got+book+set' 
url2 = 'https://www.flipkart.com/george-r-martin-s-game-thrones-5-book-boxed-set-song-ice-fire-series-thrones-clash-kings-storm-swords-feast-crows-dance-dragons/p/itmfyhk9c5jzfgvt?pid=9780345535528&lid=LSTBOK9780345535528NUOHSQ&marketplace=FLIPKART&srno=s_1_1&otracker=search&fm=SEARCH&iid=ef6013f0-438b-4d23-b475-7966b38c4914.9780345535528.SEARCH&ppt=Homepage&ppn=Homepage&ssid=x1kd01smps0000001528798671360&qH=14172ef60ac4bd59'


source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,'lxml')

price_ama = soup.find('span',{'class':'a-size-medium a-color-price inlineBlock-display offer-price a-text-normal price3P'})

source_code2 = requests.get(url2)
plain_text2 = source_code2.text
soup2 = BeautifulSoup(plain_text2,'lxml')

price_flip = soup2.find('div',{'class':'_1vC4OE _3qQ9m1'})
toaster = ToastNotifier()
    
price_ama = float(price_ama.text.replace(',',''))
price_flip = float(price_flip.text[1:].replace(',',''))
if ( price_ama < 500 or price_flip < 500):
    if(price_ama < price_flip):
        toaster.show_toast("Price Alert","Price reduced on amazon to : " + str(price_ama)
                               ,icon_path=None,
                               duration=10)
    else:
        toaster.show_toast("Price Alert","Price reduced on flipkart to : " + str(price_flip),icon_path=None,duration=10)
else:
    toaster.show_toast("Current Price","Flipkart : Rs. " + str(price_flip) + "\nAmazon : Rs. " + str(price_ama)
                           ,icon_path=None,
                               duration=10)

        

