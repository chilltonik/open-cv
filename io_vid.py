import os
import cv2

video_path = "videos"

vid_path = os.path.join(video_path, "cats.mp4")
video = cv2.VideoCapture(vid_path)

ret = True
while ret:
    ret, frame = video.read()
    if ret:
        cv2.imshow('frame', frame)
        cv2.waitKey(40)

video.release()
cv2.destroyAllWindows()
