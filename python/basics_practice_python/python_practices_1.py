# * columns
for i in range(5):
    print('*')


# * rows
for i in range(5):
    print('*' * 5)


# *row * 5
for x in range(5):
    for y in range(5):
        print('*', end='')
    print('')


# row add *
for x in range(1, 6):
    print('*'*x)
