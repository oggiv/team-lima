from machine import Pin
from utime import sleep
import time

freq = 0.1 #x s between writes/reads

def reciever():
    input1 = Pin(4, Pin.IN, Pin.PULL_UP)
    inputstream = []
    ID = []
    rValues = []
    
    time1 = time.time()
    while time.time() - time1 < 1:
        inputstream.append(input1.value())
        sleep(freq)
    
    for i in range(5)
        
        bit1 = inputstream.pop(0)
        bit2 = inputstream.pop(0)
        bit3 = inputstream.pop(0)
        bit4 = inputstream.pop(0)
        
        flag_decoded = 0
        while flag_decoded = 0:
            
            if (bit1 == 1) and (bit2 == 1) and (bit3 == 1) and (bit4 == 0):
                ID.append(1)
                
                bit1 = inputstream.pop(0)
                bit2 = inputstream.pop(0)
                bit3 = inputstream.pop(0)
                bit4 = inputstream.pop(0)
                
                for j in range(7): #kan gå igenom 7 gånger bara?
                    bit1_1 = inputstream.pop(0)
                    bit2_1 = inputstream.pop(0)
                    
                    if (bit1_1 == 1) and (bit2_1 == 0):
                        ID.append(1)
                        
                    elif (bit1_1 == 0) and (bit2_1 == 1):
                        ID.append(0)
                        
                flag_decoded = 1
                
            else:
                bit1 = bit2
                bit2 = bit3
                bit3 = bit4
                bit4 = inputstream.pop(0)
        
        read_value = 0
        
        out_bit0 = ID[0] #MSB
        
        out_bit1 = ID[1]
        
        out_bit2 = ID[2]
       
        out_bit3 = ID[3]
        
        out_bit4 = ID[4]
        
        out_bit5 = ID[5]
        
        out_bit6 = ID[6]
        
        out_bit7 = ID[7] #LSB
        
        if out_bit7 == 1:
            read_value = read value + 1 
        if out_bit6 == 1:
            read_value = read value + 2            
        if out_bit5 == 1:
            read_value = read value + 4
        if out_bit4 == 1:
            read_value = read value + 8
        if out_bit3 == 1:
            read_value = read value + 16
        if out_bit2 == 1:
            read_value = read value + 32
        if out_bit1 == 1:
            read_value = read value + 64    
        if out_bit0 == 1:
            read_value = read value + 128
            
        rValues.append(read_value)
        
    return rValues

def test():
    output1 = Pin(10, Pin.OUT)
    
    while True:
        array = reciever()
        for i in range(5)
            if array[i] == 0x84
                output1.on()
                sleep(1)
            else
                output1.off()
                sleep(1)
                
test()
            
    
            
