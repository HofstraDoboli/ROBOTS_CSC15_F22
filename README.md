# ROBOTS_CSC15_F22

## Add device to Hofstra ## 

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

## Login to the robot's Raspberry Pi ##

0. On a Windows computer download ssh (PuTTY) app (`https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.77-installer.msi`)
0. On a Mac computer open a terminal window (lookfor Terminal in Launchpad)
1. From your Terminal, type the following command: `ssh pi@xx.xx.xx.xx`, 
   where `xx.xx.xx.xx` are the top row of numbers on the side of the Ethernet port.
2. It will ask you for a password. Enter `goodyear` as the password and press the Enter key.
3. You are now connected to the robot's Raspberry PI

