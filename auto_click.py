import pyautogui as gui
from time import sleep
import winsound

i = 1
a = (1962, 229) #Open python from terminal to find the position
		#Command: pyautogui.position() and press enter after moving the 
			#mouns pointer to the position we want to click
b = (3104, 451)	#Find the position where we want to check the color
while True:
	gui.click(a)	#click the active button
	sleep(2)	#wait 2 seconds to let the page load

	try:
		c = gui.pixel(b[0],b[1])	#color of the positon where the send-offer button should be

		if c != (247,247,247):		# check if the color is not grey
			gui.click(b)		#click the send-offer button
			winsound.Beep(1800,2000)	#1800Hz frequency and 2 seconds 
			print('Attention!')		
			sleep(45)		#wait extra 45 seconds if tehe is a job
		else:
			print(i)
		sleep(25)			#
		i+=1
		
	except:					#if for some reason any error arise
		print('Trying agian')
		winsound.Beep(2200,50)
		sleep(15)
		#continue
