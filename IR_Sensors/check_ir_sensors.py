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

try: # catch runtime error in the block of code inside try
        DR_status = GPIO.input(DR) # read the infrared sensors
        DL_status = GPIO.input(DL)
        print("Right=", DR_status,"Left=", DL_status)   
        while True: # run forever
                DR_last = DR_status # save the last values of the sensors
                DL_last = DL_status
                DR_status = GPIO.input(DR) # read again the infrared sensors
                DL_status = GPIO.input(DL)

                if DR_last != DR_status or DL_last != DL_status: # if there is a
 change in the sensors
                        print("Right=", DR_status,"Left=", DL_status)   

except KeyboardInterrupt: # if the program was stopped from the keyboard (ctrl-c) then stop the program 
        GPIO.cleanup();
