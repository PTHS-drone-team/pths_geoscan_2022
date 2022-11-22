import cv2
from cv2 import aruco
import numpy as np
import distance_class
import rotate_drone_class
from pioneer_sdk import Camera, Pioneer
import time

calib_data_path = "calib_data_pioneer/MultiMatrix.npz"
MARKER_SIZE = 2.4  # размер маркера
typeAruco = aruco.DICT_4X4_50
radius_ch_2 = 80  # расстояние до вертикальный линий от центра
radius_ch_1 = 80
speed_ch_1, speed_ch_2, speed_ch_3 = 100, 100, 100  # RC изменение
direction_change_value = 30.0  # см
ch_1, ch_2, ch_3, ch_4, ch_5 = 1500, 1500, 1500, 1500, 2000

Distance = distance_class.DistanceAruco(calib_data_path, MARKER_SIZE, typeAruco,
                                                            direction_change_value, speed_ch_3)
Rotate = rotate_drone_class.Move_drone(radius_ch_1, radius_ch_2, speed_ch_1, speed_ch_2, (640, 480))
camera = Camera()
pioneer_mini = Pioneer()

while True:
    frame_copter = camera.get_frame()
    if frame_copter is not None:
        frame = cv2.imdecode(np.frombuffer(frame_copter, dtype=np.uint8), cv2.IMREAD_COLOR)

        marker_corners = Distance.get_marker_corners(frame)

        dist = Distance.get_distance(marker_corners)
        ch_3 = Distance.get_command_to_ch_3()

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
        time.sleep(2)
    elif key == ord('4'):
        pioneer_mini.land()

    pioneer_mini.send_rc_channels(channel_1=ch_1, channel_2=ch_2, channel_3=ch_3, channel_4=ch_4,
                                  channel_5=ch_5)

cap.release()
cv.destroyAllWindows()