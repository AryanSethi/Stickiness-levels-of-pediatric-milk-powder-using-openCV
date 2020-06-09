import cv2
import numpy as np

image= cv2.imread('d3/7.jpg')
blurred = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#blurred= cv2.medianBlur(gray,3)
#blurred= cv2.GaussianBlur(gray,(5,5),0)
blurred=cv2.resize(blurred,(500,500))
cv2.imshow('blurred gray',blurred)

start=80
increament=10

for _ in range(8):
    image_name= str(start)+"-"+str(start+increament)
    _,thresh= cv2.threshold(blurred,start+increament,255,cv2.THRESH_TOZERO_INV)
    _,thresh= cv2.threshold(thresh, start, 255, cv2.THRESH_TOZERO)
    thresh= cv2.resize(thresh, (500, 500))
    _,thresh = cv2.threshold(thresh,1, 255, cv2.THRESH_BINARY)
    cv2.imshow(image_name, thresh)
    start=start+increament