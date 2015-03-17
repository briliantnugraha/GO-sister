import cv2

img = cv2.imread("bili.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("grey_img.png",gray_img)
cv2.imshow("Image color",img)
cv2.imshow("Image gray",gray_img)
