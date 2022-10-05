from pioneer_sdk import Pioneer, Camera
import numpy as np
import cv2
pioneer_mini = Pioneer()
camera = Camera()
pioneer_mini.disarm()
while True:
    frame = camera.get_frame()
    if frame is not None:
        camera_frame = cv2.imdecode(np.frombuffer(frame, dtype=np.uint8), cv2.IMREAD_COLOR)
        cv2.imshow('pioneer_camera_stream', camera_frame)
        pioneer_mini.arm()
        pioneer_mini.takeoff()
    key = cv2.waitKey(1)
    if key == 27:  # esc
        print('esc pressed')
        cv2.destroyAllWindows()
        exit(0)