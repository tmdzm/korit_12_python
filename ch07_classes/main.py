'''
클래스 정의 형식 :

class 클래스명(파스칼케이스):
    본문(attribute / method)
객체 생성 형식 :
객체명 = 클래스명()
'''
# 클래스 정의 예시
class WaffleMachine:
    pass

waffle = WaffleMachine() # 객체생성
print(waffle)
'''
클래스의 구성

1. 클래스의 기본 구성
    객체를 만들어내는 클래스는 객체가 가져야 할 구성 요소를 지닌다.
    객체를 생성하기 위해서는 객체가 가져야 할 '값'과 '기능'을 지녀야 한다.
    
    값 = 속성(attribute)
    기능 = 메서드(method)
    
    클래스를 구성하는 속성은 두가지로 나뉜다.
        1) 클래스 변수 : 클ㄹ래스를 기반을로 생성된 모든 인스턴스들이 공유하는 변수
        2) 인스턴스 변수 : 인스턴스들이 개별적을로 가지는 변수
    메서드는 특징에 따라서
        1) 클래스 메서드
        2) 인스턴스 메서드
        3) 정적 메서드
        
    Java에서는 this 썻었는데(아직 정의 중인 클래스에 대한 객체가 생성될 수 없읜 임의로 this사용)
    python에서는 self
    
    self : 인스턴스 변수에서 각각의 객체를 의미하기 위해 self 키워드를 붙여준다.
    인스턴스 메서드에서의 첫번째 매개변수로 '항상' self를 추가해야 한다.(자동완성 지원)
'''

# 클래스 정의
class Person :
    # 메서드 정의
    def set_info(self, name, age,tel, address):
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address
        # 필드 선언을 미리 안해도 this(여기선 self)를 쓸 수 있다.
        # 파이썬에서 스스로 필드를 가진다고 인식하기 때문에
        # 저 밑에서 새로운 필드가 튀어나와도 오류가 안나기 때문에 짜증나는 구석이 있다.

    def show_info(self):
        print(f'이름 {self.name}')
        print(f'나이 {self.age}')
        print(f'연락처 {self.tel}')
        print(f'주소 {self.address}')

    def show_info2(self):
        pass # return으로 String 만들 생각이었름
person1 = Person()
# person2 = Person()
person1.set_info(age=20,tel='010-1234-5678',address='부산광역시 부산진구',name='김일')
person1.show_info()
# person1.show_info2()