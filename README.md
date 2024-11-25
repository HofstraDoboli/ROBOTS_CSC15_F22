# ROBOTS CSC15 F22

## Add device to Hofstra network ## 

1. Go to `mydevices.hofstra.edu` and login with your Hofstra portal user name and password
2. Click Add:
  * Enter device name = Robot15_last_name
  * Device ID = from the side of the Ethernet port enter all numbers on the second row (it starts with `E4`)
  * Description = enter your names
3. Click Submit. Check that the device name you chose appears on the device list.
4. Logout from `mydevices.hofstra.edu`

## Turn on robot ##

1. On the bottom flip the switch labelled `PWR SWITCH` while holding the robot straight (nothing should touch the robots)
2. Wait at least 30 seconds before attempting to login to the Raspberry Pi with the next set of directions.
3. Do not flip the PWR SWITCH switch while program is running. This will crash the ssh and the putty/terminal window. 

## Login to the robot's Raspberry Pi ##

0. On a Windows computer download ssh (PuTTY) app (https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.77-installer.msi)
0. On a Mac computer open a terminal window (lookfor Terminal in Launchpad)
1. From your Terminal, type the following command: `ssh pi@xx.xx.xx.xx`, 
   where `xx.xx.xx.xx` are the top row of numbers on the side of the Ethernet port.
   CHANGES TO IP address compared to sticker: The IP address of the robots has a change in its 3rd xx. 0 is replaced by 128, so a robot that has 10.26.0.73 on the sticker has the IP address 10.26.128.73. 
3. It will ask you for a password. Enter `raspberry`(OLD PASSWORD `goodyear`) as the password and press the Enter key.
4. You are now connected to the robot's Raspberry PI

## Go to the folder with robot's programs:

    1. Type `cd /AlphaBot2-Demo/RaspberryPi/AlphaBot2/python` and enter at the raspberry pi prompt (OLD path: `cd code/AlphaBot2/AlphaBot2/python` - DO NOT USW) 
    2. Type `ls` and enter. You will see a list of python files. 
    3. To run a program type: `python program_name.py` and enter. 
    3. To stop a program with an infinite loop, type `CTRL-C` on the putty/terminal window. 

## See and change robot's code ## 

**via the robot's terminal window**

    1. Type `pwd` and enter. The output should show the following path `.../AlphaBot2/python/`. If it shows a different path, type `cd ~` and enter. Then follow the direction 1 from ** Go to the folder with robot's programs** and repeat this step. 
    2. Type `ls` and enter to see the names of the files insidee the folder `/python/`.
    3. Choose a file to open and type: `nano file_name.py` and enter. Nano is a command prompt text editor (no GUI). You will see the file and a list of commands at the bottom. You can move in the file only with arrows and delete or add new code. 
    4. When you are done making changes, press `CTRL-X` then 'y' to save changes, then press enter one more time to save and exit the editor. 
    
**SKIP THIS STEP via an application (cyberduck)** 

0. Install cyberduck on your machine from: https://cyberduck.io/download/
  * Download the zip file for your machine (Windows or Mac)
  * Double click on the zip file and follow instructions. 
  * On the Mac computer move the unzipped file in the Applications folder

1. Open cyberduck app
   * Click `Open connection`
   * Select from the drop down menu SFTP
   * Enter on the first entry the number `10.26.xx.xx`
   * Enter `pi` for user name
   * Enter `goodyear` for password
   * Click on Allow on the window that shows up (SSL certificate). Also select Always. 
   * More details on https://pressable.com/knowledgebase/cyberduck-sftp-setup/#setting-up-cyberduck 
   * You should now see the folders and files on the robot's PI


