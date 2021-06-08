
# input value -> count print
x = int(input('숫자 입력 : '))

for i in range(1, x+1):
    print(i)


# count 10 & row change
y = int(input('숫자 입력 : '))

for i in range(1, y + 1):
    if i % 10 == 0:
        print(i, end='\n')
    else:
        print(i, end='\t')


# input value -> count print
x = int(input('숫자 입력 : '))

for i in range(x, 0, -1):
    print(i)
