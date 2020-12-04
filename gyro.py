from sense_hat import SenseHat
from time import sleep
import time
import json

sense = SenseHat()
sense.set_rotation(0)

w = (255, 255, 255) #white
b = (0, 0, 0) # Black
y = (255, 169, 0) #yellow

arrow_n = [
b, b, b, w, w, b, b, b,
b, b, w, w, w, w, b, b,
b, w, b, w, w, b, w, b,
b, b, b, w, w, b, b, b,
b, b, b, w, w, b, b, b,
b, b, b, w, w, b, b, b,
b, b, b, w, w, b, b, b,
b, b, b, w, w, b, b, b
]

arrow_ne = [
b, b, b, w, w, w, w, b,
b, b, b, b, b, w, b, w,
b, b, b, b, w, b, w, w,
b, b, b, w, b, w, b, w,
b, b, w, b, w, b, b, w,
b, w, b, w, b, b, b, b,
w, b, w, b, b, b, b, b,
b, w, b, b, b, b, b, b
]

arrow_e = [
b, b, b, b, b, b, b, b,
b, b, b, b, b, w, b, b,
b, b, b, b, b, b, w, b,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
b, b, b, b, b, b, w, b,
b, b, b, b, b, w, b, b,
b, b, b, b, b, b, b, b
]

arrow_se = [
b, w, b, b, b, b, b, b,
w, b, w, b, b, b, b, b,
b, w, b, w, b, b, b, b,
b, b, w, b, w, b, b, w,
b, b, b, w, b, w, b, w,
b, b, b, b, w, b, w, w,
b, b, b, b, b, w, b, w,
b, b, b, w, w, w, w, b
]

arrow_s = [
b, b, b, w, w, b, b, b,
b, b, b, w, w, b, b, b,
b, b, b, w, w, b, b, b,
b, b, b, w, w, b, b, b,
b, b, b, w, w, b, b, b,
b, w, b, w, w, b, w, b,
b, b, w, w, w, w, b, b,
b, b, b, w, w, b, b, b
]

arrow_sw = [
b, b, b, b, b, b, w, b,
b, b, b, b, b, w, b, w,
b, b, b, b, w, b, w, b,
w, b, b, w, b, w, b, b,
w, b, w, b, w, b, b, b,
w, w, b, w, b, b, b, b,
w, b, w, b, b, b, b, b,
b, w, w, w, w, b, b, b
]

arrow_w = [
b, b, b, b, b, b, b, b,
b, b, w, b, b, b, b, b,
b, w, b, b, b, b, b, b,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
b, w, b, b, b, b, b, b,
b, b, w, b, b, b, b, b,
b, b, b, b, b, b, b, b
]

arrow_nw = [
b, w, w, w, w, b, b, b,
w, b, w, b, b, b, b, b,
w, w, b, w, b, b, b, b,
w, b, w, b, w, b, b, b,
w, b, b, w, b, w, b, b,
b, b, b, b, w, b, w, b,
b, b, b, b, b, w, b, w,
b, b, b, b, b, b, w, b
]



def run_compass(bearing):
    # sense.set_rotation(0)
    local_bearing = bearing
    timeout = time.time() + 10   # 10s from now
    print(local_bearing)
    while True:
        # sleep(1)
        north = sense.get_compass()
        #Calibration
        north = north - 95
        if north < 0:
            north = north + 360
        north = round(north, 1)
        print("bearing: ", local_bearing)
        target = north - local_bearing
        if target < 0:
            target = target + 360 
        print("Target: %s" % target)
        print("North: %s" % north)

        if (target >= 337.5) or ((target >= 0) and (target < 22.5)):
            sense.set_pixels(arrow_n)

        elif (target >= 22.5) and (target < 67.5):
            sense.set_pixels(arrow_nw)

        elif (target >= 67.5) and (target < 112.5):
            sense.set_pixels(arrow_w)

        elif (target >= 112.5) and (target < 157.5):
            sense.set_pixels(arrow_sw)
        
        elif (target >= 157.5) and (target < 202.5):
            sense.set_pixels(arrow_s)
        
        elif (target >= 202.5) and (target < 247.5):
            sense.set_pixels(arrow_se)

        elif (target >= 247.5) and (target < 292.5):
            sense.set_pixels(arrow_e)

        elif (target >= 292.5) and (target < 337.5):
            sense.set_pixels(arrow_ne)

        with open('/home/pi/Desktop/Capstone/run_compass.json', 'r') as s:
            json_data = json.load(s)
        data = json_data['status']
        if data == "Stop":
            break

        with open('/home/pi/Desktop/Capstone/bearing.json', 'r') as br:
            json_data = json.load(br)
        new_bearing = json_data['value']
        if new_bearing != local_bearing:
            local_bearing = new_bearing


while True:
    sleep(1)
    status = False
    with open('/home/pi/Desktop/Capstone/run_compass.json', 'r') as s:
        json_data = json.load(s)
    data = json_data['status']
    print(data)
    if data == "Run":
        status = True
    try:    
        while status:
            with open('/home/pi/Desktop/Capstone/bearing.json', 'r') as b:
                json_data = json.load(b)
                bearing = json_data['value']
            run_compass(bearing)
            break
    except Exception:
            pass










# run_compass(180)






