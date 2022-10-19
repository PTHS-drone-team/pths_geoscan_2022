import time
import cv2
import numpy as np
from pioneer_sdk import Camera, Pioneer

arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
arucoParams = cv2.aruco.DetectorParameters_create()

camera = Camera()
pioneer = Pioneer()
curr_time = time.time()
delta_time=0.05

while True:
    raw_frame = camera.get_frame()  # Получаем сырые данные
    if raw_frame is not None:
        # Декодируем полученные данные, чтобы получить изображение
        frame = camera_frame = cv2.imdecode(np.frombuffer(raw_frame, dtype=np.uint8), cv2.IMREAD_COLOR)
        corners, ids, rejected = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams)

        if time.time() - curr_time > delta_time:
            for i in range(4):
                if ids and 4 in ids:
                    pioneer.led_control(i, 255, 0, 0)
                    pioneer.arm()
                    pioneer.takeoff()
                else:
                    pioneer.led_control(i, 0, 0, 255)
                if ids and 5 in ids:
                    pioneer.land()
                    pioneer.disarm()
            curr_time = time.time()

        # Обводим распознанные маркеры на изображении
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)
        cv2.imshow('video', frame)  # Выводим изображение на экран

    if cv2.waitKey(1) & 0xFF == 27:  # Выход из программы, если нажали ESC
        for i in range(4):
            pioneer.led_control(i, 0, 0, 0)
        break

cv2.destroyAllWindows()  # Закрываем все открытые окна