import random
count = int(input('로또를 몇장 구매하시겠습니까?: '))

for i in range(count):
    number = random.sample(range(1, 46), 6)
    number.sort()
    print(number)
