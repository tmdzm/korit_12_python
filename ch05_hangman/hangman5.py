import random

def blank_reverse (str, ch):
    for i in range (len(str)):
        if chosen_word[i] == ch:
            str[i] = ch

logo = '''
 .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .-----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  ____  ____  | || |      __      | || | ____  _____  | || |    ______    | || | ____    ____ | || |      __      | || | ____  _____  | |
| | |_   ||   _| | || |     /  \     | || ||_   \|_   _| | || |  .' ___  |   | || ||_   \  /   _|| || |     /  \     | || ||_   \|_   _| | |
| |   | |__| |   | || |    / /\ \    | || |  |   \ | |   | || | / .'   \_|   | || |  |   \/   |  | || |    / /\ \    | || |  |   \ | |   | |
| |   |  __  |   | || |   / ____ \   | || |  | |\ \| |   | || | | |    ____  | || |  | |\  /| |  | || |   / ____ \   | || |  | |\ \| |   | |
| |  _| |  | |_  | || | _/ /    \ \_ | || | _| |_\   |_  | || | \ `.___]  _| | || | _| |_\/_| |_ | || | _/ /    \ \_ | || | _| |_\   |_  | |
| | |____||____| | || ||____|  |____|| || ||_____|\____| | || |  `._____.'   | || ||_____||_____|| || ||____|  |____|| || ||_____|\____| | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
'''

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

words = ["apple","river","dream","cloud","stone","light","shadow","forest","ocean","wind","fire","earth","sky","star","moon","sun","rain","snow","storm","wave","sand","leaf","tree","grass","flower","seed","root","branch","mountain","valley","hill","field","path","road","bridge","gate","door","window","wall","roof","floor","room","house","home","city","town","village","street","corner","market","shop","store","school","class","book","page","word","letter","story","poem","song","sound","voice","echo","music","rhythm","beat","note","tone","color","shape","form","line","point","space","time","moment","second","minute","hour","day","night","morning","evening","season","year","past","present","future","memory","thought","idea","mind","brain","heart","soul","spirit","emotion","feeling","joy","smile","laugh","tear","cry","fear","hope","love","trust","peace","anger","pride","shame","guilt","calm","focus","energy","power","strength","skill","talent","effort","work","task","goal","plan","dream","vision","chance","choice","option","risk","luck","fate","path","journey","travel","trip","move","step","walk","run","jump","climb","fall","rise","grow","build","create","make","break","fix","change","shift","turn","start","begin","end","finish","close","open","enter","exit","reach","hold","grab","touch","feel","see","look","watch","hear","listen","speak","say","tell","ask","answer","learn","teach","study","read","write","draw","paint","design","code","build","test","debug","deploy","launch","update","upgrade","system","network","signal","data","input","output","process","thread","memory","storage","cache","buffer","queue","stack","array","list","map","set","node","tree","graph","edge","vertex","loop","branch","return","break","continue","error","bug","issue","fix","patch","version","release","commit","merge","clone","fork","push","pull","repo","server","client","request","response","packet","socket","port","protocol","secure","encrypt","decrypt","hash","token","key","secret","login","logout","session","cookie","cache","timeout","retry","limit","quota","usage","metric","log","trace","monitor","alert","backup","restore","recover","fail","crash","reboot","restart","shutdown","power","battery","charge","current","voltage","signal","noise","filter","amplify","reduce","compress","expand","scale","resize","rotate","flip","mirror","blend","mask","layer","pixel","vector","render","export","import","format","encode","decode","stream","buffer","frame","rate","speed","delay","pause","resume","sync","async","thread","process","task","job","queue","worker","pool","load","stress","test","bench","score","rank","level","stage","phase","mode","state","status","flag","option","config","setting","profile","theme","style","layout","grid","flex","block","inline","margin","padding","border","radius","shadow","font","size","weight","color","contrast","bright","dark","light","soft","hard","smooth","rough","sharp","dull","clean","dirty","simple","complex","basic","advanced","expert","novice","beginner","master","leader","member","team","group","crowd","people","person","human","friend","enemy","stranger","partner","owner","user","admin","guest","role","rule","policy","law","order","chaos","system","pattern","random","noise","signal","meaning","value","truth","fact","logic","reason","proof","claim","argument","debate","talk","chat","message","email","letter","note","memo","draft","final"]

chosen_word = random.choice(words)

display = []
for _ in chosen_word:
    display.append('_')

lifechecker = len(stages)-1
print(logo)

end_of_game = False
while not end_of_game : # while '_' in display : 도 가능
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