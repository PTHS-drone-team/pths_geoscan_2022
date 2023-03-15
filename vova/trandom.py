import math
import random
import time

from pioneer_sdk import Pioneer, Camera
import numpy as np
import cv2

drone_ips = [("192.168.137.22", "0a8"), ("192.168.137.81", "fbc")]
drone_ips = [("192.168.137.81", "fbc")]
drone_ips = [("192.168.4.1", "fbc")]
pioneers = [Pioneer(name, ip=ip) for ip, name in drone_ips]

# for pioneer in pioneers:
#     t = time.time()
#     while True:
#         t = input()
#         if t == "0":
#             break
#         print(pioneer.get_local_position_lps())

for pioneer in pioneers:
    pioneer.arm()
    pioneer.takeoff()

t = time.time()

# while time.time() - t < 30:
#     x, y, z = random.uniform(-0.8, 1), random.uniform(1, 3.8), random.uniform(-1, -0.5)
#     pioneers[0].go_to_local_point(x, y, z, 0)
#     t1 = time.time()
#     while time.time() - t1 < 2:
#         continue
#     pioneers[1].go_to_local_point(x, y, z, 0)

pioneer = pioneers[0]
#
# pioneer.land()
# pioneer.disarm()
# exit()

x0 = 0
y0 = 2
z0 = -0.5
r = 0.7
c = math.pi / 16
k = 0
while time.time() - t < 1:
    pioneer.led_control(255, 0, 0, 0)

    print(60 - (time.time() - t))
    x1 = r * math.sin(k * c) + x0
    y1 = r * math.cos(k * c) + y0
    pioneer.go_to_local_point(x1, y1, z0, 0)
    k += 1

    while not pioneer.point_reached():
        continue

for pioneer in pioneers:
    pioneer.land()
    pioneer.disarm()

# for pioneer in pioneers:
#     pioneer.arm()
#     pioneer.takeoff()
#     pioneer.go_to_local_point(1, 1, -1, 0)
#
# t = time.time()
#
# while time.time() - t < 10:
#     pass
#
# for pioneer in pioneers:
#     pioneer.land()
#     pioneer.disarm()

# coords = [[-0.11, 1.0, -0.6, 0], [-0.8994336128234863, 1.113474726676941, -0.6, 0], [-0.8869765996932983, 1.987778663635254, -0.6, 0]]
# while True:
#     frame = camera.get_frame()
#     if time.time() - t > 25:
#         pioneer_mini.land()
#         pioneer_mini.disarm()
#         cv2.destroyAllWindows()
#         exit(0)
#     if frame is not None:
#         camera_frame = cv2.imdecode(np.frombuffer(frame, dtype=np.uint8), cv2.IMREAD_COLOR)
#         print(pioneer_mini.get_local_position_lps())
#         # for coord in coords:
#         #     pioneer_mini.go_to_local_point(*coord)
#         #     while not pioneer_mini.point_reached():
#         #         continue
#         #     time.sleep(3)
#
#         cv2.imshow('pioneer_camera_stream', camera_frame)
#
#     if cv2.waitKey(5) & 0xFF == 27:  # esc
#         print('esc pressed')
#         pioneer_mini.land()
#         pioneer_mini.disarm()
#         cv2.destroyAllWindows()
#         exit(0)
