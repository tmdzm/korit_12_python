'''
python 대표 collection 종류
1. list : 추가 / 수정 / 삭제가 언제나 가능하고 순서가 있음
2. tuple : 추가 / 수정 / 삭제 불가, 순서 있음
3. set : 중복된 값의 저장 불가 / 순서 없음
4. dict , 딕셔너리 : 키 + 값을로 관리

'''
from pickletools import read_stringnl_noescape

list_example = [30,40,'감',[100,'게']]
print(list_example)
tuple_example = (10,20,30,'흉참')
print(tuple_example)
set_example = [100,200,300,'4']
print(set_example) # 순서가 지 맘대로
dict_example = {'이름':'김일','나이':155,'학교':'성균관'}
print(dict_example)

'''
1. list : 자료형이 달라도 저장 가능 . jva기준 하나의 배열에 하나의 자료형
'''

# list의 선언 및 초기화
li1 = [1,2,3,'김사']
'''
    1.1 list의 index /slice
    list는 str과 동일한 방식의 index / slicing을 지원
    1) 인덱스 / 마이너스
'''

print(li1[0])
print(li1[1])
print(li1[2])
print(li1[3])
print(li1[-1])
print(li1[-2])
print(li1[-3])

'''
    2) slicing
        str의 slicing과 같이 '시작 인덱스 : 종료 : 증감값' 으로 이루어져 있다.
'''

li2 = [100,3.14,'hello'] # 선언및 초기화하는 2가지 방법
li3 = list([4,5,6,7,8,9,0])
# li4 = list((4,5,6,7,8,9,0)) # truple을 list로 형변환 가능

print(li3[0:4:2]) # 4와 6, 8이 4번지

'''
    3) list의 element 추가와 삭제
    list에 새로운 요소를 추가할 때는 아까 한 것처럼 .append()를 사용
    .insert()도 존재
    
    .append() - 항상 마지막 인덱스에 element를 추가
    .insert(위치, 값) - 정해진 위치에 해당값 추가
'''

scores = [30,40,50]
scores.insert(0,100) # 0번지에 100을 넣어서, 30은 1번지로 밀린다.

'''
    .pop()의 경우 NoArgs라면 맨마지막 element가 삭제된다.
    .pop(인덱스 넘버)로 작성하면 해당 인덱스의 마지막 element를 삭제한다.
        이건 그...다차원 배열 기준인가
'''

# scores.pop() # 가장 마지막
scores.pop(1) # 해당 인덱스


'''
    .remove(값) - list 내에 해당값을 찾아내서 삭제함
'''
print(scores.remove(50)) # 결과값 None, 이미 삭제했으니 삭제한걸 알려주질 않는다.
#scores.remove(300) # 없는값을 삭제하려 하면 에러난다.
print(scores)

# li4 = [1,2,3,4,5,6,7,8,9,10]
li4=[]
for n in range(1,11):
    li4.append(n)

for i in range(len(li4)):
    li4[i] *= 2

tmp = 0
for j in li4:
    li4[tmp] = j*2
    tmp += 1

print(li4)
print()
modified_li4 = map(lambda num: num*2, li4)#map은 파이썬에서 함수임
# 이상의 경우가 극단적으로 list의 내부 각각의 element들에 동일한 함수를 적용한 결과를 적용하는 map()함수 이다.
# 그런데 JS에서 method로 사용했었다. 이상의 코드가 좀 문제가 있다면 map()함수의 결과값이 map객체에 해당하기 때문에 list()함수를 통한 형변환을 해줘야 한다.
print(modified_li4)
'''
    2. tuple(튜플) : 저장된 값을 변경할 수 없는 list라고 생각하면 된다.
    순서는 있기때문에 index넘버 사용과 slice는 가능 추가 / 삭제 / 수정 불가
'''

tu1 = (1,2,3) # 튜플 생성 방법 # 1
tu2 = tuple((4,5,6)) #2
tu3 = 7,8,9 # 3

a, b, c = 7, 8, 9 #복수의 변수 선언 및 초기화 방법
# 알아서 순서대로 대입

print(type(tu3)) # class tuple

tu5 = 'hello',' good morning',' my name is',' kim-il',' i am',' 20',' years old'

for word in tu5:
    print(word.title(), end='')
    # Hello Good Morning My Name Is Kim-Il I Am 20 Years Old
    # 20이 숫자면 에러가 난다. .title()때문인가
print()

'''
collection의 개념과  내부 element의 자료형이 서로 다르다.
tuple자체는 추가 / 수정 / 삭제가 불가능 했으나
내부 element 자체는 str이니까 데이터의 가공이 가능하다.

    3. set 세트
        : 수학의 집합 개념, Java와 동일
'''
set1 = {1,2,3}
set2 = set({4,5,6})

li = []
tu = ()
se = {} # 얘는 set가 아니라 빈 딕셔너리가 만들어진다.
se1 = set({}) # 빈 딕셔너리는 이걸로만 만들 수 있다.

'''
list / tuple은 index가 존재한다. 그래서 이렇게 인덱스가 존재하는걸 sequence로 분류한다.
set / dictionary는 인덱스가 없어서 비시퀀스라는 표현을 쓰기도 한다.
    
    set 관련 메서드
    1. .add() - set에 새로운 element 추가
    2. .remove() - 기존 element 삭제 -> 인덱스가 없어서 .pop()이 없다., 없는 숫자면 오류
    3. .discard() - 기존 element 삭제 -> 없는 숫자라도 오류 안남

'''

se3 = {10,20,30}
se3.add(50)
print(se3)
# se3.remove(70) # 없으면 오류, 즉 정확히 날려야하는 숫자가 있다면 사용
# print(se3)
se3.discard(70) #이건 오류 발생 안함, 있는지 없는지 모르지만 날리고 싶은 숫잘라면
print(se3)

for num in se3:
    print(num)

'''
    4. dict - Java에서의 Map / Js에서의 Object / JSon과 비슷한 형식
'''
dict1 = {
    '이름' : '김일',
    '나이' : 20,
    '주소' : ['서울특별시','마포구','목동'],
}
'''
나중에  학교라는 key를 추가하려고 할ㄸ, 167번 라인에 콤마 + 엔터 '학교' : '코리아 아이티같은 식으로 
추가하기 번거로우니까 나중에 확장성을 위해서 미리 콤마쳐두는 편이다.
그러면 다음 라인에 추가 property를 넣으면 된다.

정말 중요하게 반복적으로 말하는 부분
dictonary에서 반복문 돌ㄹ리면 key가 나온다.
'''

for key in dict1:
    print(key)

# 그렇다면 value를 확인하기 위해서는
for key in dict1 :
    print(dict1[key])

# key들만 추출하는 메서드
print(dict1.keys())
print(type(dict1.keys())) # 결과값 : <class 'dict_keys'>
print(list(dict1.keys())) # 결과값 : ['이름','나이','주소']

print(dict1.values())
print(type(dict1.values())) # 결과값 : class 'dict_values'

# key들 혹은 value들만 뽑아서 list를ㄹ 만들고 싶다면 list()형변환 함수를 사용하여야 한다.

'''
그래서 collections 수업을 할 때 매우 중요한 점은 list를 배웠을 때 list만 고려할 것이 아니라 set/tuple/dictionary로 자료형을 변경하는것이 가능한가
    1) dictionary에서 property 추가/ 삭제
'''

dict1['직업'] = '웹 퍼블리셔'
dict1['직업'] = '웹 개발자'
print(dict1)
# 키가 동일하면 최근 값으로 덮어 써진다.

print(dict1.pop('직업')) # 키를 알아야 삭제 가능
# .pop은 remove와 달리 삭제되는 값이 추력된다.

list = []
for i in range(10,110,10):
    list.append(i)

print(f'3번째에서 7번째 {list[2:7]}')
# list = list[2:7:]

print(f'3번째에서 7번째 {list[2:7][1]}')

month = int(input("1~12사이의 월을 입력 >>> "))
list_day = [31,28,31,30,31,30,31,31,30,31,30,31]
print(f'{month}월은 {list_day[month-1]}일 까지입니다.')

# 3
list_day2 = [28,30,31]
if month == 2 :
    print(f'{month}월은 {list_day2[0]}일 까지입니다.')
elif month%2 == 1 and month < 8 or month%2 == 0 and month >= 8 :
    print(f'{month}월은 {list_day2[2]}일 까지입니다.')
elif month in [4,6,9,11] :
    print(f'{month}월은 {list_day2[1]}일 까지입니다.')

