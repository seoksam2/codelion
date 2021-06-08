import smtplib
from email.message import EmailMessage
import imghdr
import re

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
addr = 'seoksam2@gmail.com'


def sendEmail(addr):
    reg = '^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$'
    if bool(re.match(reg, addr)):
        smtp.send_message(message)
        print('메일을 발송하였습니다.')
    else:
        print('유요한 메일이 아닙니다.')


message = EmailMessage()
message.set_content(
    '코드 라이언 수업 중 메일 보내기로 메일을 보내봅니다.\n잘 보내졌는지 궁금하구만....\n줄바꿈도 잘되었나?')

message['Subject'] = 'ptyhon 메일 보내기 연습.'
message['From'] = 'seoksam2@gmail.com'
message['To'] = 'seoksam2@gmail.com'

with open('/Users/seoksam2/Documents/projects/codelion_python/course_5/bm.png', 'rb') as image:
    image_file = image.read()

image_type = imghdr.what('bm', image_file)
message.add_attachment(image_file, maintype='image', subtype=image_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login('seoksam2@gmail.com', 'iloveline81!!')

sendEmail(addr)

smtp.quit()
