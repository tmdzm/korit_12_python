'''
상속

형식 :
class 슈퍼 클래스 :
    본문

class 서브 클래스(슈퍼클래스)
    본문

'''
import math


class Person:
    def __init__(self, name):
        self.name = name

    def eat(self,food):
        print(f'{self.name}이(가) {food}을(를) 먹는다.')

    def drink(self,bever):
        print(f'{self.name}이(가) {bever}을(를) 마신다.')

person = Person('김')
person.eat('감자')

class Student(Person):
    def __init__(self,name,school):
        super().__init__(name) # 상속받는 클래스에 있는 필드(?) 이게 필드가 맞나
        self.school = school # 자식 혼자 가진것

    def study(self):
        print(f'{self.name}은(는) {self.school}에서 공부한다.')

    def drink(self,bever): #오버라이딩
        print(f'{self.school}에서',end=' ')
        super().drink(bever)

potter = Student(name='해리포터',school='호그와트')
potter.study()
potter.eat('초콜릿 개구리') # 부모의 메서드를 정의 없이 사용가능
potter.drink('버터맥주')

'''
1. 서브 클래스의 __init__()
    Java와 마찬가지로 서브 클래스는 슈퍼 클래스가 없으면 존재할 수 없다.
    그래서 서브 클래스의 생성잘를 구현할 때는 '반드시 슈포 클래스의 생성자를ㄹ 먼저 호출'
    하는 코들를 작성해야한다.
    
    super() 슈퍼 클래스의 생성자
    potter = Student()에서 보면 알 수 있듯이.
    그러면 슈퍼 클래스의 객체가 .__init__(name)이라는 메서드를 호출했다고 해석가능
    즉, 이상의 코드에서 Student 생성자의 호출이 완벽하게 마무리 되려면 super().__init__(name)에 의해서
    슈퍼 클래스인 Person의 생성자가 먼저 호출이 완료되고
    Person 클래스의 인스턴스가 생성된다. 이후에 슈퍼 클래스의 인스턴스 변수인 name이 서브 클래스로 전달되고
    그 다음 서브 클래스에서 school 인스턴스 변수를 선언 및 초기화하여 서브 클래스의 인스턴스가 생성됨
    
    : 생성자를 호출했다면 -> 객체가 생성되었다고 볼 수 있는데 -> 그렇다면 부모 클래스의 인스턴스와 자식 클래스의 인스턴스가
    있는거 아니냐 -> 맞긴한데 그러면 별개의 인스턴스라고 봐야 하냐면 그게 좀 애매하다.
    
    Java에서는 super() -> 이건 생성자 / super.메서드명()으로 super 자체가 객체인 경우가 있지만
    python에서는 super()로 일원화 되어 있다.
    
2. 서브 클래스의 인스턴스 자료형
    슈퍼 클래스의 객체는 슈퍼 클래스의 인스턴스
    서브 클래스의 인스턴스는 서브 클래스의 인스턴스이면서 동시에 슈퍼 클래스의 인스턴스
    Student 클래스의 객체는 Student의 인스턴스이면서 Person의 인스턴스
    
    Java를 기준으로 instanceof 연산자 역할을 하는것이 Js에선 typeof연산자
    python에선 isinstance()함수가 있다.
    
형식 :
isinstance(객체명, 클래스명) -> boolean

'''

print(isinstance(potter,Student))
print(isinstance(potter,Person))
print(isinstance(person,Student)) # 혼자 False
print(isinstance(person,Person))

print(issubclass(Person,Student)) # 객체 생성 안하고 클래스간의 위계확인 가능, True

#
#

class Car:
    max_oil = 50
    def __init__(self,oil):
        self.oil = oil
        print('새 차를 뽑았습니다.')
    def add_oil(self,oil):
        if oil <= 0 :
            return
        self.oil += oil
        if self.oil > Car.max_oil :
            self.oil = Car.max_oil
        print(f'기름을 {self.oil} 주유 했습니다.')
    def car_info(self):
        print(f'현재 주유 상태 : {self.oil}')

class Hybrid(Car):
    def __init__(self,oil,amount):
        super().__init__(oil)
        self.amount = amount
        print(f'하이브드 차량을 뽑았습니다. 부릉부릉')

    def __del__(self):
        print('폐차되었습니다.')

    def charge(self,amount):
        if amount <= 0:
            return
        self.amount += amount
        if self.amount > 30 :
            self.amount = 30
        print(f'전기를 {self.amount} 충전 했습니다.')

    def hybrid_info(self):
        super().car_info()
        print(f'현재 충전 상태 : {self.amount}')


car = Hybrid(oil= 0, amount= 0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()

##
##
class Shape() :
    def __init__(self,name):
        self.name = name

    def draw(self):
        print(f'{self.name}이 생성되었습니다.')

class Circle(Shape):
    def __init__(self,name,radius):
        super().__init__(name)
        self.radius = radius
        print(f'반지름이 {radius}인',end=' ')
        super().draw()

    def area(self):
        return 3.14*self.radius**2

    def draw(self):
        extent = round(self.area(),2)#round(extent,2)는 안된다.
        print(f'이름이 {self.name}인 원의 넓이는 {extent} 입니다.')#extent.2f

class Rectangle(Shape):
    def __init__(self,name,width,height):
        super().__init__(name)
        self.width = width
        self.height = height
        print(f'너비가 {width}, 높이가 {height} 인',end=' ')
        super().draw()

    def area(self):
        return self.width*self.height

    def draw(self):
        extent = self.area()
        print(f'이름이 {self.name}인 직사각형의 넓이는 {extent} 입니다.')


circle = Circle('원1', 5)
circle.draw()
print(f'원의 넓이 : {circle.area()}')

rectangle = Rectangle('직사각형1', 10, 8)
rectangle.draw()
print(f'직사각형의 넓이: {rectangle.area()}')

circle = Circle('원2', 1)
circle.draw()