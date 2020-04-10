#!/usr/bin/python

from sense_hat import SenseHat
from time import sleep
import signal
import sys

sense = SenseHat()
sense.set_rotation(180)

def signal_handler(signal, frame):
    print('Exitting app')
    sense.clear()
    sys.exit()

bl = [0,0,0]
dg = [29,43,83]
lg = [120,120,180]
w = [255,255,255]
b = [0,0,80]
g = [0,25,0]
y=[255,255,39]
o=[255,163,0]
br=[171,82,54]
r=[255,0,77]

image = [
bl,bl,y ,y ,y ,y ,bl,bl,
bl,y ,lg,lg,y ,y ,y ,bl,
bl,lg,w ,w ,lg,y ,y ,bl,
bl,lg,w ,w ,lg,dg,dg,bl,
bl,y ,lg,lg,y ,y ,y ,bl,
bl,y ,y ,y ,y ,y ,y ,bl,
bl,b ,b ,b ,b ,b ,b ,bl,
bl,bl,b ,b ,b ,b ,bl,bl,
]

sense.set_pixels(image)

signal.signal(signal.SIGINT, signal_handler)

while True:
    sleep(0.5)
    sense.flip_h()
