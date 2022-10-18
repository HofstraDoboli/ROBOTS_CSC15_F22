import RPi.GPIO as GPIO
import time
from AlphaBot2 import AlphaBot2

Ab = AlphaBot2()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Task 1: move forward 1 second, stop 2 seconds, move backwards stop 2 seconds
try:
  # slower speed
  Ab.PA = 30
  Ab.PB = 30
  
  Ab.forward()    # move forward
  time.sleep(1)   # for 1 second
  
  Ab.stop()       # stop 
  time.sleep(2)   # for 2 seconds
  
  Ab.backward()   # move backwards
  time.sleep(1)   # for 1 second
  Ab.stop()       # stop

except KeyboardInterrupt:
  GPIO.cleanup();
    
