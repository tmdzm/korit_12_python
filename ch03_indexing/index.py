str_exmaple = 'Hello World!'
print(str_exmaple[0])
print(str_exmaple[1])
print(str_exmaple[2])
print(str_exmaple[3])
print(str_exmaple[4])
print(str_exmaple[5])
print(str_exmaple[6])

print(len(str_exmaple)) # 결과값 : 14
# 일반 for문으로 Hello, Python!을 한줄로 출력하시오.
'''
len() : 반복가능 객체의 전체 인덱스 값을 ㄹreturn하는 함수
'''

for i in range(len(str_exmaple)):
    print(str_exmaple[i], end='')

print()

for j in str_exmaple:
    print(j, end='')

'''
마이너스 인덱스 : 문자열의 뒤에서부터 부여하는 번호
-1은 맨 마지막 데이터의 인덱스 위치

문자열 슬라이싱(slice) : 문자열의 인덱스를 활용하여 한 문자 이상으로 구성된 단어나 문장을 추출할 때 사용하는 방법
    추출하고자 하는 단어나 문장의 시작 인덱스와 종료를 통해 그 사이 문자들을 추출하는 것이 가능함.
    
형식 :
변수명[ 시작 인덱스: 종료인덱스 : 증감값]
시작인덱스 : 생략하면 처음부터 추출
종료인덱스 : 새약하면 끝까지 추출ㄹ
증감값 : 생략하면 1씩 증가
'''

print()
print(str_exmaple[:-1:])
# 시작지점 0번지부터 뒤에서 3번째 인덱스 미만까지 출력

'''
range()와 변수명[]의 경우 
range는 ,
변수명은 : 로 쓴다.
함수냐 아니냐의 차이다.
'''
four = False
while(not four) :
    num = input("네 자리 숫자를 입력해 >>> ")
    if len(num) == 4 :
        four = True
    else :
        print('네 자리 숫자가 아닙니다')

print(f'맨 마지막 숫자는 {num[-1]}입니다.')

if(int(num[-1])%2 == 0 ):
    print(f'맨 마지막 숫자는 {num[-1]}이며 짝수입니다.')
else :
    print(f'맨 마지막 숫자는 {num[-1]}이며 홀수입니다.')

'''
파이썬 삼항 연산자
if - else 구조를 한줄로 줄여 쓴다.
'''
# result = int(num[-1]) % 2 == 0 ? '짝수' : '홀수'
result = '짝수' if int(num[-1]) % 2 == 0 else '홀수'

print(f'맨 마지막 숫자는 {num[-1]}이며 {result}입니다.')