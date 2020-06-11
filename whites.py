import cv2

image= cv2.imread('turbidity difference/2.jpg')
image =cv2.resize(image, (0,0), fx=0.2, fy=0.2)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
points=[]
for startx in range(281,286):
    for starty in range(371,375):
        points.append((startx,starty))


intensities=[]
for x,y in points:
    circle = cv2.circle(gray, (x,y), 1, (255,255,255), -1)
    intensities.append(gray[x][y])

print(intensities)

cv2.imshow('my image', gray)
cv2.waitKey(0)