# foods = ['치킨', '피자', '보쌈', '치킨']
# foods_set = set(foods)
# print(foods)
# print(foods_set)


menu1 = set(['치킨', '피자', '보쌈'])
menu2 = set(['족발', '피자', '햄버거'])
menu3 = menu1 | menu2
menu4 = menu1 & menu2
menu5 = menu1 - menu2
print(menu3)
print(menu4)
print(menu5)
