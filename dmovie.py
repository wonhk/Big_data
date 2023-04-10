import requests
from bs4 import BeautifulSoup

# 내가 만든 모듈(함수)를 포함
# import function
from function import my_print
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.daum.net/ranking/reservation',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 크롬에서 beatifulsoup로 가져온 파일을 크롤링
# print(soup)

# 단일 영화 정보 크롤링
# title = soup.select_one("#mainContent > div > div.box_ranking > ol > li:nth-child(1) > div > div.thumb_cont > strong > a")
# print(title.text)

lis = soup.select("#mainContent > div > div.box_ranking > ol > li")

for li in lis:
    #print(li)
    #R = f'{rank.text}위' # 순위
    #N = f'{name.text}' # 영화제목
    #M = F'{mp.text}점' # 평점
    rank = li.select_one("span.rank_num")
    name = li.select_one("div > strong > a")
    mp =  li.select_one("span.txt_grade")
    my_print(f'{rank.text}위 {name.text} 평점 : {mp.text}점')


'''
# 각 영화사이트 마다 취급하는 코드가 다르기 떄문에 
# 각 영화 타이틀 코드에 대한 패턴을 찾아서 select에 집어 넣어주고 꺼낸다
ex) 네이버 tb
'''
