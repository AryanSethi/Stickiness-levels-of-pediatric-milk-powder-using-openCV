import cv2

image= cv2.imread('d3/1.jpg')
blurred = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#blurred= cv2.medianBlur(gray,3)
#blurred= cv2.GaussianBlur(gray,(5,5),0)
cv2.imshow('blurred gray',cv2.resize(blurred,(700,700)))

start=110
increament=40

for _ in range(1):
    image_name= str(start)+"-"+str(start+increament)
    _,thresh= cv2.threshold(blurred,start+increament,255,cv2.THRESH_TOZERO_INV)
    _,thresh= cv2.threshold(thresh, start, 255, cv2.THRESH_TOZERO)
    thresh= cv2.resize(thresh, (500, 500))
    _,thresh = cv2.threshold(thresh,1, 255, cv2.THRESH_BINARY)
    cv2.imshow(image_name, thresh)
    start=start+increament


median=cv2.medianBlur(thresh,9)
cv2.imshow('median',median)
gaussian=cv2.GaussianBlur(median,(51,51),0)
cv2.imshow('gaussian',gaussian)
_,final=cv2.threshold(gaussian,150,255,cv2.THRESH_BINARY)
cv2.imshow('final',final)

cv2.waitKey(0)
cv2.destroyAllWindows()








