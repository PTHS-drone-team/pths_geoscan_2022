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
delta_time=0.05

while True:
    raw_frame = camera.get_frame()  # Получаем сырые данные
    if raw_frame is not None:
        # Декодируем полученные данные, чтобы получить изображение
        frame = camera_frame = cv2.imdecode(np.frombuffer(raw_frame, dtype=np.uint8), cv2.IMREAD_COLOR)
        corners, ids, rejected = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams)

        # Обводим распознанные маркеры на изображении
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)
        cv2.imshow('video', frame)  # Выводим изображение на экран

        if ids and 4 in ids:
            pioneer.land()
            pioneer.disarm()

        if ids and 5 in ids:
            pioneer.arm()
            pioneer.takeoff()


    if cv2.waitKey(1) & 0xFF == 27:  # Выход из программы, если нажали ESC
        break

cv2.destroyAllWindows()  # Закрываем все открытые окна
