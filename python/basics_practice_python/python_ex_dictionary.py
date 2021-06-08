total_dictionary = {}

while True:
    question = input('질문을 입력해주세요 : ')
    if question == 'q' or question == 'ㅂ' or question == 'Q':
        break
    else:
        total_dictionary[question] = ''


print('입력한 질문 리스트 입니다.')
for i in total_dictionary:
    print(i)
print('=============')


for i in total_dictionary:
    answer = input('답변을 입력해주세요 : ')
    total_dictionary[i] = answer
print(total_dictionary)


# information['특기'] = '게임'
# information[key] = value
# {key:value, key:value}
