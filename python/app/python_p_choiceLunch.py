import random
import time

lunch = ['아버지 폰', '어머니 폰', '쓰던폰']
print('기본 메뉴', lunch)
while True:
    item = input('메뉴 추가 (넘기기: q 입력): ')
    if item == 'q' or item == 'Q' or item == 'ㅂ':
        break
    else:
        lunch.append(item)

set_lunch = set(lunch)
print('메뉴선정 완료!!')
print(set_lunch)
print('=========================')


while True:
    item = input('메뉴 삭제 (넘기기: q 입력): ')
    if item == 'q' or item == 'Q' or item == 'ㅂ':
        break
    else:
        set_lunch = set_lunch - set([item])

print('=========================')
print(set_lunch, '에서 선택합니다.')
time.sleep(3)
for i in range(5):
    print(5-i)
    time.sleep(1)

print('건희 휴대폰은', random.choice(list(set_lunch)), '입니다 :) ')
