import cv2
import numpy as np
import time
from pioneer_sdk import Camera, Pioneer


arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250) # Словарь aruco-маркеров
arucoParams = cv2.aruco.DetectorParameters_create() # Параметры детектирования (в данном случае параметры по умолчанию)

yaw = np.pi / 24
cap = cv2.VideoCapture(0)
while True:
    success, frame = cap.read()
    corners, ids, rejected = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams) # Детектируем маркеры
    dc = cv2.aruco.drawDetectedMarkers(frame, corners, ids) # Обводим распознанные маркеры на изображении
    dsize = (int(frame.shape[1]), int(frame.shape[0]))
    r = 50
    if len(corners) > 0:
        center = (int((corners[0][0][0][0] + corners[0][0][2][0]) / 2),
                  int((corners[0][0][0][1] + corners[0][0][2][1]) / 2))
        frame = cv2.circle(frame, (center[0], center[1]), 10, (0, 255, 0), -1)
        if center[0] >= dsize[0] // 2 - r and center[0] <= dsize[0] // 2 + r:
            print("OK")
            command = 0
        elif center[0] > dsize[0] // 2 + r:
            print("right")
            command = -yaw
        elif center[0] < dsize[0] // 2 - r:
            print("left")
            command = yaw
       # print(center, frame.shape, dsize, sep = "\n")

    frame = cv2.line(frame, (dsize[0] // 2 - r, 0), (dsize[0] // 2 - r, dsize[1]), (255, 0, 0))
    frame = cv2.line(frame, (dsize[0] // 2 + r, 0), (dsize[0] // 2 + r, dsize[1]), (255, 0, 0))
    #output = cv2.resize(frame, dsize)
    cv2.imshow('video', frame) # Выводим изображение на экран

    if cv2.waitKey(1) & 0xFF == 27:  # Выход из программы, если нажали ESC
        print('esc pressed')
        cv2.destroyAllWindows()
        exit(0)

cap.release()  # Отпускаем захват камеры
cv2.destroyAllWindows()  # Закрываем все открытые окна
