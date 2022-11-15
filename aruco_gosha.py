import cv2
import numpy as np
import time
from pioneer_sdk import Camera, Pioneer


arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250) # Словарь aruco-маркеров
arucoParams = cv2.aruco.DetectorParameters_create() # Параметры детектирования (в данном случае параметры по умолчанию)

pioneer_mini = Pioneer(ip='192.168.4.1')
camera = Camera(ip='192.168.4.1')
print(pioneer_mini.get_battery_status())
try:
    while True:
        ch_1, ch_2, ch_3, ch_4, ch_5 = 1500, 1500, 1500, 1500, 2000
        frame_copter = camera.get_frame()
        if frame_copter is not None:
            frame = cv2.imdecode(np.frombuffer(frame_copter, dtype=np.uint8), cv2.IMREAD_COLOR)
            corners, ids, rejected = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams) # Детектируем маркеры
            dc = cv2.aruco.drawDetectedMarkers(frame, corners, ids) # Обводим распознанные маркеры на изображении
            dsize = (int(frame.shape[1]), int(frame.shape[0]))

            if len(corners) > 0:
                center = (int((corners[0][0][0][0] + corners[0][0][2][0]) / 2),
                          int((corners[0][0][0][1] + corners[0][0][2][1]) / 2))
                frame = cv2.circle(frame, (center[0], center[1]), 10, (0, 255, 0), -1)
                r = 80
                if center[0] >= dsize[0] // 2 - r and center[0] <= dsize[0] // 2 + r:
                    print("OK")
                    ch_2 = 1500
                elif center[0] > dsize[0] // 2 + r:
                    print("right")
                    ch_2 = 1400
                elif center[0] < dsize[0] // 2 - r:
                    ch_2 = 1600
                    command = 1000
               # print(center, frame.shape, dsize, sep = "\n")

            frame = cv2.line(frame, (dsize[0] // 2 - 30, 0), (dsize[0] // 2 - 30, dsize[1]), (255, 0, 0))
            frame = cv2.line(frame, (dsize[0] // 2 + 30, 0), (dsize[0] // 2 + 30, dsize[1]), (255, 0, 0))
            #output = cv2.resize(frame, dsize_cam)
            cv2.imshow('video', frame) # Выводим изображение на экран

        key = cv2.waitKey(1)
        if key & 0xFF == 27:  # Выход из программы, если нажали ESC
            print('esc pressed')
            pioneer_mini.land()
            cv2.destroyAllWindows()
            exit(0)
        elif key == ord('1'):
            pioneer_mini.arm()
        elif key == ord('2'):
            pioneer_mini.disarm()
        elif key == ord('3'):
            time.sleep(2)
            pioneer_mini.arm()
            time.sleep(1)
            pioneer_mini.takeoff()
            time.sleep(2)
        elif key == ord('4'):
            pioneer_mini.land()
        elif key == ord('q'):
            ch_2 = 2000
        elif key == ord('e'):
            ch_2 = 1000
        pioneer_mini.send_rc_channels(channel_1=ch_1, channel_2=ch_2, channel_3=ch_3, channel_4=ch_4,
                                      channel_5=ch_5)


    cap.release()  # Отпускаем захват камеры
    cv2.destroyAllWindows()  # Закрываем все открытые окна
finally:
    time.sleep(1)
    pioneer_mini.land()
