orders = ["짜장", "짬뽕", "탕수육"]
food = input("먹고싶은 메뉴를 입력해주세요 : ")

if food in orders:
    print("주문할 수 있습니다.")
else:
    print("주문할 수 없습니다.")


menu = {"짜장": 4000, "짬뽕": 5000, "탕수육": 9000}
food = input("먹고싶은 메뉴를 입력해주세요 : ")

if food in menu:
    print("주문 가능")
    print(menu[food], '원 입니다.')
else:
    print("주문 불가")
