import random

# 비복원추출
numbers = random.sample(range(1, 46), 6)
print(numbers)

# string-interpolation
# f-string
# string 사이에 값을 삽입
print(f'오늘의 로또 번호는 {numbers} 입니다.')