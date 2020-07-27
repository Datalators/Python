import pyautogui as gui
from time import sleep
import winsound

i = 1
#print('Hover to active button and press Enter')
a = (1962, 229)
#print('Hover to send offer button and press Enter')
b = (3104, 451)
while True:
	gui.click(a)
	sleep(2)

	try:
		c = gui.pixel(a[0],b[1])

		if c != (247,247,247):
			gui.click(b)
			winsound.Beep(1800,2000)
			print('Attention!')		
			sleep(25)
		else:
			print(i)
		sleep(25)
		i+=1
	except:
		print('Trying agian')
		winsound.Beep(2200,50)
		sleep(15)
		#continue
