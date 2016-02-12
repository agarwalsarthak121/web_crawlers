#! /usr/bin/python3
import requests
from bs4 import BeautifulSoup
movie_list = []
no = int(input('Enter no. of movies you want to compare: '))
for i in range(no):
    movie_list.append(input('Enter movie '+str(i+1)+': '))
    print ()

def get_movie_data(movie_url):
        source_code = requests.get(movie_url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,'lxml')
        for div in soup.findAll('div',{'class':'ratingValue'}):
            print ('Imdb rating of the movie/Tv Series "'+movie_name+'" is: ',end='')
            print (div.text)
            

        for div in soup.findAll('div',{'class':'summary_text'}):
            print ('Summary of the movie/Tv series:')
            print (div.text.lstrip())
            print ()

def get_title(movie_url):
    source_code = requests.get(movie_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'lxml')
    for title in soup.findAll('div',{'class':'title_wrapper'}):
        return title.find('h1').text.rstrip()

for movie in movie_list:
    url = 'http://www.imdb.com/find?ref_=nv_sr_fn&q='+movie+'&s=all'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'lxml')

    for td in soup.findAll('td',{'class':'result_text'}):
        href = td.find('a')['href']
        movie_page = 'http://www.imdb.com'+href
        break

    movie_name = get_title(movie_page)
    get_movie_data(movie_page)

'''print_genre = soup.findAll('div',{'class':'subtext'})
for div in print_genre:
    for genre in print_genre.findAll('a'):
        print (genre.text,end=' |')
        print ()'''

