import requests
from bs4 import BeautifulSoup
import re

url = 'https://careers.linecorp.com/ko/jobs?co=Korea&ca=Engineering&fi=Tech%20Mgmt'
responce = requests.get(url)
html = responce.content.decode('utf-8', 'replace')

soup = BeautifulSoup(html, 'html.parser')
count = 1

file = open('jobList.text', 'w')

file.close

results = soup.find_all('h3', 'title')


for result in results:
    file.write(str(count) + ': ' + result.get_text() + '\n')
    print(count, ': ', result.get_text(), '\n')
    count += 1
