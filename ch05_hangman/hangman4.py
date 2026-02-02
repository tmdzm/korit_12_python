import random

def blank_reverse (str, ch):
    for i in range (len(str)):
        if chosen_word[i] == ch:
            str[i] = ch

def checker (str, ch):
    for i in range (len(str)):
        if str[i] == ch:
            return True
    return False

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["apple", "dream", "river", "bright", "window", "journey", "quiet", "forest", "smile", "cloud"
]
chosen_word = random.choice(word_list)
# print(f'테스트 단어 : {chosen_word}')

display = []
for _ in chosen_word:
    display.append('_')

full = False
lifechecker = len(stages)-1
print(stages[lifechecker])

end_of_game = False
while not end_of_game : # while '_' in display : 도 가능
    guess = input("알파벳을 입력해 >>> ").lower()
    blank_reverse(display, guess)
    print(' '.join(display))
    for _ in display:
         if _ == '_' :
            full = False
            break
         else :
             full = True
    if not checker(display, guess) : # guess가 chosen_word에 있나 확인
        lifechecker -= 1
    print(stages[lifechecker])
    print(f"남은 기회 {lifechecker}회")
    if lifechecker == 0: # 목숨이 다 떨어졌으면 게임 끝
        end_of_game = True
        print(f'정답은 {chosen_word} 입니다.')
    if full : # 정답을 다 맞췄으면 게임 끝 , if '_' not in display : 와 같다.
        break # 아님 end_of_game = True하던가

print("정답입니다 !!") if full else print("오답입니다.")