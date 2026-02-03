class Student :
    def __init__(self,name,student_id) : #_를 생각할것
        self._name = name
        self._student_id = student_id
        # 성적을 저장하기 위한 빈 딕셔너리
        self._grades = {}

    # python 버전의 getter에 해당하는 메서드 정의 방식
    @property
    def name(self) :
        return self._name

    # python버전의 setter의 예시
    @name.setter
    def name(self,value) :
        self._name = value

# 객체 생성
student1 = Student('김일',2026001)
#getter의 호출 - 주의 사항 : 객체명.속성명도 아니고 객체명.메서드명() - 소괄호가 없다.
print(f'학생 이름 : {student1.name}')

#setter 호출
student1.name = '김영'
print(f'변경된 학생 이름 : {student1.name}')
print(student1._name) # 여전히 이거로도 부를 수 있다.

'''
이상의 코드에서 확인 가능한 점은 Java 기준으로  python 코드를 해석할 때 의문스러운 점이 많다.

1. _name일라는 속성이 있는데 객체명.name을 통해서 '김일'/'김영' 이라는 속성값이 출력된다는 점
    동시에 - 객체명._name도 작동한다는 점
2. 객체명._name = '김영'이 아니라 객체명.name =  '김영'으로 재대입한 것처럼 보이지 
    setter의 호출로 보이지 않는다.
    객체명.set_name('김영')이어야 하지 않나하는것
    
하지만 파이썬 내부에선 _name / name을 동일한 속성으로 처리한다.
객체명.속성명이면 getter로 처리하고 '객채명.속성명 = 데이터'면 알아서 setter로 처리해준다.
그 '알아서' 처리하기위한 작업이 @property와 '속성명.setter'라는 데코레이터 때문

원래는 이거 자동생성되기 때문에 @같은거 쓸 필요가 없는데
backend를 파이썬으로 짜지 않기 때문에 현재 쓸모가 없다.
python으로 백엔드 작성할때 의미가 있다는것만 알아두자

'''