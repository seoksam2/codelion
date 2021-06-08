import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'http://www.daum.net'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
results = soup.findAll('a', 'link_favorsch')
rank = 1

search_rank_file = open(
    '/Users/seoksam2/Documents/projects/codelion_python/deepening_python_Chapter2/rankResult.txt', 'w')


print(datetime.today().strftime('%y년 %m월 %d일의 실시간 검색어 순위 입니다. \n'))
for result in results:
    search_rank_file.write(str(rank)+'위:' + result.get_text()+'\n')
    print(rank, "위: ", result.get_text(), '\n')
    rank = rank + 1

# file = open('daum.net', 'w')
# file.write(response.text)
# file.close()

# print(soup.title)
# print(soup.title.string)
# print(soup.span.string)
