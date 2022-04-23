#using Signals in Python 3.x.x


#Signals.SIGBREAK:Interrupt from keyboard (CTRL + BREAK).
 

import signal # Import signal module using the import keyword
import time   # available signals on your system



   
#create a Signal Handler for Signals.SIGBREAK:(CTRL + BREAK)
def SignalHandler_SIGBREAK(SignalNumber,Frame):
	print('SignalHandler of signal.SIGBREAK')
	print(f'Signal Number -> {SignalNumber} Frame -> {Frame} ')
        

signal.signal(signal.SIGBREAK,SignalHandler_SIGBREAK)


while 1:  
    print("Press Ctrl + BREAK ") 
    time.sleep(1) 