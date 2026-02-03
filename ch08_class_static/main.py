'''
1. 클래스 변수 vs. 인스턴스 변수
    인스턴스 변수 : 인스턴스마다 서로 다른 값
    클래스 변수 : 모든 인스턴스가 동일한 값을 지니는 변수

    인스턴스 변수 접근 방식 - 인스턴스 접근(o) / 클래스 접근 x
    클래스 변수 접근 방식 - 인스턴스 접근 o / 클래스 접근 o

'''

# 클래스 변수 예시
class Korean:
    country = '한국'
    def __init__(self,name,age,address) :
        self.name = name
        self.age = age
        self.address = address

korean = Korean('김일',21,'마포구')
print(korean.country) # 객체명. 클래스 변수명
print(Korean.country) # 클래스명. 클래스 변수명으로 접근가능

'''
객체명.클래스 변수명을 통해서 클래스 변수에 접근이 가능하긴 한데, 클래스 내부 코드를 보기 전까지는 country라는 변수가 
인스턴스 변수인지 클래스 변수인지 알 방법이 없다.

그래서 클래스 변수를 확인하고자 할때는 클래스명.클래스변수명을 통해서 참조하는것이 권장된다.

2. 클래스 메서드
'''

class Korean2:
    country = '대한민국'
    #클래스 메서드의 정의 방법
    @classmethod    # @decorator를 달면 된다.
    def trip(cls,travelling_site): # cls는 class의 축약어
        if cls.country == travelling_site:
            print('국내 여행')
        else :
            print('해외 여행')

# 클래스 메서드 호출
Korean2.trip('대한민국')
Korean2.trip('미국')

person2 = Korean2()
person2.trip('일본') # 비권장, 객체명.클래스메서드()

'''
3. 정적 메서드
    정적 메서드 또한 self를 쓰지 않는다.
    즉, 인스턴스 변수에 접근하여 사용하는 것이 불가능함을 의미.
    self.속성명을 사용하여 인스턴스 변수의 값을 참조하는데 정적 ㅁ서드는 아예 첫번째 매개변수가 고정되어 있지 않다.
    인스턴스 변수를 참조하지 못한다는 점에서 클래스 메서드와의 공통점에 해당
    
    인스턴스를ㄹ 생성하징 낳아도 사용할ㄹ 수 있다 - 클래스 메서드와의 공통점 #2
    
특징 :
    1) 인스턴스 / 클래스로 호출 가능 -> 클래스 메서드와의 공통점
    2) 생성된 인스턴스가 없어도 호출 가능 -> 클래스 메서드와의 공통점
    
    3) @staticmethod 데코레이터를 표기하고 작성 -> 클래스 메서드와의 차이점 1
    4) 반드시 작성해야 하는 매개변수(self/cls)가 없음 -> 차이점 2
    
인스턴스 / 클래스 변수를 모두 사용하지 않는 메서드를 정의하는 경우에 적합하다.

즉, Java에서의 정적 메서드는 =
'''

class Korean3:
    country = '한국'

    @staticmethod
    def slogan():
        print('Imagine Your Korea!')

    @staticmethod
    def slogan2(str_example):
        print(f'Imagine Your Korea! {str_example}')

# static method 호출
Korean3.slogan()
Korean3.slogan2('겨울왕국')

#
#
#

class Bag :
    count = 0

    def __init__(self):
        Bag.count += 1 # cls.count가 아닌점에 주목, 왜?
        # 생성자는 인스턴스 메서드이기 때문에 인스턴스 메서드 내에서 클래스 변수를 참조할때는 cls.클래스 변수명이 아니라
        # 클래스명. 클래스명으로 참조해야한다는 점이 중요하다.

    #클래스 메서드 정의
    @classmethod
    def sell(cls):
        print('가방이 팔렸다.')
        cls.count -= 1 #이건 클래스 메서드니까 Bag.count가 아니라 cls.count

    @classmethod
    def remain_bag(cls):
        return cls.count

# 객체 생성
bag1 = Bag()
print(f'현재 가방 재고 : {Bag.count}')
# 인스턴스 메서드를 통해서 클래스 변수를 바꿨다. 그게 그다지도 중요한가
# 이 값은 모든 Bag 클래스의 인스턴스들이 공유한다는 점에서 정적 변수 개념과 동일하다

bag2 = Bag()
bag3 = Bag()
print(f'현재 가방 재고 : {Bag.count}')
bag1.sell() # 객체명.클래스메서드
print(f'현재 가방 재고 : {Bag.count}')

#
#1
class Person:
    population = 0
    def __init__(self,name) :
        self.name = name
        print(f'{name}이(가) 태어났습니다.')
        Person.population += 1

    def __del__(self) :
        print(f'{self.name} RIP')

    @classmethod
    def get_population(cls):
        return Person.population


man = Person('김일')
woman = Person('김이')
print(f'전체 인구수 : {Person.get_population()}')
print(f'전체 인구수 : {Person.population}')

del man