import time
import cv2
import numpy as np
from pioneer_sdk import Camera, Pioneer

drone_ips = ["192.168.137.28"]

cameras = [Camera(ip) for ip in drone_ips]
pioneers = [Pioneer(ip) for ip in drone_ips]

# Поочерёдно поднимаем и опускаем каждый дрон
while True:
    for i in range(len(pioneers)):
        pioneer = pioneers[i]
        camera = cameras[i]
        pioneer.send_rc_channels(1500, 1500, 1500, 1500, 2000)
        time.sleep(1)
        pioneer.send_rc_channels(1500, 1500, 1500, 1500, 1000)
        time.sleep(1)
        pioneer.send_rc_channels(1500, 1500, 1500, 1500, 2000)
        time.sleep(1)
        pioneer.send_rc_channels(1500, 1500, 1500, 1500, 1000)
        time.sleep(1)
        pioneer.send_rc_channels(1500, 1500, 1500, 1500, 2000)
        time.sleep(1)
        pioneer.send_rc_channels(1500, 1500, 1500, 1500, 1000)
        time.sleep(1)
        pioneer.send_rc_channels(1500, 1500, 1500, 1500, 2000)
        time.sleep(1)
        pioneer.send_rc_channels(1500, 1500, 1500, 1500, 1000)
        time.sleep(1)
        pioneer.send_rc_channels(1500, 1500, 1500, 1500, 2000)
        time.sleep(1)
        pioneer.send_rc_channels(1500, 1500, 1500, 1500, 1000)
        time.sleep(1)
        pioneer.send_rc_channels(1500, 1500, 1500, 1500, 2000)
        time.sleep(1)
        pioneer.send_rc_channels(1500, 1500, 1500, 1500, 1000)
        time.sleep(1)
        pioneer.send_rc_channels(1500, 1500, 1500, 1500, 2000)
        time.sleep(1)
        pioneer.send_rc_channels(1500, 1500, 1500, 1500, 1000)
        time.sleep(1)
        pioneer.send_rc_channels(1500, 1500, 1500, 1500, 2000)
        time.sleep(1)
        pioneer.send_rc_channels(1500, 1500, 1500, 1500, 1000)