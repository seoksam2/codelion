import random

# * 1번 문제
for i in range(5):
    for i in range(5):
        print('*', end='')
    print()

# * 2번 문제
for x in range(5):
    for y in range(x+1):
        print('*', end='')
    print()

# 입력 값 역순 출력
x = int(input('숫자 입력: '))

for i in range(x):
    print(x-i)


# 10단위 출력 후 줄 바꿈
x = int(input('숫자 입력: '))

for i in range(x+1):
    if i % 10 == 0:
        print(i, sep='\n')
    else:
        print(i, end=',')
print()

# 로또 번호 생성기
count = int(input('로또를 몇장 구매하시겠습니까?: '))

for i in range(count):
    number = random.sample(range(1, 46), 6)
    number.sort()
    print(number)
