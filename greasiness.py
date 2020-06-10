import cv2
import numpy as np

image= cv2.imread('d3/7.jpg')
blurred = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#blurred= cv2.medianBlur(gray,3)
#blurred= cv2.GaussianBlur(gray,(5,5),0)
blurred=cv2.resize(blurred,(500,500))
cv2.imshow('blurred gray',blurred)

start=110
increament=20

for _ in range(1):
    image_name= str(start)+"-"+str(start+increament)
    _,thresh= cv2.threshold(blurred,start+increament,255,cv2.THRESH_TOZERO_INV)
    _,thresh= cv2.threshold(thresh, start, 255, cv2.THRESH_TOZERO)
    thresh= cv2.resize(thresh, (500, 500))
    _,thresh = cv2.threshold(thresh,1, 255, cv2.THRESH_BINARY)
    #cv2.imshow(image_name, thresh)
    start=start+increament




kernel = np.ones((2,2),np.uint8)
dilation = cv2.dilate(thresh,kernel,iterations = 1)
final= cv2.bitwise_and(blurred,dilation)
cv2.imshow("final1",final)

_,final = cv2.threshold(final,1, 150, cv2.THRESH_BINARY)
cv2.imshow('final2',final)



cv2.waitKey(0)
cv2.destroyAllWindows()








