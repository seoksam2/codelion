foods = ["된장찌개", "피자", "제육볶음"]
foods.append("김밥")
del foods[0]
print('====food list====')
for x in foods:
    print(x)

information = {"고향": "수원", "취미": "영화관람", "잘먹는 음식": "국수"}
information['특기'] = '게임'

print('====information get====')
print(information.get('고향'))
print(information['특기'])

print('====information for all====')
for i in information:
    print(information[i])


print('====information while all====')

i = 0
while True:
    if i > len(information):
        break
    else:
        print(information)
        i += 1


print('====information All====')
for x, y in information.items():
    print(x, end=': ')
    print(y)
