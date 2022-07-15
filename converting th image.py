# import cv2 as cv
# path = input('path of image')
# type = input('enter the type of conversion you need in the image such as grey, blur, canny, resized image or cropping the image or text')
# image = cv.imread(path)
# cv.imshow('image', image)
# if type == 'text':
#     msg = input('enter the message')
#     location = tuple(input('enter the x and y coordinates').split())
#     location = tuple(int(i) for i in location)
#     thickness = int(input('enter the thickness'))
#     font = float(input('enter font size'))
#     color = tuple(int(input('enter the rgb value')) for _ in range(3))
#     cv.putText(image, msg, location, cv.FONT_HERSHEY_DUPLEX, font, color, thickness=thickness)
#     cv.imshow('image', image)
# elif type == 'gray':
#     gr = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#     cv.imshow('gray', gr)
# elif type == 'blur':
#     blur = cv.GaussianBlur(image, (3, 3), cv.BORDER_DEFAULT)
#     cv.imshow('blur', blur)
# elif type == 'canny':
#     cany = cv.Canny(image, 175, 125)
#     cv.imshow('canny', cany)
# elif type == 'resize':
#     list = ['width', 'height']
#     size = (int(input(f'enter the {i} of image')) for i in list)
#     cv.imshow('resize', cv.resize(image, (400, 300), interpolation=cv.INTER_AREA))
# else:
#     print('Enter valid input')
# cv.waitKey(0)
from twilio.rest import Client
accountsid = "AC15f830ec844a5201e08c95da896b6b50"
authoni = "b5d4248cbd78ae3e3227722c58c2ea09"
cli = Client(accountsid, authoni)
fro = "whatsapp:+14155238886"
to = "whatsapp:+918309197541"

mess = cli.messages.create(body="Start your game",
                           media_url='https://demo.twilio.com/owl.png',
                           from_=fro, to=to)