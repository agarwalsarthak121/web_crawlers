#! /usr/bin/python
import requests
from bs4 import BeautifulSoup
import pynotify
import pyperclip
from time import sleep

while True:
    movie = pyperclip.paste()
    if movie != '':
        url = 'http://www.imdb.com/find?ref_=nv_sr_fn&q='+movie+'&s=all'
        pyperclip.copy('')
        print 'You searched for '+movie
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,'lxml')

        for td in soup.findAll('td',{'class':'result_text'}):
            href = td.find('a')['href']
            movie_page = 'http://www.imdb.com'+href
            break

        def get_title(movie_url):
            source_code = requests.get(movie_url)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text,'lxml')
            for title in soup.findAll('div',{'class':'title_wrapper'}):
                return title.find('h1').text.rstrip()

        movie_name = get_title(movie_page)

        def get_movie_data(movie_url):
            source_code = requests.get(movie_url)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text,'lxml')
            div = soup.findAll('div',{'class':'ratingValue'})
            div2 = soup.findAll('div',{'class':'summary_text'})
            pynotify.init('test')
            n = pynotify.Notification(movie_name+' '+div[0].text,div2[0].text.lstrip())
            n.show()

        get_movie_data(movie_page)
    print 'copy a movie name to search'
    sleep(5)

'''print_genre = soup.findAll('div',{'class':'subtext'})
for div in print_genre:
    for genre in print_genre.findAll('a'):
        print (genre.text,end=' |')
        print ()'''

