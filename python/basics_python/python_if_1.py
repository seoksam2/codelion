myGrade = int(input('학번을 입력하세요: '))
youGrade = int(input('학번을 입력하세요: '))


if myGrade == youGrade:
    print('같은 학번이네')
elif myGrade > youGrade:
    print('선배!')
elif myGrade < youGrade:
    print('후배')
else:
    print('누구냐?')
