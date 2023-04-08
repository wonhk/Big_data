#print('hello_world')

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://serieson.naver.com/v3/movie?isWebtoonAgreePopUp=true',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# print(soup)

#title = soup.select_one('#flicking_paging > li:nth-child(1) > a > div.Poster_info_area__HGRo_ > span')
#print(title.text)

list = soup.select("#flicking_paging > li")

rank = 0

for li in list:
    name = li.select_one("a > div > span")
    rank = rank + 1
    print(f'{rank}위 영화제목 : {name.text}')
    
    
