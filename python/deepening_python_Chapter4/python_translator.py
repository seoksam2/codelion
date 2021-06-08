from googletrans import Translator

translator = Translator()

sentence = input("입력: ")
nationList = {'프랑스': ' fr', '아랍': ' ar', '베트남': ' vi',
              '스페인': ' es', '영어': ' en', '중국': ' zh-CN'}
print(nationList)
dest = input('어디?: ')

result = translator.translate(sentence, dest)
detected = translator.detect(sentence)


print('========= 출력 결과 ==========')
print(detected.lang, ':', sentence)
print(result.dest, ':', result.text)
print('===========================')

# sentence = "안녕"
# sentence = str(input('감지한 언어 입력: '))

# detected = translator.detect(sentence, dest, sec)

# print(detected.lang)
