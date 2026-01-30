'''
1. if문
2. if-else문
    - 참고로 True / False로 대문자를 써야한다.
3. if - elif - else문
'''

# age = int(input('나이를 입력하세요 >>> '))
# if age > 20:
#     print('성인')
# elif age <= 20 and age > 13:
#     print('미자')
# else :
#     print('유아')

'''
if문의 전체 형식 :

if 조건식 1 :
    실행문 1
(elif 조건식 2~n:)
    (실행문 2~n)
else :
    실행문 n+1

Nested - if문 (중첩 if문)도 가능
'''

age = 21
has_ticket = True
print(type(has_ticket)) # class bool
if age >= 19:
    if has_ticket:
        print('입장가능')
    else:
        print('표를 사')
else:
    print('미자는 출입금지')

'''
비교 연산자
동일

논리 연산자
    1) and : &&
    2) or  : ||
    3) not : !와 같다. 근데 not=은 없고 !=가 있다.
'''
