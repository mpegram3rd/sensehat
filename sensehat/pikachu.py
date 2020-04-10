#!/usr/bin/python

from sense_hat import SenseHat
from time import sleep
import signal
import sys


sense = SenseHat()
sense.set_rotation(180)

def signal_handler(signal, frame):
    print('Exiting app')
    sense.clear()
    sys.exit()


bl = [0,0,0]
dg = [29,43,83]
y=[255,255,39]
o=[255,163,0]
b=[171,82,54]
r=[255,0,77]

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

sense.set_pixels(image)

signal.signal(signal.SIGINT, signal_handler)

while True:
    sleep(0.5)
    sense.flip_h()
