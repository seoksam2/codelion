import random

count = int(input('로또 몇장 구매하시겠습니까? : '))

for i in range(count):
    lottoNumber = random.sample(range(1, 46), 6)
    lottoNumber.sort()
    print(lottoNumber)
