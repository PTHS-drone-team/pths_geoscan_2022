import cv2
import numpy as np
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
nzCount = 0
flag = 0
temp = 0

while (1):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([50, 50, 110])
    upper_blue = np.array([200, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    nzCount = cv2.countNonZero(mask)
    if nzCount > width * height / 3:
        flag = 1
    else:
        flag = 0
    if flag == 0:
        cv2.imshow('mask', mask)
    elif flag == 1:
        cv2.imshow('frame', frame)

    #cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 0:
        temp = 1
    if k == 27:
        break

cv2.destroyAllWindows()

cap.release()
