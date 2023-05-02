from machine import Pin, PWM
from PhyComProtocol import Recieve, Send, Peek
from LED import playerColour, lights
import time
import random
import gc

gc.collect()
gc.enable()

def playerStatus(ExpectedID, colour, RecFlag, time_playerout): # Method used to process the physical communication between units
    if RecFlag == 1: # If THIS unit is a RECEIVER:
        playerColour(colour) # Run initial lightshow and display colour
        RecPlayerID = 0 # Initializing variable to store recieved ID over bitbanger link
        time1 = time.time_ns()
        while(time.time_ns() - time1 < time_playerout): # While round timer is not exceeded
            lights(colour) # Display given pair colour
            RecPlayerID = Recieve() # Read value off the bitstream
            if RecPlayerID == ExpectedID: # If read value is equivalent to the partner in the same pair:
                lights("white") # Display WHITE colour
                for i in range(5): # Send THIS units ID a couple of times
                    Send()
                return True
            elif (RecPlayerID != 0 and RecPlayerID != 333 and RecPlayerID != 666): # If read value is another unit NOT equivalent to partner:
                lights("off") # Display NO colour
                for i in range(2): # Send THIS units ID 
                    Send()
                RecPlayerID = 0 # Reset variable
            Send() # Send THIS units ID (this in case the opposing hand is wrong and also a reciever)
        lights("red") # Time exceeded limit, Display red colour
        return False
    
    elif RecFlag == 0: # If THIS unit is a SENDER:
        RecPlayerID = 0 # Initialize variable to store recieved ID
        playerColour(colour) # Run lightshow and display given pair colour
        time1 = time.time_ns()
        while(time.time_ns() - time1 < time_playerout): # While round timer is not exceeded
            lights(colour) # Display given pair colour
            Send() # Send ID on the bitstream
            if Peek() == True: # If any information is recieved on the bitstream:
                while(time.time_ns() - time1 < time_playerout):
                    RecPlayerID = Recieve() # Read value off bitstream
                    if RecPlayerID == ExpectedID: # If read value is equivalent to the partner in the same pair:
                        lights("white") # Display WHITE colour
                        for i in range(5): # Send THIS units ID a couple of times
                        Send()
                        return True
                    elif (RecPlayerID == 333 or RecPlayerID == 666): # If a bad read was conducted:
                        RecPlayerID = Recieve() # Read value off bitstream
                    elif (RecPlayerID != 0 and RecPlayerID != 333 and RecPlayerID != 666): # If read value is another unit NOT equivalent to partner:
                        lights("off") # Display NO colour
                        time.sleep(0.3) # Delay next cycle
                        break # Return to send data
                    else:
                        pass
        lights("red") # Time exceeded limit, Display red colour
        return False