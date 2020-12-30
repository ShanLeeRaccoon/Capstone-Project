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
    sleep(15)
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


# run = True

# while run:
#     straight()
    
#     i = input("Please input a turning prompt, press L to turn left, R to turn right and E to exit")
#     if i == "l":
#         left()
#     elif i == "r":
#         right()
#     elif i == "e":
#         sense.clear()
#         run = False

# roundabout(7)