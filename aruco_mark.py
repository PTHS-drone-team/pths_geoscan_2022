from pioneer_sdk import Pioneer, Camera
import numpy as np
import cv2

arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
arucoParams = cv2.aruco.DetectorParameters_create()
pioneer_mini = Pioneer()
camera = Camera()
pioneer_mini.arm()
pioneer_mini.takeoff()
yaw = np.pi / 2
while True:
    frame = camera.get_frame()
    if frame is not None:
        camera_frame = cv2.imdecode(np.frombuffer(frame, dtype=np.uint8), cv2.IMREAD_COLOR)

        corners, ids, rejected = cv2.aruco.detectMarkers(camera_frame, arucoDict, parameters=arucoParams)
        cv2.aruco.drawDetectedMarkers(camera_frame, corners, ids, [255, 0, 0])

        if ids == [[5]]:
            pioneer_mini.led_control(255, 0, 0)
            pioneer_mini.land()
            break
        elif ids == [[6]]:
            pioneer_mini.go_to_local_point_body_fixed(0, 0, 0, yaw)


        dsize = (1024, 768)
        output = cv2.resize(camera_frame, dsize)
        cv2.imshow('pioneer_camera_stream', output)

    if cv2.waitKey(5) & 0xFF == 27:  # esc
        print('esc pressed')
        pioneer_mini.land()
        cv2.destroyAllWindows()
        exit(0)