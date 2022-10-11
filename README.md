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

0. On a Windows computer download ssh (PuTTY) app (https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.77-installer.msi)
0. On a Mac computer open a terminal window (lookfor Terminal in Launchpad)
1. From your Terminal, type the following command: `ssh pi@xx.xx.xx.xx`, 
   where `xx.xx.xx.xx` are the top row of numbers on the side of the Ethernet port.
2. It will ask you for a password. Enter `goodyear` as the password and press the Enter key.
3. You are now connected to the robot's Raspberry PI

## Access robot's code ## 

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


Do not flip the PWR SWITCH switch while program is running. This will crash the ssh and the putty/terminal window. 
Stop the robot with CTRL-C on the putty/terminal window. 
