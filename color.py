import cv2

img = cv2.imread("images/or_cat.png")

img_hvs = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

cv2.imshow("img", img_hvs)
cv2.waitKey(0)

