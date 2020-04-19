
import os
import moviepy.editor as mp

import cv2
import numpy as np

import time

gif_name = "insertion.gif"
file_name = gif_name[0:gif_name.rindex('.')]
mp4_name = file_name + ".mp4"
if not os.path.exists(mp4_name):
    clip = mp.VideoFileClip(gif_name)
    clip.write_videofile(mp4_name)

cap = cv2.VideoCapture(mp4_name)
# w and h respectively
dims = [int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))]
fourcc = cv2.VideoWriter.fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter(file_name + "_output.mp4", fourcc, 5.0, (dims[0], dims[1]))

res, fx = cap.read()
res, fy = cap.read()
while cap.isOpened():
    diff = cv2.absdiff(fx, fy)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 100:
            continue
        cv2.rectangle(fx, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    image = cv2.resize(fx, (dims[0], dims[1]))
    out.write(image)
    cv2.imshow("feed", fx)
    fx = fy
    res, fy = cap.read()

    time.sleep(0.5)

    if cv2.waitKey(40) == 27:
        break;

cv2.destroyAllWindows()
cap.release()
out.release()

