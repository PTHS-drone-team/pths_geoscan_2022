import time
import cv2
import numpy as np

# Словарь aruco-маркеров
arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
# Параметры детектирования (в данном случае параметры по умолчанию)
arucoParams = cv2.aruco.DetectorParameters_create()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv2.imshow('video', frame)

    frame_width = int(frame.shape[1])
    frame_height = int(frame.shape[0])

    corners, ids, rejected = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams)

    # Обводим распознанные маркеры на изображении
    cv2.aruco.drawDetectedMarkers(frame, corners, ids)
    if (len(corners) > 0):
        center = (int((corners[0][0][0][0] + corners[0][0][2][0]) / 2),
                  int((corners[0][0][0][1] + corners[0][0][2][1]) / 2))

        if (center[0] > frame_width / 2 + 100):
            ch_2 = 1000
            frame = cv2.arrowedLine(frame, (20, 10), (100, 10), (0, 0, 255), 3)


        elif (center[0] < frame_width / 2 - 100):
            ch_2 = 2000
            frame = cv2.arrowedLine(frame, (100, 10), (20, 10), (0, 0, 255), 3)

        frame = cv2.circle(frame, center, 5, (255, 0, 0), thickness=-1)

    frame = cv2.line(frame, (frame_width // 2 - 100, 0), (frame_width // 2 - 100, frame_height), (0, 255, 0), 5)
    frame = cv2.line(frame, (frame_width // 2 + 100, 0), (frame_width // 2 + 100, frame_height), (0, 255, 0), 5)

    cv2.imshow('video', frame)  # Выводим изображение на экран

    pioneer.send_rc_channels(channel_1=ch_1, channel_2=ch_2, channel_3=ch_3, channel_4=ch_4,
                             channel_5=ch_5)

    if cv2.waitKey(1) & 0xFF == 27:  # Выход из программы, если нажали ESC
        break

cap.release()
cv2.destroyAllWindows()  # Закрываем все открытые окна
