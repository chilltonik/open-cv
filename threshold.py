import os
import cv2

img = cv2.imread("images/or_cat.png")

img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)

thresh = cv2.blur(thresh, (10, 10))

cv2.imshow("img", img_gray)
cv2.imshow("thresh", thresh)
cv2.waitKey(0)



img = cv2.imread("images/handwritten.png")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 60, 255, cv2.THRESH_BINARY)

adaptive_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)
ret, simple_thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

# thresh = cv2.blur(thresh, (10, 10))

cv2.imshow('img', img)
cv2.imshow('adaptive_thresh', adaptive_thresh)
cv2.imshow('simple_thresh', simple_thresh)
cv2.waitKey(0)
