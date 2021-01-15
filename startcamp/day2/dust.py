import requests
from pprint import pprint

key= 'O%2FcKosQ2judPsRRWS5g%2FkJxe%2BLsHDQ9A6loWj0NaQB1m4DIxt%2BVC35QWTpZeIvlNrrKgyBsw48eMFGLNzBDd9g%3D%3D'
return_type = 'json'
num_of_rows = '20'
page_no = '1'
sido_name = '경기'
ver = '1.0'
url= f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&returnType={return_type}&numOfRows={num_of_rows}&pageNo={page_no}&sidoName={sido_name}&ver={ver}'

response = requests.get(url).json()
# pprint(response)

location = response['response']['body']['items'][16]['stationName']
pm = response['response']['body']['items'][16]['pm10Value']

# location 자리에 response['response']['body']['items'][16]['stationName'] 못 넣는다.
notify = f'{location}의 미세먼지 농도는 {pm}입니다.'
print(notify)