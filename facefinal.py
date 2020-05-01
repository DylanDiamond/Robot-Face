
import numpy as np
import cv2
import serial
import time
ser = serial.Serial('COM9',baudrate = 9600)
face_cascade = cv2.CascadeClassifier('C:\\Users\\dylan\\Desktop\\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if np.any(faces):
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
#        print("x")
#        print(x)
            hieght = h/2+y
            mid = w/2+x


            #lINE 3
            if mid > 864 and hieght > 288 and hieght < 432:
                ser.write(repr(1).encode('ascii'))
                ser.write(repr(",").encode('ascii'))
            if mid < 216 and hieght > 288 and hieght < 432:
                ser.write(repr(2).encode('ascii'))
                ser.write(repr(",").encode('ascii'))
            if mid > 432 and mid < 648 and hieght > 288 and hieght < 432:
                ser.write(repr(0).encode('ascii'))
                ser.write(repr(",").encode('ascii'))
            if mid > 216 and mid < 432 and hieght > 288 and hieght < 432:
                ser.write(repr(9).encode('ascii'))
                ser.write(repr(",").encode('ascii'))
            if mid > 648 and mid < 864 and hieght > 288 and hieght < 432:
                ser.write(repr(10).encode('ascii'))
                ser.write(repr(",").encode('ascii'))


            #lINE 1
            if mid > 864 and hieght < 144:
                ser.write(repr(3).encode('ascii'))
                ser.write(repr(",").encode('ascii'))
            if mid < 216 and hieght < 144:
                ser.write(repr(4).encode('ascii'))
                ser.write(repr(",").encode('ascii'))
            if mid > 432 and mid < 740 and hieght < 144:
                ser.write(repr(5).encode('ascii'))
                ser.write(repr(",").encode('ascii'))
            if mid > 216 and mid < 432 and hieght  < 144:
                ser.write(repr(11).encode('ascii'))
                ser.write(repr(",").encode('ascii'))
            if mid > 648 and mid < 864 and hieght < 144:
                ser.write(repr(12).encode('ascii'))
                ser.write(repr(",").encode('ascii'))

            #LINE 5
            if mid > 864 and hieght > 576:
                ser.write(repr(6).encode('ascii'))
                ser.write(repr(",").encode('ascii'))
            if mid < 216 and hieght > 576:
                ser.write(repr(7).encode('ascii'))
                ser.write(repr(",").encode('ascii'))
            if mid > 432 and mid < 740 and hieght > 576:
                ser.write(repr(8).encode('ascii'))
                ser.write(repr(",").encode('ascii'))
            if mid > 216 and mid < 432 and hieght  < 576:
                ser.write(repr(13).encode('ascii'))
                ser.write(repr(",").encode('ascii'))
            if mid > 648 and mid < 864 and hieght < 576:
                ser.write(repr(14).encode('ascii'))
                ser.write(repr(",").encode('ascii'))

            #LINE 4
            if mid > 864 and hieght > 432 and hieght < 576:
                ser.write(repr(19).encode('ascii'))
                ser.write(repr(",").encode('ascii'))
            if mid < 216 and hieght > 432 and hieght < 576:
                ser.write(repr(15).encode('ascii'))
                ser.write(repr(",").encode('ascii'))
            if mid > 432 and mid < 740 and hieght > 432 and hieght < 576:
                ser.write(repr(17).encode('ascii'))
                ser.write(repr(",").encode('ascii'))
            if mid > 216 and mid < 432 and hieght > 432 and hieght < 576:
                ser.write(repr(16).encode('ascii'))
                ser.write(repr(",").encode('ascii'))
            if mid > 648 and mid < 864 and hieght > 432 and hieght < 576:
                ser.write(repr(18).encode('ascii'))
                ser.write(repr(",").encode('ascii'))

            #LINE 2
            if mid > 864 and hieght > 144 and hieght < 288:
                ser.write(repr(24).encode('ascii'))
                ser.write(repr(",").encode('ascii'))
            if mid < 216 and hieght > 144 and hieght < 288:
                ser.write(repr(20).encode('ascii'))
                ser.write(repr(",").encode('ascii'))
            if mid > 432 and mid < 740 and hieght > 144 and hieght < 288:
                ser.write(repr(22).encode('ascii'))
                ser.write(repr(",").encode('ascii'))
            if mid > 216 and mid < 432 and hieght > 144 and hieght < 288:
                ser.write(repr(21).encode('ascii'))
                ser.write(repr(",").encode('ascii'))
            if mid > 648 and mid < 864 and hieght > 144 and hieght < 288:
                ser.write(repr(23).encode('ascii'))
                ser.write(repr(",").encode('ascii'))


    else:
#        print("no face")
        ser.write(repr(25).encode('ascii'))
        ser.write(repr(",").encode('ascii'))
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
