'''
1. 함수의 종류
    1) 파이썬 내장 함수
    2) 메서드
    3) 사용자 정의 함수
2. 함수 용어 정리
    1) 함수 정의 : 사용자 정의 함수를 새로 만드는 것
    2) 인수(argument) : 함수에 전달할 입력값
    3) 매개변수 : argument를 받아서 저장하는 변수를 의미
    4) 반환값/결과값/return값 : 함수의 출력값
    5) 함수 호출 : 함수르 실제로 사용하는 것으 의미
3. (사용자 정의) 함수의 형식 :
    1) 함수의 정의 부분
def 함수_이름(매개변수1,매개변수2):
    실행문
    return blahblah

    2) 함수 호출 부분
변수 = 함수_일름(argument1, argument2)

'''

# eng_name = input('너의 영어 이름은? >>> ')
# eng_name_low = eng_name.lower()
# eng_name_up = eng_name_low.upper()
# print(f'{eng_name_low} / {eng_name_up}')

'''
.lower()는 str 데이터를 소문자로
.upper()는 대문자로 바꾼다.
특정클래스에 종속된 함수들을 메소드(method)라고 한다.
함수는 독립적을로 사용이 가능하다.
Java / JS 때와 마찬가지로 call1()~4() 유형으로 정의할 수 있다.


'''
# def multiply(n) :
#     for i in range(1,10):
#         print(f'{n} x {i} = {n * i}')
#
# dan = int(input("몇 단을 출력하고 싶니 >>> "))
# multiply(dan)

'''
파이썬에 있는 특별한 연산자
** : 제곱
// : 몫 연산자

'''

# print(5%2) # 답 1
# print(5//2) # 답 2

def vending_machine(n):
    price = 700
    for i in range(n//price+1) :
        print(f'음료수 {i}개, 잔돈 = {n-i*price}')

vending_machine(600)

#