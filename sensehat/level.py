from sense_hat import SenseHat
from time import sleep

import signal
import sys

sense = SenseHat()
sense.clear()

# Start in the middle of the screen.
black = (0,0,0)
white = (255, 255, 255)
green = (0, 255, 0)

x = 0
y = 0
done = False

def signal_handler(signal, frame):
    print('Exiting app')
    sense.clear()
    sys.exit()

def pushed_button(event):
    done = True;

def init():
    sense.clear();
    sense.set_pixel(x,y, (255, 255, 255));
    signal.signal(signal.SIGINT, signal_handler)
    sense.stick.direction_middle = pushed_button

def update_level(pitch, roll, x, y):
    newx = x
    newy = y
    print "Pitch: %s and Roll: %s" % (pitch, roll)
    if 0 < pitch < 180:
       newx = 3 - (pitch // 22)      
       if newx < 0:
          newx = 0
    elif 359 > pitch > 181:
       newx = 4 + ((360 - pitch) // 22)
       if newx > 7:
          newx = 7

    if 0 < roll < 180:
       newy = 4 + (roll // 22)
       if newy > 7:
          newy = 7
    elif 359 > roll > 181:
       newy = 3 - ((360 - roll) // 22)
       if newy < 0:
          newy = 0

    print "x: %s, y: %s, newx: %s, newy %s: " % (x, y, newx, newy)
    sense.set_pixel(x, y, black)
    roundpitch = round(pitch)
    roundroll = round(roll)
    print "roundpitch: %s, roundroll: %s" % (roundpitch, roundroll)
    dotcolor = white
    if (roundpitch <= 1 or roundpitch >= 358) and (roundroll <= 1 or roundroll >= 358):
       dotcolor = green 
    sense.set_pixel(newx, newy, dotcolor)

    return newx, newy

init()

while not done:
    pitch = sense.get_orientation()['pitch']
    roll = sense.get_orientation()['roll']
    x, y = update_level(pitch, roll, x, y)
    sleep(0.5)

sense.clear()
sys.exit()
