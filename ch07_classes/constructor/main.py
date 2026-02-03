'''
일종의 setter 같은 것을 이용해 속성값을 대입해 줬는데
field 선언을 하지 않고 method

객체 생성시 기본 생성자 호풀 -> set_info() 메소드 호풀해서 값 대입

AllArgsConstructor에 해당되는걸 python 에서 정의할 수 있지 않을까
'''

# 클래스 정의
class Candy :
    def set_info(self,shape,color) :
        self.shape = shape
        self.color = color

    def show_info(self) :
        print(f'사탕의 머양은 {self.shape}이고, 색깔은 {self.color}입니다.')


satang = Candy()
satang.set_info('구형','갈색')
satang.show_info()

'''
속성값에 대한 제한이 따로 있지 않다면 굳이 빈 객체 만들어놓고 거기에 대인하는 것이 비효율적으로 느껴진다.
그래서 AllaragsConstructor를 도입할거

Java / JS에서의 생성자 명은 클래스 명과 동일하거나 constructor를 쓰는데
python에선 __init__을 쓴다.

'''

class Candy2:
    def __init__(self,shape,color) :
        self.shape = shape
        self.color = color

    def show_info(self) :
        print(f'사탕의 머양은 {self.shape}이고, 색깔은 {self.color}입니다.')

satang2 = Candy2(shape='정육면체',color='흰색')
satang2.show_info()

'''
소멸자 , 디스트럭터
'''

class Sample:
    def __init__(self) :
        print('인스턴스 생성됨')
    def __del__(self) :
        print('인스턴스 소멸')

sample = Sample()
print()
del(sample) #객체 메모리를 날려야 하기 때문에 객체에 종속이 아니다.

'''
코드 다 돌아가면 객체가 소멸되는 것은 같은데 굳이 소멸ㄹ자를 학습하는 이유 -> 객체가 생성되면 메모리 공간을 차지하기 때문에
객체가 생성될 때마다 그곳에서 불려나오게 된다. 하지만 특정 객체가 일정 코드라인 이후로 전혀 사용되지 않을 때에도 여전히 메모리를 차지하기 때문에 소멸ㄹ자를 통해ㅐ서 강제로 객체를 삭제해주게 되면 메모리 관리가 된다고 볼 수 있다.

즉, 극단적인 메모리 관리를 위해 필요하다
'''

class USB :
    def __init__(self,capcity) :
        self.capcity = capcity
        print('USB객체가 생성되었습니다.')
    def get_info(self) :
        print(f'{self.capcity}GB USB')

usb = USB(64)
usb.get_info()

class Person :
    def __init__(self,name) :
        self.name = name
        print(f'{name} is born')
    def __del__(self) :
        print(f'{self.name} is dead')

man = Person('James')
woman = Person('emily')
del man