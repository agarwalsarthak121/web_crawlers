import os
import shutil
import requests
from bs4 import BeautifulSoup

source = os.walk(os.getcwd())

for x,y,z in source:
    files = z
    break

for movies in files:
    if movies[-3:].lower() == 'mp4' or movies[-3:].lower() == 'avi' or movies[-3:].lower() == 'mkv' or movies[-3:].lower() == 'flv':
        url = 'http://www.imdb.com/find?ref_=nv_sr_fn&q='+movies[:-4]+'&s=all'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,'lxml')

        name = soup.findAll('td',{'class':'result_text'})
        href = name[0].find('a')['href']
        movie_page = 'http://www.imdb.com'+href

        def get_title(movie_url):
            source_code = requests.get(movie_url)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text,'lxml')
            for title in soup.findAll('div',{'class':'title_wrapper'}):
                return title.find('h1').text.rstrip()

        movie_name = get_title(movie_page)

        source_code = requests.get(movie_page)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,'lxml')
        rate = soup.findAll('div',{'class':'ratingValue'})
        rating = rate[0].text[:-4]
        print (movie_name,rating)
        folder = rating+'- '+movie_name
        os.makedirs(folder,exist_ok=True)
        shutil.move('./'+movies,'./'+folder)

  



