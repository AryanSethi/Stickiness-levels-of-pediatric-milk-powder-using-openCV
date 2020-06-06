import cv2
import matplotlib.pyplot as plt

image1= cv2.imread('d2/.jpg')

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
blurred= cv2.GaussianBlur(gray,(5,5),0)

# _,thresh1 = cv2.threshold(blurred,85,255,cv2.THRESH_BINARY)
_,thresh2 = cv2.threshold(blurred,100,255,cv2.THRESH_BINARY)
# _,thresh3 = cv2.threshold(blurred,125,255,cv2.THRESH_BINARY)
# _,thresh4 = cv2.threshold(blurred,80,255,cv2.THRESH_BINARY)
# _,thresh5 = cv2.threshold(blurred,90,255,cv2.THRESH_BINARY)
# _,thresh6 = cv2.threshold(blurred,100,255,cv2.THRESH_BINARY)


# thresh1 = cv2.resize(thresh1,(400,400))
# thresh2 = cv2.resize(thresh2,(400,400))
# thresh3 = cv2.resize(thresh3,(400,400))
# thresh4 = cv2.resize(thresh4,(400,400))
# thresh5 = cv2.resize(thresh5,(400,400))
# thresh6 = cv2.resize(thresh6,(400,400))


# cv2.imshow('85', thresh1)
# cv2.imshow('100', thresh2)
# cv2.imshow('125', thresh3)
# cv2.imshow('80', thresh4)
# cv2.imshow('90', thresh5)
# cv2.imshow('100', thresh6)

total_pixels = image1.shape[0]*image1.shape[1]
print(100*cv2.countNonZero(thresh2)/total_pixels)

cv2.waitKey(0)
cv2.destroyAllWindows()







