
orders = ['짜장', '짬뽕', '탕수육']

# list Add
orders.append('냉면')
print(orders)

orders.insert(1, '깐풍기')
print(orders)

# list delete
del orders[0]
print(orders)

orders.remove('탕수육')
print(orders)

# list length
print(len(orders))

name = '안녕하세요. 코드라이언으로 코딩을 배우고 있습니다.'
print(len(name))
print(len(orders))
