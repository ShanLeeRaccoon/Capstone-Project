from gpiozero import InputDevice, OutputDevice
from time import sleep, time
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

w = (255, 255, 255) #white
b = (0, 0, 0) # Black
y = (255, 169, 0) #yellow

arrow_up = [
   b, b, b, w, w, b, b, b,
   b, b, w, w, w, w, b, b,
   b, w, b, w, w, b, w, b,
   b, b, b, w, w, b, b, b,
   b, b, b, w, w, b, b, b,
   b, b, b, w, w, b, b, b,
   b, b, b, w, w, b, b, b,
   b, b, b, w, w, b, b, b
]
arrow_left = [
   b, b, b, b, b, b, b, b,
   b, b, y, b, b, b, b, b,
   b, y, b, b, b, b, b, b,
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   b, y, b, b, b, b, b, b,
   b, b, y, b, b, b, b, b,
   b, b, b, b, b, b, b, b
]


arrow_right = [
   b, b, b, b, b, b, b, b,
   b, b, b, b, b, y, b, b,
   b, b, b, b, b, b, y, b,
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   b, b, b, b, b, b, y, b,
   b, b, b, b, b, y, b, b,
   b, b, b, b, b, b, b, b
]

trig = OutputDevice(4)
trig2 = OutputDevice(17)


# def pulse_motor():
#     trig.on()
#     trig2.on()
    
def straight():
    sense.set_pixels(arrow_up)
    
    

def left():
    for i in range(10):
        sense.clear()
        trig.off()
        sleep(0.3)
        sense.set_pixels(arrow_left)
        trig.on()
        sleep(0.3)
        
        
    # trig.on()
    # trig.off()
    
    sense.clear()
    trig.off()
    
def right():
    for i in range(10):
        sense.clear()
        trig2.off()
        sleep(0.3)
        trig2.on()
        sense.set_pixels(arrow_right)
        sleep(0.3)
        
    # trig2.on()
    # trig2.off()
    
    sense.clear()
    trig2.off()

run = True

while run:
    straight()
    
    i = input("Please input a turning prompt, press L to turn left, R to turn right and E to exit")
    if i == "l":
        left()
    elif i == "r":
        right()
    elif i == "e":
        sense.clear()
        run = False