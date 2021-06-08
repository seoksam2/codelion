name = input("이름을 입력하세요")
print(name+"씨 안녕하세요.")

food1 = input("내가 먹은 음식 가격 : ")
food2 = input("친구가 먹은 음식 가격 : ")

# input type str, translation -> int(str)
food1 = int(food1)
food2 = int(food2)

print(food1 + food2)


월세 = int(input("월세를 입력해주세요 : "))
관리비 = int(input("관리비를 입력해주세요 : "))

print(월세 + 관리비)
print(월세 - 관리비)
print((월세 + 관리비) * 12)
print(월세 / 관리비)
