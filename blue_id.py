import cv2
import numpy as np

cap = cv2.VideoCapture(0)

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

cv2.destroyAllWindows()

cap.release()
