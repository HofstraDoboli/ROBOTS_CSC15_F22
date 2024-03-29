# This is the same code as in move_forward_ir_sensors.py 
# You need to change it so the robot moves left when an object is detected on the right side, 
# and it moves right when an object is detected on the left side. 

import RPi.GPIO as GPIO
import time
from AlphaBot2 import AlphaBot2 # import the class with function definitions

Ab = AlphaBot2() # Ab = alphabot robot

DR = 19          # Infrared sensor Right
DL = 16          # Infrared sensor Left

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(DR,GPIO.IN,GPIO.PUD_UP) # set Infrared sensor as input, type PUD_UP (
pull up resistor)
GPIO.setup(DL,GPIO.IN,GPIO.PUD_UP)

Ab.setPWMA(20) # set duty cycle for the left motor
Ab.setPWMB(20) # set duty cycle for the right motor
 
try: # catch runtime error in the block of code inside try
 Ab.forward() # start moving forward slowly
 while True: # run forever
  DR_status = GPIO.input(DR) # read again the infrared sensors
  DL_status = GPIO.input(DL)
  if (DR_status == 0): # right side robot object detected
   print("DR= 0, object right - Turn left ") 
   Ab.left()
  
  elif (DL_status == 0):  # left side robot object detected
   print("DL = 0, object left - Turn right ")
   Ab.right()               
  else: # no objects detected 
   Ab.forward()
                         
except KeyboardInterrupt: # if the program was stopped from the keyboard (ctrl-c ) then stop the program 
 GPIO.cleanup();
