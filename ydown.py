import requests
import os
from bs4 import BeautifulSoup

search = input('Enter search term: ')
print ()
print ('Search results: ')
print ()
url = 'https://www.youtube.com/results?search_query='+search
sc = requests.get(url)
soup = BeautifulSoup(sc.text,'lxml')
results = soup.findAll('a',{'class':'yt-uix-sessionlink yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2       spf-link '})
i = 0
for result in results:
    i += 1
    print (str(i)+'. '+result.text)

print ()

while True:    
    try:    
        user_input = int(input('Enter the video you want to download: '))
    except NameError:
        print ('Enter correct input')
        continue
    if 1 <= user_input <= i:
        break
    else:
        print ('Enter correct input')
        continue

res = input('Enter quality of the video you want to download(360/720: ')
if res == '360':
    quality = 18
elif res == '720':
    quality = 22

os.system('youtube-dl -f '+str(quality)+' '+'https://www.youtube.com'+results[user_input - 1].get('href'))
