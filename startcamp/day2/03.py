# python에서 request를 보내는 유일한 library
import requests


response= requests.get('https://search.naver.com/search.naver?query=lg%EC%A0%84%EC%9E%90').text

# print 해보면 아주 복잡하기 때문에 예쁘게 나타내주는 라이브러리를 쓰자 (뷰티풀숩)
# print(response)

# F12 - copy - copy selector