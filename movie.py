import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)
# 내가 원하는 위치에 있는 데이터 가져오기
# 결과 = soup.select('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')

'''
#오 그러면 이렇게 해도
출력에도 상관이 없겠네
??????
'''
trs = soup.select("#old_content > table > tbody > tr")
#랭킹을 달아주기 위한 변수
rank = 0
for tr in trs:
    a_tag = tr.select_one("td.title > div > a")
    # 만약에 a_tag가 None이 아니면
    if a_tag is not None:
        rank = rank + 1 
        print(rank, a_tag.text)
