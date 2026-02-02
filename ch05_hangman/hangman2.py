import random

word_list = ['apple','banana','camel']
chosen_word = random.choice(word_list)
print(f'테스트 단어 : {chosen_word}')

def blank_reverse (str, ch):
    exist = False
    for i in range (len(str)):
        if chosen_word[i] == ch:
            str[i] = ch
            exist = True
    return exist

# todo - 1 : 비어있는 list인 display를 만들어라
display = []
# list에 element를 추가하는 메서드 : .append()
# display.append('김')
# display.append('영')
# print(display)
# display[1] = 1 # 처음엔 몇번지인지 없기때문에 즉, 인덱스가 없기때문에 '추가'는 안되지만
# print(display) # 이미 있는 장소에 element를 바꿀 수 있다.

# todo - 2 : chosen_word의 각 문자 개수마다 '_'를 추가하라
# todo - 3 : guess가 맞다 면 출력을 바꿀것

for ch in chosen_word:
    display.append('_') # 구태여 def로 둘 이유를 몰르겠다.

for i in range(5):
    guess = input("알파벳을 입력해 >>> ").lower()
    if blank_reverse(display, guess) :
        i -= 1
    print(i)
    print(display)