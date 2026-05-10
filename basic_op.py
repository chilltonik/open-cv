import os
import cv2

img = cv2.imread("images/orange_cat.png")

res_img = cv2.resize(img, (600, 600, ))
cv2.imwrite("images/or_cat.png", res_img)
print(res_img.shape)

cv2.imshow('img', res_img)
cv2.waitKey(0)

cropped_img = img[200:400, 200:400]
cv2.imshow('img', cropped_img)
cv2.waitKey(0)