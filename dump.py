import cv2

image= cv2.imread('turbidity difference/4.jpg')
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([image],[0],None,[256],[0,256])
sum=0
for intensity in range(256):
    sum=sum+(intensity*hist[intensity])

print(sum/(316*342))