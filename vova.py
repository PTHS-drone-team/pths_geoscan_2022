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

min_v = 1300
max_v = 1700


while True:
    raw_frame = camera.get_frame()  # Получаем сырые данные
    ch_1 = 1500
    ch_2 = 1500
    ch_3 = 1500
    ch_4 = 1500
    ch_5 = 2000

    if raw_frame is not None:
        frame = camera_frame = cv2.imdecode(np.frombuffer(raw_frame, dtype=np.uint8), cv2.IMREAD_COLOR)

        frame_width = int(frame.shape[1])
        frame_height = int(frame.shape[0])

        corners, ids, rejected = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams)

        # Обводим распознанные маркеры на изображении
        # cv2.aruco.drawDetectedMarkers(frame, corners, ids)
        if (len(corners) > 0):
            center = (int((corners[0][0][0][0] + corners[0][0][2][0]) / 2),
                      int((corners[0][0][0][1] + corners[0][0][2][1]) / 2))

            if (center[0] > frame_width / 2 + 50):
                ch_2 = 1400
                frame = cv2.arrowedLine(frame, (20, 10), (100, 10), (0, 0, 255), 3)


            elif (center[0] < frame_width / 2 - 50):
                ch_2 = 1600
                frame = cv2.arrowedLine(frame, (100, 10), (20, 10), (0, 0, 255), 3)

            frame = cv2.circle(frame, center, 10, (255, 0, 0), thickness=-1)

        frame = cv2.line(frame, (frame_width // 2 - 50, 0), (frame_width // 2 - 50, frame_height), (0, 255, 0), 5)
        frame = cv2.line(frame, (frame_width // 2 + 50, 0), (frame_width // 2 + 50, frame_height), (0, 255, 0), 5)

        cv2.imshow('video', frame)  # Выводим изображение на экран

    key = cv2.waitKey(1)
    if key == 27:  # esc
        print('esc pressed')
        cv2.destroyAllWindows()
        pioneer.land()
        pioneer.disarm()
        break
    elif key == ord('1'):
        pioneer.arm()
    elif key == ord('2'):
        ch_1 = 2000
    elif key == ord('k'):
        ch_1 = 1000

    pioneer.send_rc_channels(channel_1=ch_1, channel_2=ch_2, channel_3=ch_3, channel_4=ch_4,
                             channel_5=ch_5)
cv2.destroyAllWindows()  # Закрываем все открытые окна
