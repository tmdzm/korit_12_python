MENU = {
    '에스프레소' : {
        '재료' :{
            '물' : 50,
            '커피' : 18,
        },
        '가격' : 1.5,
    },
    '라떼' : {
        '재료' :{
            '물' : 200,
            '우유' : 150,
            '커피' : 24,
        },
        '가격' : 2.5,
    },
    '카푸치노' : {
        '재료' :{
            '물' : 250,
            '우유' : 100,
            '커피' : 24,
        },
        '가격' : 3.0,
    },
}

class CoffeeMachine:
    profit = 0 # 이거 내부의 profit인데 왜
    resources = {
        '물' : 300,
        '우유': 200,
        '커피': 100,
    }
    def esspresso(self):
        self.resources['물']-= MENU['에스프레소']['재료']['물']
        self.resources['커피'] -= MENU['에스프레소']['재료']['커피']
        self.profit += MENU['에스프레소']['가격']

    def cappuccino(self):
        self.resources['물']-= MENU['카푸치노']['재료']['물']
        self.resources['우유']-= MENU['카푸치노']['재료']['우유']
        self.resources['커피'] -= MENU['카푸치노']['재료']['커피']
        self.profit += MENU['카푸치노']['가격']

print(MENU['카푸치노']['가격'])
print(MENU['에스프레소']['재료']['물'])

coffee = CoffeeMachine()
# cofffe.esspresso()
# cofffe.esspresso()
coffee.cappuccino()

print(CoffeeMachine.resources)
print(coffee.profit)
# input("무엇을 드시겠습니까? (에스프레소/라떼/카푸치노): ")
