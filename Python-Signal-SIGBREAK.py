#OS Signal Handling in Python 3.x.x

#using Signals in Python 3.x.x
#Signals.SIGBREAK:Interrupt from keyboard (CTRL + BREAK).
#www.xanthium.in


# requires BREAK key on KeyBoard

import signal # Import signal module using the import keyword
import time   



   
#create a Signal Handler for Signals.SIGBREAK:(CTRL + BREAK)
def SignalHandler_SIGBREAK(SignalNumber,Frame):
	print('SignalHandler of signal.SIGBREAK')
	print(f'Signal Number -> {SignalNumber} Frame -> {Frame} ')
        
# Register the Signal Handler def SignalHandler_SIGBREAK() with the Signal       
# signal.signal(Signal Name,Name of Handler Function)
signal.signal(signal.SIGBREAK,SignalHandler_SIGBREAK)


while 1:  
    print("Press Ctrl + BREAK ") 
    time.sleep(1) 
