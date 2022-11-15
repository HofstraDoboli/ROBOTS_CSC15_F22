## Lab 2 ## 

### Goals ###

1. Learn about Infrared Sensors (IR sensors)
2. Use Infrared Sensors to detect an object to the left or the right of the robot
3. Use Infrared Sensors to move around obstacles. 

### References ###

a. Look at the user manual https://www.mouser.com/pdfdocs/Alphabot2-user-manual-en.pdf  
b. AlphaBot2 Wiki: https://www.waveshare.com/wiki/AlphaBot2-Pi#Introduction  
c. Learn how to move the robot's motors: https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/
 
### Tasks ### 

1. Identify IR (infrared) sensors on the robot
2. Read how they work: https://www.keyence.com/ss/products/sensor/sensorbasics/photoelectric/info/
3. Follow the steps in Readme.md to connect to the robot. 
4. Follow the steps in Readme.md to move to /python/ folder. 

5. **Copy file `check_ir_sensors.py` on the robot**
    * Type `nano check_ir_sensors.py` and enter
    * Copy and paste the content of the file `check_ir_sensors.py` from here to the nano text editor
    * Type `CTRL-X` and 'y' to save the changes. 
6. Run `check_ir_sensors.py`. Type `python check_ir_sensors.py`. Observe what happens when you put your hand on the left, front and right side of the robot. Look at the program. Write what the program `check_ir_sensors.py` does in `Answers.txt`. Be specific. 

7. **Copy file `move_forward_ir_sensors.py` on the robot**
    * Type `nano move_forward_ir_sensors.py` and enter
    * Copy and paste the content of the file `move_forward_ir_sensors.py` from here to the nano text editor
    * Type `CTRL-X` and 'y' to save the changes. 
8. Run `move_forward_ir_sensors.py`. Type `python move_forward_ir_sensors.py`. Observe what happens when you put your hand on the left, front and right side of the robot. Look at the program. Write what the program `move_forward_ir_sensors.py` does in `Answers.txt`. Be specific.

9.  Type `cp move_forward_ir_sensors.py move_ir_sensors.py' (this copies the content of `move_forward_ir_sensors.py` to `move_ir_sensors.py`. 
10. Type `nano move_ir_sensors.py`. Modify this file, so the robot turns left if a robot is detected on its right side and it turns right if a robot is detected on its left side and forward otherwise. Use some of the move commands below. Copy your final code in `Answers.txt`. Write if your program worked or not and if not what do you think happened?

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

 
