#!/usr/bin/python

from sense_hat import SenseHat, ACTION_RELEASED
import time
import signal
import sys

sense = SenseHat()

def clear():
    sense.clear()

def signal_handler(signal, frame):
    print('Exitting app')
    clear()
    sys.exit()

sense.set_rotation(180)

def clear():
    sense.clear()

def toFarenheit(tempInC):
    return tempInC * 1.8 + 32

def pushed_button(event):
    if event.action == ACTION_RELEASED:
        t = toFarenheit(sense.get_temperature())
        th = toFarenheit(sense.get_temperature_from_humidity())
        tp = toFarenheit(sense.get_temperature_from_pressure())
        p = sense.get_pressure()
        h = sense.get_humidity()

        t = round(t, 1)
        th = round(th, 1)
        tp = round(tp, 1)
        p = round(p, 1)
        h = round(h, 1)

        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        print("Reading as of %s" % currentTime)
        print("Temperature: %s F" % t)
        print("Temperature (from Humidity): %s F" % th)
        print("Temperature (from Pressure): %s F" % tp)
        print ("Pressure: %s (millibars) " %p )
        print ("Humidity: %s%% " %h )

        msg = "Temperature = {0}, Pressure = {1}, Humidity = {2}".format(t,p,h)

        sense.show_message(msg, scroll_speed=0.05)

        clear()

clear()
sense.stick.direction_middle = pushed_button
signal.signal(signal.SIGINT, signal_handler)
signal.pause()

