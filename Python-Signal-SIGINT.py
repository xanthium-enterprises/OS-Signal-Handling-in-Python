#OS Signal Handling in Python 3.x.x

#using Signals in Python 3.x.x

#Signals.SIGINT:  CTRL + C ,Default action is to raise KeyboardInterrupt.

#www.xanthium.in
 

import signal # Import signal module using the import keyword
import time   # available signals on your system

# Create a Signal Handler for Signals.SIGINT:  CTRL + C 
def SignalHandler_SIGINT(SignalNumber,Frame):
	print('SignalHandler of signal.SIGINT')
	print(f'Signal Number -> {SignalNumber} Frame -> {Frame}')
    

# Register the Signal Handler def SignalHandler_SIGINT() with the Signal       
# signal.signal(Signal Name,Name of Handler Function)
signal.signal(signal.SIGINT,SignalHandler_SIGINT) 



while 1:  
    print("Press Ctrl + C ") 
    time.sleep(1) 
