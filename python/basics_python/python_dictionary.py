menu = {'짜장': 4000, '짬뽕': 5000, '탕수육': 9000}

# dictionary add key value
menu['냉면'] = 6000
print(menu)

# dictionaty value change
print(menu['탕수육'])
menu['탕수육'] = 8500
print(menu['탕수육'])


del menu['냉면']
print(menu)
