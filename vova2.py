import time
import random
import cv2
import numpy as np
from pioneer_sdk import Camera, Pioneer

drone_ips = ["192.168.137.73", "192.168.137.190", "192.168.137.145"]
drone_names = {"192.168.137.73": "drone1", "192.168.137.190": "drone2", "192.168.137.145": "drone3"}

cameras = [Camera(drone_names[ip], ip=ip) for ip in drone_ips]
pioneers = [Pioneer(drone_names[ip], ip=ip) for ip in drone_ips]

time.sleep(3)

# Поочерёдно поднимаем и опускаем каждый дрон
for i in range(len(pioneers)):
    pioneers[i].arm()

for i in range(len(pioneers)):
    pioneers[i].takeoff()
    pioneers[i].go_to_local_point(0, 0, 1, 0)
    t = time.time()
    while not pioneers[i].point_reached():
        if time.time() - t > 3:
            break
        pass

for i in range(len(pioneers)):
    pioneers[i].go_to_local_point(0, 0, 2, 0)
    t = time.time()
    while not pioneers[i].point_reached():
        if time.time() - t > 3:
            break
        pass

    pioneers[i].go_to_local_point(0, 0, 1, 0)
    t = time.time()
    while not pioneers[i].point_reached():
        if time.time() - t > 3:
            break
        pass


for i in range(len(pioneers)):
    pioneers[i].land()
    pioneers[i].disarm()


#
#   for i in range(len(pioneers)):
#     pioneers[i].go_to_local_point(0, 0, 2, 0)
#     time.sleep(3)
#     pioneers[i].go_to_local_point(0, 0, 1, 0)
#
#
# for i in range(len(pioneers)):
#     pioneers[i].land()
#     pioneers[i].disarm()


# time.sleep(2)
# for ii in range(2):
#     for i in range(len(pioneers)):
#         pioneer = pioneers[i]
#         camera = cameras[i]
#         pioneers[i].arm()
#         time.sleep(1)
#         pioneer.takeoff()
#         time.sleep(2)
#         pioneer.land()
#
# for i in range(len(pioneers)):
#     pioneers[i].disarm()