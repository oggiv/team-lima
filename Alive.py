from machine import Pin, PWM
from PhyComProtocol import Recieve, Send, Peek
from LED import playerColour, lights
import time
import random
import gc

gc.collect()
gc.enable()

time_playerout = 20000000000 # Param used to define starting time limit

def playerStatus(ExpectedID, colour, RecFlag, time_decrement): #Recieve expected partners ID, colour, whether this unit should send/recieve and timechange. 
    if RecFlag == 1: # If this unit is a reciever:
        playerColour(colour) # Conduct Lightshow and display given colour
        RecPlayerID = 0
        time1 = time.time_ns()
        while(time.time_ns() - time1 < time_playerout): # while player is not out of game:
            lights(colour) # show light in given colour
            RecPlayerID = Recieve() # Check what hand is currently being shook
            if RecPlayerID == ExpectedID: # If the hand shook is the one expected
                lights("white") 
                for i in range(5): # Send my ID to the other unit X times
                    Send()
                return True # Return True
            elif (RecPlayerID != 0 and RecPlayerID != 333 and RecPlayerID != 666): # If the hand shook is a hand but not the one expected:
                lights("off") # Turn led off
                for i in range(2): # Send my ID to the other unit X times
                    Send()
                RecPlayerID = 0 # Return to loop
        lights("red") # Time is up and correct hand is not shook, show red light
        return False # Return False
    
    elif RecFlag == 0: # If this unit is a sender:
        RecPlayerID = 0
        playerColour(colour) # Conduct Lightshow and display given colour
        time1 = time.time_ns()
        while(time.time_ns() - time1 < time_playerout): # while player is not out of game:
            lights(colour) # show light in given colour
            Send() # send ID a couple of times (50?) on the stream
            if Peek() == True: # If someone else send information on the bitstream:
                while(time.time_ns() - time1 < time_playerout): # while player is not out of game:
                    RecPlayerID = Recieve() # Check what hand is currently being shook
                    if RecPlayerID == ExpectedID: # If the hand shook is the one expected
                        lights("white")
                        return True # Return True
                    elif (RecPlayerID == 333 or RecPlayerID == 666): # If a bad read was conducted
                        RecPlayerID = Recieve()
                    elif (RecPlayerID != 0 and RecPlayerID != 333 and RecPlayerID != 666): # If the hand shook is incorrect
                        lights("off") # Turn leds off
                        time.sleep(0.5) 
                        break # Go back to send data (as long as theres time left)
                    else:
                        pass
        lights("red") # Time is up, show red light
        return False # Return False