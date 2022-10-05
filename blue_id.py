import cv2
import numpy as np
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

while (1):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([50, 50, 110])
    upper_blue = np.array([200, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    res = cv2.bitwise_and(frame, frame, mask=mask)
    #cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    #cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        nzCount = cv2.countNonZero(mask);
        break
print(nzCount)
print(width, height)
if nzCount > width * height / 3:
    print("WELL DONE")

cv2.destroyAllWindows()

cap.release()
