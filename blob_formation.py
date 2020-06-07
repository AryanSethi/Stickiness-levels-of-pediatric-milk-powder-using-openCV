import cv2

image= cv2.imread('d3/3.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#blurred= cv2.medianBlur(gray,3)
blurred= cv2.GaussianBlur(gray,(5,5),0)
cv2.imshow('blurred gray',cv2.resize(blurred,(500,500)))

start=170
increament=80

for _ in range(1):
    image_name= str(start)+"-"+str(start+increament)
    _,thresh= cv2.threshold(blurred,start+increament,255,cv2.THRESH_TOZERO_INV)
    _,thresh= cv2.threshold(thresh, start, 255, cv2.THRESH_TOZERO)
    thresh= cv2.resize(thresh, (500, 500))
    _,thresh = cv2.threshold(thresh,1, 255, cv2.THRESH_BINARY)
    thresh1=cv2.medianBlur(thresh,5)
    thresh2 = cv2.medianBlur(thresh, 7)
    thresh3 = cv2.medianBlur(thresh, 9)
    cv2.imshow(image_name, thresh1)
    cv2.imshow('lol', thresh2)
    cv2.imshow('lol2', thresh3)
    start=start+increament



# previous_image=None
# start=170
# increament=10
# for i in range(8):
#     image_name= str(start)+"------"+str(start+increament)
#     _,thresh= cv2.threshold(blurred,start+increament,255,cv2.THRESH_TOZERO_INV)
#     _,thresh= cv2.threshold(thresh, start, 255, cv2.THRESH_TOZERO)
#     thresh= cv2.resize(thresh, (500, 500))
#     _,thresh = cv2.threshold(thresh,1, 255, cv2.THRESH_BINARY)
#     thresh=cv2.medianBlur(thresh,7)
#     #cv2.imshow(image_name, thresh)
#     if(start!=170):
#         cv2.bitwise_or(previous_image,thresh,previous_image)
#     elif(start==170):
#         previous_image=thresh
#     start = start + increament

# cv2.imshow('final', previous_image)




# total_pixels = image1.shape[0]*image1.shape[1]
# print(100*cv2.countNonZero(thresh2)/total_pixels)

cv2.waitKey(0)
cv2.destroyAllWindows()







