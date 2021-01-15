import requests
from bs4 import BeautifulSoup

# API는 사용 방법이 있으니 그에 맞추어야 한다.
KEY = 'O%2FcKosQ2judPsRRWS5g%2FkJxe%2BLsHDQ9A6loWj0NaQB1m4DIxt%2BVC35QWTpZeIvlNrrKgyBsw48eMFGLNzBDd9g%3D%3D'
URL = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={KEY}&numOfRows=5&pageNo=1&sidoName=서울&ver=1.0&returnType=xml'

response = requests.get(URL).text
data = BeautifulSoup(response, 'xml')
# print(data)
item = data('item')[0]
time = item.dataTime.text
station = item.stationName.text
dust = int(item.pm10Value.text)

print(f'{time} 기준 {station}의 미세먼지 농도는 {dust} 입니다.')

if 150 < dust:
    print('매우나쁨')
elif 80 < dust:
    print('나쁨')
elif 50 < dust:
    print('보통')
else:
    print('좋음')