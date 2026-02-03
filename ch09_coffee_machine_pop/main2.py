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

resources = {
        '물' : 300,
        '우유': 200,
        '커피': 100,
    }

profit = 0.0

def report():
    print(f'물 : {resources['물']}ml')
    print(f'우유 : {resources['우유']}ml')
    print(f'커피 : {resources['커피']}g')
    print(f'돈 : ${profit}')

def is_resource_enough(order) :
    for i in MENU[order]['재료']:
        if resources[i] < MENU[order]['재료'][i]:
            print(f'{i}이(가) 모자랍니다.')
            return False
    return True

def process_coins():
    '''
    동전을 입력받아 전체 금액을 반환하는 함수 call3
    :return:
    '''
    total = 0

    total += int(input("쿼터 몇개? ")) * 0.25
    total += int(input("다임 몇개? ")) * 0.10
    total += int(input("니켈 몇개? ")) * 0.05
    total += int(input("페니 몇개? ")) * 0.01

    return total

def is_transaction_successful(push,need) :
    change = round(push-need,2)
    if push < need:
        print('돈이 부족합니다.')
        print(f'${push}를 반환합니다.')
        return False
    elif push > need:
        print(f'${change}를 반환합니다.')
        return True
    else :
        print('잔돈은 없습니다.')
        return True

def make_coffee(li):
    global profit # 함수 내에서 전역 변수의 값을 바꾸는것이 바람직 하지 않아서 제한을 걸어뒀다.
    for i in li:
        resources[i] -= li[i]
    profit += MENU[choice]['가격']

is_on = True

while is_on:
    choice = input("무엇을 드시겠습니까? (에스프레소/라떼/카푸치노): ")#.lower
    if choice == 'off':
        print('자판기가 종료되었습니다.')
        is_on = False
    elif choice == 'report':
        report()
    elif choice in ['에스프레소','라떼','카푸치노']:
        drink = MENU[choice]
        if is_resource_enough(choice) :
            money_received = process_coins() # 코인 여러개 받는 함수
            if is_transaction_successful(money_received,drink['가격']) :
                make_coffee(drink['재료'])
    else:
        print('잘못입력하셨습니다.')