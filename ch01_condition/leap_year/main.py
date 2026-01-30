year = input('년도를 입력하시오. >>> ')
year = int(year)

if (year%4==0 and year%100!=0 or year%400==0):
    print('윤년')
else :
    print('평년')

