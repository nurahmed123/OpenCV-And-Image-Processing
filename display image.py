import cv2

img = cv2.imread("./assets/logo.jpg", 0)
# img = cv2.resize(img, (400, 400))
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite("new img.jpg", img)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindow()