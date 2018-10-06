# Detecting-Bluetooth-Presence-on-Raspberry-Pi
For this project I have modified the Pi to detect the presence of my iPhone using Bluetooth signal.  The objective is to detect whether a particular device within the vicinity of the Pi and then take some actions.   (An example situation is checking whether someone in your family is home or not, sort of a "poor man surveillance')

 

Once a Bluetooth device is detected, I programmed my Pi to:  (1) Turn on a lamp, (2) send an message to a WebEx Teams room.

## Components and Setup:

I configured the Raspberry Pi to run Raspbian.  There is a lot of resources on the web on how to setup the Pi.  I recommend the Raspberry Pi Cookbook which tells you the exact steps to get the Pi running.  The kit I used also contains an USB WiFi dongle, a breakout ribbon cable to connect to the I/O pins and a breadboard.

 
I also added a Bluetooth USB dongle.  I used one made by Asus but any Bluetooth dongle should do.  You do need to install drivers to activate Bluetooth.  Here is the link to the instruction:

http://www.raspberrypi.org/learning/robo-butler/bluetooth-setup/

 
