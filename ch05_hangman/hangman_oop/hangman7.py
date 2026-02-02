import random
from hangman_arts import * # 전체 데이터
from hangman_word_list import words # words 변수만

def blank_reverse (str, ch):
    for i in range (len(str)):
        if chosen_word[i] == ch:
            str[i] = ch

chosen_word = random.choice(words)
print(logo)

display = []
for _ in chosen_word:
    display.append('_')

lifechecker = len(stages)-1
end_of_game = False
while not end_of_game :
    guess = input("알파벳을 입력해 >>> ").lower()
    blank_reverse(display, guess)
    print(' '.join(display))
    if guess not in chosen_word : # guess가 chosen_word에 있나 확인
        lifechecker -= 1
    print(stages[lifechecker])
    print(f"남은 기회 {lifechecker}회")
    if lifechecker == 0: # 목숨이 다 떨어졌으면 게임 끝
        print(f'You died')
        print(f'정답은 {chosen_word} 입니다.')
        end_of_game = True
    if '_' not in display : # 정답을 다 맞췄으면 게임 끝
        print("정답입니다 !!")
        end_of_game = True