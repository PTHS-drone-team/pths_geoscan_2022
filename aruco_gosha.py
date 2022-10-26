import cv2
import numpy as np


arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250) # Словарь aruco-маркеров
arucoParams = cv2.aruco.DetectorParameters_create() # Параметры детектирования (в данном случае параметры по умолчанию)

cap = cv2.VideoCapture(0)
dsize = (800, 600)

while True:
    ret, frame = cap.read()  # Получаем изображение
    corners, ids, rejected = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams) # Детектируем маркеры
    dc = cv2.aruco.drawDetectedMarkers(frame, corners, ids) # Обводим распознанные маркеры на изображении

    if len(corners) > 0:
        center = (int((corners[0][0][0][0] + corners[0][0][2][0]) / 2),
                  int((corners[0][0][0][1] + corners[0][0][2][1]) / 2))
        cv2.circle(frame, (center[0], center[1]), 10, (0, 255, 0), -1)
        if center[0] > dsize[1] // 2 + 50:
            print("left")
        elif center[0] < dsize[1] // 2 - 50:
            print("right")
        else:
            print("OK")

    cv2.line(frame, (dsize[0] // 2 - 150, 0), (dsize[0] // 2 - 150, dsize[1]), (255, 0, 0))
    cv2.line(frame, (dsize[0] // 2 - 50, 0), (dsize[0] // 2 - 50, dsize[1]), (255, 0, 0))
    output = cv2.resize(frame, dsize)
    cv2.imshow('video', output) # Выводим изображение на экран

    if cv2.waitKey(1) & 0xFF == 27:  # Выход из программы, если нажали ESC
        break

cap.release()  # Отпускаем захват камеры
cv2.destroyAllWindows()  # Закрываем все открытые окна