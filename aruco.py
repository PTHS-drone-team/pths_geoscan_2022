import time
import cv2
import numpy as np
from pioneer_sdk import Camera, Pioneer
import os
import sys
import math
import cv2.aruco as aruco
import yaml
import multiprocessing as mp
from multiprocessing.managers import BaseManager

arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
arucoParams = cv2.aruco.DetectorParameters_create()

camera = Camera()
pioneer = Pioneer()
curr_time = time.time()
delta_time=0.05

while True:
    raw_frame = camera.get_frame()
    if raw_frame is not None:
        frame = camera_frame = cv2.imdecode(np.frombuffer(raw_frame, dtype=np.uint8), cv2.IMREAD_COLOR)
        corners, ids, rejected = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams)
        aruco.drawAxis(camera_frame, camera_mtx, camera_dist, r_vec_rodrigues, t_vec, 0.01)
        aruco.drawDetectedMarkers(camera_frame, corners)
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)
        cv2.imshow('video', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        for i in range(4):
            pioneer.led_control(i, 0, 0, 0)
        break

cv2.destroyAllWindows()  # Закрываем все открытые окна