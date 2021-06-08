import random
import time

gachaBox = []
itemName = input('상품을 입력하세요: ')
percent = int(input('확률을 입력하세요: '))
# money = int(input('뽑기 금액을 입력하세요'))
boom = 100 - percent

for i in range(percent):
    gachaBox.append(itemName)

for i in range(boom):
    gachaBox.append('꽝')

time.sleep(2)
print(itemName, '뽑기를 시작합니다.')
time.sleep(2)
print('확률은', percent, '퍼센트 입니다.')
time.sleep(2)
print('그럼 뽑기를 시~~작 합니다! 렛츠 기릿!!!!!!')
time.sleep(2)
for i in range(5):
    print(5-i)
    time.sleep(1)

print('뽑기 결과는!!!!!!!!!!!!!')
time.sleep(2)
print(random.choice(gachaBox), '입니다!')


# while True:
#     item = input('상품 추가 (넘기기: q 입력): ')
#     if item == 'q' or item == 'Q' or item == 'ㅂ':
#         break
#     else:
#         gachaBox.append(item)

# set_lunch = set(lunch)
# print('메뉴선정 완료!!')
# print(set_lunch)
# print('=========================')


# while True:
#     item = input('메뉴 삭제 (넘기기: q 입력): ')
#     if item == 'q' or item == 'Q' or item == 'ㅂ':
#         break
#     else:
#         set_lunch = set_lunch - set([item])

# print('=========================')
# print(set_lunch, '에서 선택합니다.')
# time.sleep(3)
# for i in range(5):
#     print(5-i)
#     time.sleep(1)

# print('건희 휴대폰은', random.choice(list(set_lunch)), '입니다 :) ')
