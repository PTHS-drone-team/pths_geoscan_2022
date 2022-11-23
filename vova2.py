import time
import random
import cv2
import numpy as np
from pioneer_sdk import Camera, Pioneer

drone_ips = ["192.168.137.109"]
cameras = [Camera(ip, ip=ip) for ip in drone_ips]
pioneers = [Pioneer(ip, ip=ip) for ip in drone_ips]

time.sleep(3)
 

pioneers[0].arm()
time.sleep(5)
pioneers[0].takeoff()

#
# Поочерёдно поднимаем и опускаем каждый дрон
# for i in range(len(pioneers)):
#     pioneers[i].arm()
#     time.sleep(5)
#     pioneers[i].takeoff()
#     time.sleep(5)
#     pioneers[i].go_to_local_point(0.2, 0.1, 0.5, 0)
#     time.sleep(3)
#     for j in range(3):
#         time.sleep(1)
#         pioneers[i].go_to_local_point(0.15 * random.random(), 0.15 * random.random(), 0.11 * random.random(), 0)
#     pioneers[i].go_to_local_point(0, 1, 0, 0)
#
#
# for i in range(len(pioneers)):
#     pioneers[i].land()
#     pioneers[i].disarm()
#
#
# # time.sleep(2)
# # for ii in range(2):
# #     for i in range(len(pioneers)):
# #         pioneer = pioneers[i]
# #         camera = cameras[i]
# #         pioneers[i].arm()
# #         time.sleep(1)
# #         pioneer.takeoff()
# #         time.sleep(2)
# #         pioneer.land()
# #
# # for i in range(len(pioneers)):
#     pioneers[i].disarm()