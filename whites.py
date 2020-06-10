import cv2

image= cv2.imread('b.jpg')
image =cv2.resize(image, (0,0), fx=0.1, fy=0.1)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#blurred= cv2.GaussianBlur(gray,(5,5),0)
circle =  cv2.circle(gray, (230,150), 5, (0,0,0), 2)
intensity = gray[230][150]
print("the color intensity is "+ str(intensity))
cv2.imshow('my image', circle)
