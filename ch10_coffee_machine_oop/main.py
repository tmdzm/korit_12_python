from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 기본 생성자를 통한 객체 생성
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

print(menu.get_items())

is_on = True

# print(menu.menu[1]) # espresso라는 스트링을 뽑아내려면?, 당장엔 <menu.MenuItem object at 0x0000021A477F8F50>가 출력
# print(menu.menu[1].name)
while is_on:
    choice = input(f'어떤 음료를 먹을래 ? {menu.get_items()} >>> ')
    if choice == '정산' :
        coffee_maker.report()
        money_machine.report()
    elif choice == '정지' :
        print('자판기가 종료됩니다.')
        is_on = False
    elif choice == '재고보충' :
        coffee_maker.restock()
        coffee_maker.report()
    else :
        drink = menu.find_drink(choice)
        if drink is not None:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)

# 가능한 확장, 메뉴를 번호순으로 출력해서 해당 번호를 입력해도 메뉴가 나오게 한다.
# 음료를 시킬때 중복해서 계산을 하게 한다.
# 머신안에 잔돈이 부족할 경우 계산 불가능하게 하기
# 영수증?