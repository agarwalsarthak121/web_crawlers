#! /usr/bin/python3
# multidownloadXkcd.py - Downloads XKCD comics using multiple threads.

import requests, os,threading
from bs4 import BeautifulSoup

os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        print('Downloading page http://xkcd.com/%s...' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        soup = BeautifulSoup(res.text,'lxml')
        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = 'http:'+comicElem[0].get('src')
            # Download the image.
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            # Save the image to ./xkcd.
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            imageFile.write(res.content)
            imageFile.close()

downloadThreads = []  
for i in range(1, 1648, 100): 
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, min(i + 100,1649)))
    downloadThreads.append(downloadThread)
    downloadThread.start()

for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
