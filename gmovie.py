import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.daum.net/ranking/reservation',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
#print(soup)
#title = soup.select_one("#mainContent > div > div.box_ranking > ol > li:nth-child(1) > div > div.thumb_cont > strong > a")

#print(title.text)
lis = soup.select("#mainContent > div > div.box_ranking > ol > li")

ranking = 1;

for li in lis:
    #print(li)
    a_tag = li.select_one("div > strong > a")
    print(ranking, a_tag.text)
    ranking = ranking + 1

'''
# 각 영화사이트 마다 취급하는 코드가 다르기 떄문에 
# 각 영화 타이틀 코드에 대한 패턴을 찾아서 select에 집어 넣어주고 꺼낸다
ex) 네이버 tb
'''
