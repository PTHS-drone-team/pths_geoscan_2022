import cv2
from cv2 import aruco
import numpy as np
import distance_class
import move_drone_class
from pioneer_sdk import Camera, Pioneer
import time

calib_data_path = "calib_data_pioneer/MultiMatrix.npz"
MARKER_SIZE = 8.1  # размер маркера
typeAruco = cv2.aruco.DICT_6X6_250
radius_ch_2 = 80  # расстояние до вертикальный линий от центра
radius_ch_1 = 80
speed_ch_1, speed_ch_2, speed_ch_3 = 300, 100, 100  # RC изменение
direction_change_value = 50.0  # см
ch_1, ch_2, ch_3, ch_4, ch_5 = 1500, 1500, 1500, 1500, 2000

Distance = distance_class.DistanceAruco(calib_data_path, MARKER_SIZE, typeAruco,
                                                            direction_change_value, speed_ch_3)
Rotate = move_drone_class.Move_drone(radius_ch_1, radius_ch_2, speed_ch_1, speed_ch_2, (640, 480))
camera = Camera()
pioneer_mini = Pioneer()

while True:
    frame_copter = camera.get_frame()
    if frame_copter is not None:
        frame = cv2.imdecode(np.frombuffer(frame_copter, dtype=np.uint8), cv2.IMREAD_COLOR)

        marker_corners = Distance.get_marker_corners(frame)
        dist = Distance.get_distance(marker_corners)
        # if dist is not None:
        #     ch_3 = Distance.get_command_to_ch_3(dist)
        # else:
        #     ch_3 = 1500
        if dist is not None:
            if dist > 70.0:
                ch_3 = 1500 - speed_ch_3
            elif dist < 30.0:
                ch_3 = 1500 + speed_ch_3
            else:
                ch_3 = 1500
        # print(dist, ch_3, sep=" ")


        center = Rotate.get_center(marker_corners)
        ch_2 = Rotate.get_command_to_ch_2(center)
        ch_1 = Rotate.get_command_to_ch_1(center)

        Rotate.draw_line(frame)

        if center is not None:
            frame = cv2.circle(frame, (center[0], center[1]), 10, (0, 255, 0), -1)
        cv2.imshow("video", frame)

    key = cv2.waitKey(1)
    if key & 0xFF == 27:  # Выход из программы, если нажали ESC
        print('esc pressed')
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
        # pioneer_mini.go_to_local_point(0, 0, 1.5, 0)
        # while not pioneer_mini.point_reached():
        #     pass
        time.sleep(2)
    elif key == ord('4'):
        pioneer_mini.land()

    # print(ch_1, ch_2, ch_3, ch_4, ch_5, sep=" ")
    pioneer_mini.send_rc_channels(channel_1=int(ch_1), channel_2=int(ch_2), channel_3=int(ch_3), channel_4=int(ch_4), channel_5=int(ch_5))

cap.release()
cv.destroyAllWindows()