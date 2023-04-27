from machine import Pin, PWM
from PhyComProtocol import Recieve, Send, Peek
from LED import playerColour, lights
import time
import random
import gc

gc.collect()
gc.enable()

time_playerout = 20000000000

def playerStatus(ExpectedID, colour, RecFlag):
    if RecFlag == 1:
        playerColour(colour)
        RecPlayerID = 0
        time1 = time.time_ns()
        while(time.time_ns() - time1 < time_playerout):
            lights(colour)
            RecPlayerID = Recieve()
            if RecPlayerID == ExpectedID:
                lights("white")
                for i in range(5):
                    Send()
                return True
            elif (RecPlayerID != 0 and RecPlayerID != 333 and RecPlayerID != 666):
                lights("off")
                for i in range(2):
                    Send()
                RecPlayerID = 0
        lights("red")
        return False
    
    elif RecFlag == 0:
        RecPlayerID = 0
        playerColour(colour)
        time1 = time.time_ns()
        while(time.time_ns() - time1 < time_playerout):
            lights(colour)
            Send()
            if Peek() == True:
                while(time.time_ns() - time1 < time_playerout):
                    RecPlayerID = Recieve()
                    if RecPlayerID == ExpectedID:
                        lights("white")
                        return True
                    elif (RecPlayerID == 333 or RecPlayerID == 666):
                        RecPlayerID = Recieve()
                    elif (RecPlayerID != 0 and RecPlayerID != 333 and RecPlayerID != 666):
                        lights("off")
                        time.sleep(0.5)
                        break
                    else:
                        pass
        lights("red")
        return False