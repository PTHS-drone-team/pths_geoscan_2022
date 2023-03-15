from pioneer_sdk import Pioneer
import math
import time

r = 0.5 # radius
a = 2 * math.pi / 6
x_c = 0
y_c = 2
z_c = -1.5
offset_all = 0

mini_ip = ["192.168.43.152", "192.168.43.124"]
mini = {}
offset = {}
point_reached = {}

def get_x_y(ip, k):
    x = x_c + r * math.cos(a * k + offset[ip] + offset_all)
    y = y_c + r * math.sin(a * k + offset[ip] + offset_all)
    return x, y

def wait_connection():
    while True:
        ret = True
        for ip in mini_ip:
            if not mini[ip].connected():
                ret = False
        if ret:
            return

def go_to_start_point():
    for ip in mini_ip:
        input(ip + " ARM?")
        mini[ip].arm()
        input(ip + " TAKEOFF?")
        mini[ip].takeoff()
        # mini[ip].go_to_local_point(x=x_c, y=y_c, z=z_c, yaw=0)
        # while not mini[ip].point_reached():
        #     pass
        # time.sleep(2)
        x, y = get_x_y(ip, 0)
        mini[ip].go_to_local_point(x=x, y=y, z=z_c, yaw=0)
        while not mini[ip].point_reached():
            pass



def run_circle_flight():
    k = 0
    while True:
        print("k = " + str(k))
        for ip in mini_ip:
            x, y = get_x_y(ip, k)
            mini[ip].go_to_local_point(x=x, y=y, z=z_c, yaw=0)
            point_reached[ip] = False
        while True:
            points_reached = True
            for ip in mini_ip:
                if not point_reached[ip]:
                    point_reached[ip] = mini[ip].point_reached()
                if not point_reached[ip]:
                    points_reached = False
            if points_reached:
                break
        k += 1

def all_land():
    for ip in mini_ip:
        mini[ip].land()
    return


if __name__ == '__main__':
    # Initialize pioneers
    for ip in mini_ip:
        mini[ip] = Pioneer(ip=ip, name=ip)
        offset[ip] = mini_ip.index(ip) * (2 * math.pi) / len(mini_ip)
    wait_connection() # Wait until all the drones are connected
    try:
        go_to_start_point()
        input("RUN ??????")
        run_circle_flight()
    finally:
        all_land()
