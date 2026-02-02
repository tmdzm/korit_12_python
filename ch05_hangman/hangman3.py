import random

def blank_reverse (str, ch):
    for i in range (len(str)):
        if chosen_word[i] == ch:
            str[i] = ch

word_list = ['apple','banana','camel']
chosen_word = random.choice(word_list)
print(f'테스트 단어 : {chosen_word}')

display = []
for _ in chosen_word:
    display.append('_')

'''
.join(반복가능객체) method : '.' 앞에 있는 문자열을 기준을로 반복 가능 객체의 element들을 합쳐서 str로 만들어주는 method
'''

temp = ['s','q','l','d']
test =''.join(temp)
print(test)
test ='/'.join(temp)
print(test)
test =' '.join(temp)
print(test)

full = False
while(not full) : # while '_' in display : 도 가능
    guess = input("알파벳을 입력해 >>> ").lower()
    blank_reverse(display, guess)
    print(' '.join(display))
    for _ in display:
        full = False if _ == '_' else True
        #
        # if _ == '_':
        #     full = False
        #     break
        # else :
        #     full = True

print("정답입니다") if full else print("오답입니다.")