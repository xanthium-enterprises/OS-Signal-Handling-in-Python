#OS Signal Handling in Python 3.x.x
#Display available signals on our System
#www.xanthium.in

import signal    # Import signal module using the import keyword
import platform  # for identifying the OS 
import pprint    # for pretty print 

# available signals on our System
valid_signals = signal.valid_signals()     # requires python 3.9.0
                                           # returns a SET
                                           
#print('Available Signals           ->',valid_signals)
print('\n\nOperating System            ->',platform.platform())
print('Number of Available Signals ->', len(valid_signals) , '\n')

pprint.pprint(valid_signals)#using pretty print to display set datastructure



