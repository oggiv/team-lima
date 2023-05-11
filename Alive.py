from machine import Pin, PWM
from PhyCom import Receive, Send, Peek
from LED import playerColour, lights
import time
import random
import gc

gc.collect()
gc.enable()

def playerStatus(ExpectedID, colour, time_playerout, SWcolour): # Method used to process the physical communication between units
    RecPlayerID = 0 # Initialize variable to store Received ID
    playerColour(SWcolour) # Run lightshow and display given pair colour
    time1 = time.time_ns()
    while(time.time_ns() - time1 < time_playerout): # While round timer is not exceeded
        if (time.time_ns() - time1 < 3000000000):
            lights(SWcolour) # Display switcharoo colour first 3 seconds
        else:
            lights(colour) # Display given pair colour
        time.sleep((0.5 * random.random()))
        if Peek() == False:
            Send() # Send ID on the bitstream
        elif Peek() == True: # If any information is Received on the bitstream:
            while(time.time_ns() - time1 < time_playerout):
                RecPlayerID = Receive() # Read value off bitstream
                if RecPlayerID == ExpectedID: # If read value is equivalent to the partner in the same pair:
                    lights("white") # Display WHITE colour
                    for i in range(5): # Send THIS units ID a couple of times
                        Send()
                    return True
                elif (RecPlayerID == 333 or RecPlayerID == 666): # If a bad read was conducted:
                    RecPlayerID = Receive() # Read value off bitstream
                elif (RecPlayerID != 0 and RecPlayerID != 333 and RecPlayerID != 666): # If read value is another unit NOT equivalent to partner:
                    Send()
                    for x in range(3):
                        lights("off") # Display NO colour
                        time.sleep(0.15)
                        lights(colour) # Display given pair colour
                        time.sleep(0.15)
                    break # Return to send data
                else:
                    break
    lights("red") # Time exceeded limit, Display red colour
    return False

def outOfRound():
    lights("lightshow")
    playerColour("off") # Run lightshow and display given pair colour
    return True
    
