# using signals to get out of an infinite loop
# Signal used is Signals.SIGINT:  CTRL + C

import signal # Import signal module using the import keyword
import time   # available signals on your system

Sentry = True

# Create a Signal Handler for Signals.SIGINT:  CTRL + C 
def SignalHandler_SIGINT(SignalNumber,Frame):
    print('SignalHandler of signal.SIGINT')
    #print(f'Signal Number -> {SignalNumber} Frame -> {Frame}')
    global Sentry
    Sentry = False

signal.signal(signal.SIGINT,SignalHandler_SIGINT) #register the signal handler

while Sentry:
    print('Long continous event Eg,Read from sensor,Press CTRL+C to exit')
    time.sleep(1)

print('Out of the while loop')
print('Clean up Here')