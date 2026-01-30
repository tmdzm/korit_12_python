'''
1. while 반복문
    while 다음에 나오는 조건식이 참이라면 참인 동안 돌아감
while 조건식 1:
    반복실행문1

특정 시점에는 while 반복문이 종료될 수 있게 지정
'''

n = 1
while n < 11:
    print(n)
    n += 1 # ++는 없다

while n > 1:
    print(n-1)
    n -= 1

dan = 2

while dan < 10:
    number = 1
    while number < 10:
        print(f'{dan} x {number} = {dan * number}')
        number += 1
    dan += 1

# print(number) 하면 10이 나온다. 전역/지역 변수개념이 java와는 다르다.