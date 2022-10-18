## Lab 1 ## 

### Goals ###

1. Learn the robot (power switch, power connector, sensors).
2. Connect to the robot's raspberry PI. 
3. Open and edit a robot file (move.py). 
4. Understand basic move commands. 
5. Modify move.py

### References ###

a.  Look at the user manual https://www.mouser.com/pdfdocs/Alphabot2-user-manual-en.pdf  
b. AlphaBot2 Wiki: https://www.waveshare.com/wiki/AlphaBot2-Pi#Introduction  
c. Learn how to move the robot's motors: https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/
 
### Tasks ### 

1. Identify all inputs/outputs and sensors on the robot (check reference pages (a) and (b)). 
2. Understand how DC motors work. Read about pulse width modulation (PWM) here: https://prototyperobotics.com/tutorials/pulse-width-modulation. 
    * What is duty cycle?
    * What is the relationship between motor speed and duty cycle?
3. Understand how the robot moves (check the reference page (c)): 
    * Robot moves forward/backward if both motors move forward/backward with the same duty cycle. 
    * Robot turns left if: right motor moves forwars and left motor moves backward. 
    * Robot turns right if: left motor moves forward and left motor moves backwards.
5. Follow the steps in Readme.md to connect to the robot. 
6. Follow the steps in Readme.md to move to /python/ folder. 

**Robot move functions (defined in AlphaBot2.py)**

* robot_obj.setPWMA(value) = set duty cycle for left motor, value is between 0 and 100
* robot_obj.setPWMB(value) = set duty cycle for right motor, value is between 0 and 100
* robot_obj.stop()         = stop both motors of the robot
* robot_obj.forward()      = move robot forwardo with the duty cycle set with set PWMA
* robot_obj.backward()     = move robot backward with the duty cycle set with set PWMA
* robot_obj.left()         = move right wheel forward, left wheel backward with 30% duty cycle
* robot_obj.right()        = move left wheel forward, right wheel backward with 30% duty cycle
* robot_obj.setMotor(left, right)
    * The robot moves with independent left and right duty cycles. 
    * Both right and left values can be between -100 and 100. 
    * if left is positive, the robot moves the right wheel forward with duty cycle  = left
    * if left is negative, the robot moves the right wheel backward with duty cycle = -left
    * if right is positive, the robot moves the left wheel forward with duty cycle  = left
    * if right is negative, the robot moves the left wheel backward with duty cycle = -left
* NOTES: 
    * Once you call a robot move function, you need to specify the time you want the robot to execute it. Use the command time.sleep(seconds) to control how long a robot move function runs. 
    * In between two robot move commands, add a stop command for a more reliable movement. 

**Copy move.py on the robot**

7. Type `nano move.py` and enter
8. Copy and paste the content of the file `move.py` from here to the nano text editor
9. Type `CTRL-X` and 'y' to save the changes. 

**Understand move.py and run it**

10. Type `nano move.py` and look at the file. Identify what each line does. Then type `CTRL-X` and 'y' to exit. 
11. Put the robot in the middle of the desk. Run the program by typing `python move.py` and enter. 
Make sure the robot doesn't fall. What does the robot do?

**Make changes to move.py**

12. Type `nano move.py` and enter. 
13. Change the code so the robot moves forward, turns right approximately 90 degrees, and then moves forward again. Test with the turn right time so the robot makes a reasonably close 90 degrees turn. 
14. Make the robot move in a square. Change the code by adding a for loop that repeats 4 times. Inside the loop the robot should do 2 moves: move forward followed by a turn approx .90 degrees. Test the program. Copy the program in the file `move_square.py`
15. Change the turn right with a turn left. Test the program on the robot. 
16. Make the robot move in a circle first clockwise and then counter-clockwise. Call the function `setMotor(left, right)` to move the robot in a circle. Change the values of left and right to adjust the radius of the circle. Copy the program in file `move_circle.py`
17. In the file `Answers.txt` answer the questions. 
18. In the file `WhatYourGroupDid.txt` write what experiments you did with the robot and what did you observe. Explain what you did, what worked, what did not work, and what problems you had 