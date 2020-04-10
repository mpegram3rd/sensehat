from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from time import *
from random import *
import hogwarts
import signal
import sys

sense = SenseHat()
sense.low_light=False

def show_house(pixels, name):
  sense.show_message("You are in "+ name, scroll_speed=0.05)
  sense.set_pixels(pixels)
  sleep(5)


def pick_a_house():
  sense.show_message("Hmm... I'm thinking!", scroll_speed=0.05)
  sense.set_pixels(hogwarts.sorting_hat)
  for x in range(1,5):
    sense.flip_h()
    sleep(0.75)

  house_number = randint(0, 3)
  if house_number == 0:
    show_house(hogwarts.gryffindor, "Gryffindor")

  if house_number == 1:
    show_house(hogwarts.slytherin, "Slytherin")

  if house_number == 2:
    show_house(hogwarts.hufflepuff, "Hufflepuff")

  if house_number == 3:
    show_house(hogwarts.ravenclaw, "Ravenclaw")
    
# Screen cleanup for app exit
def signal_handler(signal, frame):
    print('Exitting app')
    sense.clear()
    sys.exit()

signal.signal(signal.SIGINT, signal_handler)
  
while True:
  sense.set_pixels(hogwarts.sorting_hat)
  event = sense.stick.wait_for_event()
  if event.action == ACTION_RELEASED: 
    pick_a_house()


