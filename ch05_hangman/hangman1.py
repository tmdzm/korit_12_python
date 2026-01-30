import random
numbers = [1,2,3,4,5]
chosen_number = random.choice(numbers)
# random이라는 객체같은 것에 choice라는 메서드가 있고, 내부에 list 자료형을 넣으면 하나를 뽑아서 변수에 저장하는가 보다.
# print(chosen_number)

def check(g , w) :
    for i in range(len(w)):
        if w[i] == g :
            print(f'정답')
        else :
            print(f'오답')


word_list = ['apple','banana','camel']
# todo - 1 : word_list에서 하나의 단어를 임의로 선택하도록 random 모듈을 사용, chosen_word에 담는다.
# todo - 2 : 사용자에게 알파벳 하나를 입력하라 요청후 guess 변수에 담아라. .lower로 대문자 방지
# todo - 3 : guess가 chosen_word의 문자열중 하나가 맞는지 확인하고 정답 /오답 출력하게 하기

chosen_word = random.choice(word_list)
guess = input("아무 알파벳을 입력해라 >>> ").lower()
check(guess , chosen_word)

