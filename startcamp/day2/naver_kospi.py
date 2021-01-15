# import가 쌓여있으면 짧은 게 위로 가는걸 권장
import requests
# bs4 안의 BeautifulSoup만 import
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'

# 전체 데이터 중에 text만 가져오기
response = requests.get(url).text

data = BeautifulSoup(response, 'html.parser')

# 꾸민 응답 중에서 원하는 데이터만 선택한다.
result = data.select_one('#KOSPI_now').text
print(result)