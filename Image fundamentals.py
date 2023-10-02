import cv2
import random 
img = cv2.imread("./assets/logo.jpg", -1)

tag = img[500:700, 600:900]
img[100:300, 650:950] = tag

# for i in range(100):
#     for j in range(img.shape[1]):\
#         img[i][j] = [random.randint(0,255), random.randint(0, 255), random.randint(0, 255)]

# print(img) # show a numpuy array list
# print(img.shape) #print the image row, colum, and channel. channel means colors space. how many pxls or value are in the image

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.distroyAllWindows()