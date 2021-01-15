import requests

name='kim'
url = f'https://api.agify.io/?name={name}'

response = requests.get(url).json()
age = response['age']

print(f'{name}이 예상 나이는 {age}살입니다.')