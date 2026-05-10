import os
import cv2

images_path = "images/"

img_path = os.path.join(images_path, "cat.png")
img = cv2.imread(img_path)

cv2.imwrite(os.path.join(images_path, "cat_out.png"), img)

cv2.imshow("catttt", img)
cv2.waitKey(0)
