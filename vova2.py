import time
import cv2
import numpy as np
from pioneer_sdk import Camera, Pioneer

# Словарь aruco-маркеров
arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
# Параметры детектирования (в данном случае параметры по умолчанию)
arucoParams = cv2.aruco.DetectorParameters_create()

camera = Camera()
pioneer = Pioneer()
curr_time = time.time()
delta_time = 0.05

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    frame_width = int(frame.shape[1])
    frame_height = int(frame.shape[0])

    corners, ids, rejected = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams)

    # Обводим распознанные маркеры на изображении
    # cv2.aruco.drawDetectedMarkers(frame, corners, ids)
    if (len(corners) > 0):
        center = (int((corners[0][0][0][0] + corners[0][0][2][0]) / 2),
                  int((corners[0][0][0][1] + corners[0][0][2][1]) / 2))

        if (center[0] > frame_width / 2 + 100):
            print("right")
            frame = cv2.arrowedLine(frame, (20, 10), (10, 10), (0, 0, 255), 2)

        elif (center[0] < frame_width / 2 - 100):
            print("left")
            frame = cv2.arrowedLine(frame, (10, 10), (20, 10), (0, 0, 255), 2)


        frame = cv2.circle(frame, center, 10, (255, 0, 0), thickness=-1)

    frame = cv2.line(frame, (frame_width // 2 - 100, 0), (frame_width // 2 - 100, frame_height), (0, 255, 0), 5)
    frame = cv2.line(frame, (frame_width // 2 + 100, 0), (frame_width // 2 + 100, frame_height), (0, 255, 0), 5)

    cv2.imshow('video', frame)  # Выводим изображение на экран

    if cv2.waitKey(1) & 0xFF == 27:  # Выход из программы, если нажали ESC
        break

cv2.destroyAllWindows()  # Закрываем все открытые окна