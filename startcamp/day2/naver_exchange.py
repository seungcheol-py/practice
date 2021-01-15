import requests
from bs4 import BeautifulSoup

url='https://finance.naver.com/marketindex/'

response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')


result = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text
print(result)

# JSON (Javascript Object Notation) : 데이터를 주고 받기 위한 표현법
# 파이썬의 리스트와 딕셔너리를 이용하여 표현할 수 있다.
# API : 응용프로그램간의 대화
# 배달의 민족과 페이스북의 대화
# 데이터를 보낼 때 JSON으로 보내준다.
# 데이터를 보낼 때는 규칙이 있다.
# 너가 이렇게 보내야 내가 응답을 해줄게