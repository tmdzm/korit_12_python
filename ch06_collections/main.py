# #1
# place = set({})
# for i in range(3):
#     place.add(input("희망하는 수학여행지를 입력하세요 >>> "))
#
# print(f'조사된 여행지는 {place}')
# print(f'조사된 여행지는 {list(place)}')
#
# #2
# numbers = int(input("몇개의 숫자를 입력할까요 >>> "))
# number_list = []
# number_list_even = []
# for i in range(numbers):
#     number_list.append(input(f'{i+1}번째 숫자를 입력하시오 >>> '))
#     if int(number_list[i]) % 2 == 0:
#         number_list_even.append(number_list[i])
#
# print(f'입력 받은 숫자는 {number_list}')
# print(f'입력 받은 숫자들 중 짝수는  {number_list_even} 입니다.')

#3
humans = {}
for i in range(1,4):
    humans.setdefault((input(f'{i}번째 사람의 이름을 입력하세요 >>> ')),(input(f'{i}번째 사람의 연락처를 입력하세요 >>> ')))

print(f'입력 받은 연락처는 {humans}')

#4
def add_numbers1(lastnum) :
    for num in range(1, lastnum + 1) :
        numbers1.append(num)

def add_numbers2(lastnum):
    add_numbers1(lastnum)
    return numbers1

def add_numbers3(lastnum,li):
    for num in range(1, lastnum + 1):
        li.insert(num-1,num)

numbers1 = []
lastnum =  int(input('숫자 몇 까지 입력할래 >>> '))

add_numbers1(lastnum)
print(add_numbers2(lastnum))

hello = ['안', '녕', '하', '세', '요']
add_numbers3(lastnum,hello)
print(hello)