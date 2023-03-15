import cv2
from cv2 import aruco
import numpy as np
from pioneer_sdk import Camera, Pioneer
import time

pioneer = Pioneer()


pioneer.arm()
pioneer.takeoff()
pioneer.lua_script_control("Start")
time.sleep(5)
pioneer.lua_script_control("Stop")
pioneer.land()
pioneer.disarm()