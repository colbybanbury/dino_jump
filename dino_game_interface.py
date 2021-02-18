import pyautogui
import time
import serial

#This script will read output from the serial port and input a command to the game

#Steps:
#1 Connect Arduino running motion classification script
#2 Change Seial port to corrispond to the Arduino output
#3 Run this script
#4 Naviagte to this website: http://www.trex-game.skipser.com/
#5 Play the game and try to get a high score!

port = '/dev/cu.usbmodem141101' 
#This port will likely have to be changed
#You can find the correct port using the Arduino Serial Monitor


def jump():
	"""
	Jump over the obstacle
	"""
	pyautogui.keyDown('space')
	time.sleep(0.095)
	pyautogui.keyUp('space')

def duck():
	"""
	Duck!
	"""
	pyautogui.keyDown('down')
	time.sleep(0.5)
	pyautogui.keyUp('down')


ser = serial.Serial(port)
print("navigate to the game window and input up")
while(1):
	gesture = ser.readline()
	print('gesture recived: ', gesture)
	if "up" in str(gesture):
		print('jumping')
		jump()
	elif "down" in str(gesture):
		print('Duck!')
		duck()