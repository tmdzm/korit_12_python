'''
for 반복문 :
원래 python에서의 default for문의 경우 enhanced for가 기본이다.(걍 for each가 기본이라는것)

range() 함수가 중요하다
'''

#1~10을 foransdmfh

for i in range(10):
    print(i+1)

'''
i는 0부터 시작, range()는 몇번 반복할지 지정하는 함수. 특히 for문과 연계되어 함께 쓰인다
range() 함수의 응용
range((시작값), 한계값, (증감값))

시작값 : 생략 가능, 생략하면 0부터 시작
한계값 : 명시하지 않으면 끝까지 진행
증감값 : 생략가능, 생략하면 1씩 증가
'''

for i in range(2, 11, 2):
    print(i, end=' ')
print()
print(i) # 결과값 : 10
'''
Java에서는 for(int i = 0...) 어쩌고 한 부분이 있을 때
sout(i)하면 오류가 났었다.
while에서와 마찬가지로 지역 변수의 범위가 다르다.

하지만 range()함수는 for의 default 함수가 아니다.
default 형태는
for 변수명 in iterable(반복가능객체):
    반복실행문
이다.
'''

nums = [1,2,3,4,5]
for i in nums:
    print(i, end=' ')

if 5 in nums:
    print('5가 nums 리스트 내에 있다.')
else :
    print('5가 nums 리스트 내에 없다.')

'''
그러면 Java를 배운 우리와 익숙하지 않지만 in이라는 애가 생각보다 엄청 중요하다.
in이 적용된 무언가의 결과값의 자료형은 무엇인가?
-> True / False가 나오는 '연산자'
A in B라고 했을 때 A라는 요소가 B라는 반복가능 객체 내에 존재하는 지를 True / False로 뽑아주게된다.
'''

print(5 in nums) # 결과값 True