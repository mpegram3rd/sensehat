from sense_hat import SenseHat, ACTION_RELEASED
from time import sleep
import signal
import sys

sense = SenseHat()

# Fix it so Pikachu isn't upside down.
sense.set_rotation(180)

# Tell Sense Hat to clean up before exitting
def signal_handler(signal, frame):
    print('Exitting app')
    stop_animation()
    sys.exit()

# defines the colors for Pikachu
bl = [0,0,0]
dg = [29,43,83]
y=[255,255,39]
o=[255,163,0]
b=[171,82,54]
r=[255,0,77]

# Defines the pixel grid of Pikachu
image = [
bl,dg,dg,bl,bl,bl,bl,dg,
bl,bl,y ,o ,bl,bl,bl,o ,
bl,bl,bl,y ,y ,y ,y ,o ,
o ,o ,bl,y ,bl,y ,y ,bl,
o ,o ,bl,r ,y ,y ,y ,o,
bl,o ,bl,y ,o ,o ,o ,bl,
bl,o ,y ,o ,y ,o ,y ,bl,
bl,bl,y ,o ,b ,b ,o ,bl
]

# Animation state (on or off)
animation = False

def start_animation():
    global animation
    sense.set_pixels(image)
    while animation:
        sleep(0.5)
        sense.flip_h()

def stop_animation():
    sense.clear()

def pushed_button(event):
    global animation
    # if the button is released, we flip the animation state.
    if event.action == ACTION_RELEASED:
        animation = not animation
        if animation:
            start_animation()
        else:
            stop_animation()

sense.stick.direction_middle = pushed_button
signal.signal(signal.SIGINT, signal_handler)
signal.pause()    
