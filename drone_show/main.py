import cv2
from cv2 import aruco
import numpy as np
from pioneer_sdk import Camera, Pioneer
import time

drone_names = {"192.168.137.73": "drone1", "192.168.137.190": "drone2", "192.168.137.145": "drone3"}