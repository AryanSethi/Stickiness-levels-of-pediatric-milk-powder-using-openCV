import cv2
import matplotlib.pyplot as plt

image1= cv2.imread('turbidity difference/a.jpg')
image2= cv2.imread('turbidity difference/b.jpg')
image3= cv2.imread('turbidity difference/c.jpg')
image4= cv2.imread('turbidity difference/d.jpg')
image5= cv2.imread('turbidity difference/e.jpg')
image6= cv2.imread('turbidity difference/f.jpg')
# image7= cv2.imread('d3/7.jpg')



hist1 = cv2.calcHist([image1],[0],None,[256],[0,256])
hist1= 100*hist1/sum(hist1)
hist2 = cv2.calcHist([image2],[0],None,[256],[0,256])
hist2= 100*hist2/sum(hist2)
hist3 = cv2.calcHist([image3],[0],None,[256],[0,256])
hist3= 100*hist3/sum(hist3)
hist4 = cv2.calcHist([image4],[0],None,[256],[0,256])
hist4= 100*hist4/sum(hist4)
hist5 = cv2.calcHist([image5],[0],None,[256],[0,256])
hist5= 100*hist5/sum(hist5)
hist6 = cv2.calcHist([image6],[0],None,[256],[0,256])
hist6= 100*hist6/sum(hist6)
# hist7 = cv2.calcHist([image7],[0],None,[256],[0,256])
# hist7= 100*hist7/sum(hist7)

plt.subplot(231), plt.plot(hist1)
plt.subplot(232), plt.plot(hist2)
plt.subplot(233), plt.plot(hist3)
plt.subplot(234), plt.plot(hist4)
plt.subplot(235), plt.plot(hist5)
plt.subplot(236), plt.plot(hist6)
# plt.subplot(337), plt.plot(hist7)

plt.show()
