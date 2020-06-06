import cv2
import matplotlib.pyplot as plt

image= cv2.imread('d3/1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred= cv2.GaussianBlur(gray,(5,5),0)
cv2.imshow('gray',cv2.resize(blurred,(700,700)))

start=160
increament=20

for _ in range(3):
    image_name= str(start)+"-"+str(start+increament)
    _,thresh= cv2.threshold(blurred,start+increament,255,cv2.THRESH_TOZERO_INV)
    _,thresh= cv2.threshold(thresh, start, 255, cv2.THRESH_TOZERO)
    thresh= cv2.resize(thresh, (500, 500))
    _,thresh = cv2.threshold(thresh,1, 255, cv2.THRESH_BINARY)
    cv2.imshow(image_name, thresh)
    start=start+increament

cv2.waitKey(0)
cv2.destroyAllWindows()








