import requests
from bs4 import BeautifulSoup

URL = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='
query = input('찾고 싶은 뉴스는??: ')

fullURL = URL + query

data = requests.get(fullURL).text
soup = BeautifulSoup(data, 'html.parser')
news_title = soup.find_all(class_='news_tit')
title_array = []

for title in news_title:
    title_array.append(title.get('title'))

for i in title_array:
    print(i)
