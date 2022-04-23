#using Signals in Python 3.x.x

import signal    # Import signal module using the import keyword
import platform  # for identifying the OS 


# available signals on our System
valid_signals = signal.valid_signals()     # requires python 3.9.0
                                           # returns a SET
                                           
#print('Available Signals           ->',valid_signals)
print('Operating System            ->',platform.platform())
print('Number of Available Signals ->', len(valid_signals) , '\n')
for i in valid_signals:
    print(i)


