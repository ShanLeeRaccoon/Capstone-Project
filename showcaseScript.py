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

order1 = [
    b, w, b, b, b, b, b, b,
    w, w, b, b, b, b, b, b,
    b, w, b, b, b, b, b, b,
    b, w, b, b, b, b, y, b,
    w, w, w, b, y, y, y, y,
    b, b, b, b, y, b, y, b,
    b, b, b, b, y, b, b, b,
    b, b, b, b, y, b, b, b 
]

order2 = [
    w, w, w, b, b, b, b, b,
    b, b, w, b, b, b, b, b,
    w, w, w, b, b, b, b, b,
    w, b, b, b, b, b, y, b,
    w, w, w, b, y, y, y, y,
    b, b, b, b, y, b, y, b,
    b, b, b, b, y, b, b, b,
    b, b, b, b, y, b, b, b
]

order3 = [ 
    w, w, w, b, b, b, b, b,
    b, b, w, b, b, b, b, b,
    w, w, w, b, b, b, b, b,
    b, b, w, b, b, b, y, b,
    w, w, w, b, y, y, y, y,
    b, b, b, b, y, b, y, b,
    b, b, b, b, y, b, b, b,
    b, b, b, b, y, b, b, b 
]
order4 = [
    w, b, w, b, b, b, b, b,
    w, b, w, b, b, b, b, b,
    w, w, w, b, b, b, b, b,
    b, b, w, b, b, b, y, b,
    b, b, w, b, y, y, y, y,
    b, b, b, b, y, b, y, b,
    b, b, b, b, y, b, b, b,
    b, b, b, b, y, b, b, b
]

order5 = [
    w, w, w, b, b, b, b, b,
    w, b, b, b, b, b, b, b,
    w, w, w, b, b, b, b, b,
    b, b, w, b, b, b, y, b,
    w, w, w, b, y, y, y, y,
    b, b, b, b, y, b, y, b,
    b, b, b, b, y, b, b, b,
    b, b, b, b, y, b, b, b
]

order6 = [
    w, w, w, b, b, b, b, b,
    w, b, b, b, b, b, b, b,
    w, w, w, b, b, b, b, b,
    w, b, w, b, b, b, y, b,
    w, w, w, b, y, y, y, y,
    b, b, b, b, y, b, y, b,
    b, b, b, b, y, b, b, b,
    b, b, b, b, y, b, b, b
]
order7 = [
    w, w, w, b, b, b, b, b,
    b, b, w, b, b, b, b, b,
    b, b, w, b, b, b, b, b,
    b, b, w,b, b, b, y, b,
    b, b, w, b, y, y, y, y,
    b, b, b, b, y, b, y, b,
    b, b, b, b, y, b, b, b,
    b, b, b, b, y, b, b, b 
]

order8 = [
    w, w, w, b, b, b, b, b,
    w, b, w, b, b, b, b, b,
    w, w, w, b, b, b, b, b,
    w, b, w, b, b, b, y, b,
    w, w, w, b, y, y, y, y,
    b, b, b, b, y, b, y, b,
    b, b, b, b, y, b, b, b,
    b, b, b, b, y, b, b, b
]

order9 = [
    w, w, w, b, b, b, b, b,
    w, b, w, b, b, b, b, b,
    w, w, w, b, b, b, b, b,
    b, b, w, b, b, b, y, b,
    w, w, w, b, y, y, y, y,
    b, b, b, b, y, b, y, b,
    b, b, b, b, y, b, b, b,
    b, b, b, b, y, b, b, b 
]

u_turn_right = [
    b, b, b, b, b, b, b, b,
    b, y, y, y, y, y, y, b,
    b, y, y, y, y, y, y, b,
    b, y, y, b, b, y, y, b,
    b, y, y, b, b, y, y, b,
    b, y, y, b, b, y, y, b,
    b, b, b, b, y, y, y, y,
    b, b, b, b, b, y, y, b
    ]

U_turn_left = [ 
    b, b, b, b, b, b, b, b,
    b, y, y, y, y, y, y, b,
    b, y, y, y, y, y, y, b,
    b, y, y, b, b, y, y, b,
    b, y, y, b, b, y, y, b,
    b, y, y, b, b, y, y, b,
    y, y, y, y, b, b, b, b,
    b, y, y, b, b, b, b, b
]
trig = OutputDevice(4)
trig2 = OutputDevice(17)


# def pulse_motor():
#     trig.on()
#     trig2.on()
    

def roundabout(exitNum):
    if exitNum == 1:
        sense.set_pixels(order1)
    elif exitNum == 2:
        sense.set_pixels(order2)
    elif exitNum == 3:
        sense.set_pixels(order3)
    elif exitNum == 4:
        sense.set_pixels(order4)
    elif exitNum == 5:
        sense.set_pixels(order5)
    elif exitNum == 6:
        sense.set_pixels(order6)
    elif exitNum == 7:
        sense.set_pixels(order7)
    elif exitNum == 8:
        sense.set_pixels(order8)
    elif exitNum == 9:
        sense.set_pixels(order9)
    else:
        print("out of range!!")

    trig2.on()
    trig.on()
    sleep(3)
    trig2.off()
    trig.off()

    sleep(10)
    sense.clear()

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
        
    
    sense.clear()
    trig2.off()

def uturnL():
    for i in range(10):
        sense.clear()
        trig.off()
        sleep(0.3)
        sense.set_pixels(U_turn_left)
        trig.on()
        sleep(0.3)
        
   
    
    sense.clear()
    trig.off()

def uturnR():
    for i in range(10):
        sense.clear()
        trig2.off()
        sleep(0.3)
        sense.set_pixels(u_turn_right)
        trig2.on()
        sleep(0.3)
        
   
    
    sense.clear()
    trig2.off()
    

while True:
    straight()
    sleep(5)
    left()
    straight()
    sleep(5)
    uturnL()
    straight()
    sleep(5)
    roundabout(4)
    straight()
    sleep(5)
    right()
    straight()
    sleep(5)
    left()
    straight()
    sleep(5)
    uturnR()
    straight()
    sleep(5)
    roundabout(2)
    straight()
    sleep(5)
    right()
    
