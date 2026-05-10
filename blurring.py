import cv2


img = cv2.imread("images/or_cat.png")

key_size = 3

blur_img = cv2.blur(img, (key_size, key_size))

cv2.imshow("img", blur_img)
cv2.waitKey(0)