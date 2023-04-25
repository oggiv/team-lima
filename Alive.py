from machine import Pin, PWM
from PhyComProtocol import Recieve, Send
from LED import playerColour, lights
import time
import random
import gc

playerStatus(132, "green", 1)

def playerStatus(ExpectedID, colour, RecFlag):
    if RecFlag == 1:
        playerColour(colour)
        RecPlayerID = 0
        time1 = time.time_ns()
        while(time.time_ns() - time1 < 10000000000):
            lights(colour)
            RecPlayerID = Recieve()
            if RecPlayerID == ExpectedID:
                lights("white")
                return True
            if (RecPlayerID != 0 or RecPlayerID != 333 or RecPlayerID != 666):
                lights("off")
                RecPlayerID = 0
        return False        
    elif RecFlag == 0:
        playerColour(colour)
        time1 = time.time_ns()
        while(time.time_ns() - time1 < 10000000000):
            Send()
    
