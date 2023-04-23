from machine import Pin
from utime import sleep 

freq = 0.1 #Given time between writes/reads, needs to be same on all units
ID = 0x84 #Unique identification of each glove

def sender():
    output1 = Pin(4, Pin.OUT, Pin.PULL_DOWN) #Setting up transmission
    tempID = ID
#####################################
# Extracting bits to binary signals #    
#####################################
    out_bit0 = (tempID & 0x01)      # 
    tempID = (tempID >> 1)          #
    out_bit1 = (tempID & 0x01)      #
    tempID = (tempID >> 1)          #
    out_bit2 = (tempID & 0x01)      #
    tempID = (tempID >> 1)          #
    out_bit3 = (tempID & 0x01)      #
    tempID = (tempID >> 1)          #
    out_bit4 = (tempID & 0x01)      #
    tempID = (tempID >> 1)          #
    out_bit5 = (tempID & 0x01)      #
    tempID = (tempID >> 1)          #
    out_bit6 = (tempID & 0x01)      #
    tempID = (tempID >> 1)          #
    out_bit7 = (tempID & 0x01)      #
    tempID = (tempID >> 1)          #
#####################################
    
    while True: #Send signal
        output1.on() 
        sleep(freq * 10) #send 10 high bits
        
################################
# Sending byte according to ID #
################################
        if out_bit7 == 1:      #
            output1.on()       #
            sleep(freq)        #
            output1.off()      #
            sleep(freq)        #
        elif out_bit7 == 0:    #
            output1.off()      #
            sleep(freq)        #
            output1.on()       #
            sleep(freq)        #
                               #
        if out_bit6 == 1:      #
            output1.on()       #
            sleep(freq)        #
            output1.off()      #
            sleep(freq)        #
        elif out_bit6 == 0:    #
            output1.off()      #
            sleep(freq)        #
            output1.on()       #
            sleep(freq)        #
                               #
        if out_bit5 == 1:      #
            output1.on()       #
            sleep(freq)        #
            output1.off()      #
            sleep(freq)        #
        elif out_bit5 == 0:    #
            output1.off()      #
            sleep(freq)        #
            output1.on()       #
            sleep(freq)        #
                               #
        if out_bit4 == 1:      #
            output1.on()       #
            sleep(freq)        #
            output1.off()      #
            sleep(freq)        #
        elif out_bit4 == 0:    #
            output1.off()      #
            sleep(freq)        #
            output1.on()       #
            sleep(freq)        #
                               #
        if out_bit3 == 1:      #
            output1.on()       #
            sleep(freq)        #
            output1.off()      #
            sleep(freq)        #
        elif out_bit3 == 0:    #
            output1.off()      #
            sleep(freq)        #
            output1.on()       #
            sleep(freq)        #
                               #
        if out_bit2 == 1:      #
            output1.on()       #
            sleep(freq)        #
            output1.off()      #
            sleep(freq)        #
        elif out_bit2 == 0:    #
            output1.off()      #
            sleep(freq)        #
            output1.on()       #
            sleep(freq)        #
                               #
        if out_bit1 == 1:      #
            output1.on()       #
            sleep(freq)        #
            output1.off()      #
            sleep(freq)        #
        elif out_bit1 == 0:    #
            output1.off()      #
            sleep(freq)        #
            output1.on()       #
            sleep(freq)        #
                               #
        if out_bit0 == 1:      #
            output1.on()       #
            sleep(freq)        #
            output1.off()      #
            sleep(freq)        #
        elif out_bit0 == 0:    #
            output1.off()      #
            sleep(freq)        #
            output1.on()       #
            sleep(freq)        #
################################
sender()