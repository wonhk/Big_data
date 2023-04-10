import requests
from bs4 import BeautifulSoup
import csv
from openpyxl import Workbook

# 엑셀파일 쓰기 준비
# 엑셀파일 쓰기
write_wb = Workbook()

# 이름이 있는 시트를 생성
write_ws = write_wb.create_sheet('생성시트')

# Sheet1에다 입력
write_ws = write_wb.active

# 헤더 입력
write_ws['A1'] = '순위'
write_ws['B1'] = '제목'
write_ws['C1'] = '평점'

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
    ranking = li.select_one("span.rank_num")
    name = li.select_one("div > strong > a")
    mp =  li.select_one("span.txt_grade")
    R = f'{ranking.text}위' # 순위
    N = f'{name.text}' # 영화제목
    M = f'{mp.text}점' # 평점
    #print(rank.text, name.text, mp.text)
    write_ws.append([R, N, M])

write_wb.save('영화 순위 다음.xlsx')
'''
# 각 영화사이트 마다 취급하는 코드가 다르기 떄문에 
# 각 영화 타이틀 코드에 대한 패턴을 찾아서 select에 집어 넣어주고 꺼낸다
ex) 네이버 tb
# 인식시킬때 줄 순서도 중요하니까 알아둘 것
'''
