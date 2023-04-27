from machine import Pin
from utime import sleep 
import gc

gc.collect()
gc.enable()

def ID(): #Unique identification of each glove
    return 225
def Handtype():
    return "right"

freq = 0.001 #Given time between writes/reads, needs to be same on all units

def Send(): #Run send operation
    output1 = Pin(4, Pin.OUT, Pin.PULL_DOWN) #Setting up transmission
    tempID = ID()
    
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
    
    for i in range(10): #Send signal
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

def Recieve():
    input1 = Pin(4, Pin.IN, Pin.PULL_DOWN) #Setting up transmission
    inputstream = [] #Input stream is stored in this array
    ID_Rec = [] #Used to extract the bit value
    
    for i in range(50): #Read 50 bits
        inputstream.append(input1.value())
        sleep(freq)
    #print(inputstream)
    if inputstream: #If array is not empty (edge case for compilation only)
        bit1 = inputstream.pop(0) #Extract bit from stream
        bit2 = inputstream.pop(0) #Extract bit from stream
        bit3 = inputstream.pop(0) #Extract bit from stream
        bit4 = inputstream.pop(0) #Extract bit from stream
        
        flag_decode = True #Used as interrupt whenever decode of stream is finished
        while flag_decode:
            
            if (bit1 == 1) and (bit2 == 1) and (bit3 == 1) and (bit4 == 0): #If start signal is found
                ID_Rec.append(1) #Add first bit to read value
                
                for j in range(7): #Read the 7 following bits (14 since theyre encoded as pairs)
                    if inputstream: #If array is not empty (edge case for compilation only)
                        bit1_1 = inputstream.pop(0) #Extract 1 bit
                    else:
                        print("Error 1")
                        return 0
                    
                    if inputstream: #If array is not empty (edge case for compilation only)
                        bit2_1 = inputstream.pop(0) #Extract 1 more bit
                        
                        if (bit1_1 == 1) and (bit2_1 == 0): #If bits are sequentially 1 and 0
                            ID_Rec.append(1) #add 1 as decoded and read bit
                        elif (bit1_1 == 0) and (bit2_1 == 1): #If bits are sequentially 0 and 1
                            ID_Rec.append(0) #add 0 as decoded and read bit
                        elif (bit1_1 == 1) and (bit2_1 == 1): #If bits are sequentially 1 and 1
                            ID_Rec.append(9) #add 9 as detected error bit
                        elif (bit1_1 == 0) and (bit2_1 == 0): #If bits are sequentially 0 and 0
                            ID_Rec.append(9) #add 9 as detected error bit
                    else:
                        print("Error 2")
                        return 0     
                flag_decode = False #1 byte is extracted --> return
                
            else: #If start signal was not found, look at next bits of stream
                if inputstream:
                    bit1 = bit2
                    bit2 = bit3
                    bit3 = bit4
                    bit4 = inputstream.pop(0)
                else: #If connection is lost between units
                    print("Connection lost")
                    return 0
            
        read_value = 0 #Variable in which the final numeric value is stored to
        
        out_bit0 = ID_Rec[0] #MSB
        out_bit1 = ID_Rec[1]
        out_bit2 = ID_Rec[2]
        out_bit3 = ID_Rec[3]
        out_bit4 = ID_Rec[4]
        out_bit5 = ID_Rec[5]
        out_bit6 = ID_Rec[6]
        out_bit7 = ID_Rec[7] #LSB
        
        valid_byte = out_bit0 + out_bit1 + out_bit2 + out_bit3 + out_bit4 + out_bit5 + out_bit6 + out_bit7 #Sum up values
        if valid_byte <= 8: #If read value has no error bits; begin extraction from binary to decimal
            if out_bit7 == 1:
                read_value = read_value + 1 
            if out_bit6 == 1:
                read_value = read_value + 2            
            if out_bit5 == 1:
                read_value = read_value + 4
            if out_bit4 == 1:
                read_value = read_value + 8
            if out_bit3 == 1:
                read_value = read_value + 16
            if out_bit2 == 1:
                read_value = read_value + 32
            if out_bit1 == 1:
                read_value = read_value + 64    
            if out_bit0 == 1:
                read_value = read_value + 128
        elif valid_byte <= 26: #If read value has max 2 error bits
            read_value = 333
            print("Bad read")
        elif valid_byte > 26: #If read value has 3-8 error bits
            read_value = 666
            print("Bad read")
    return read_value #Return read value or error indication

def Peek():
    input1 = Pin(4, Pin.IN, Pin.PULL_DOWN) #Setting up transmission
    inputstream = [] #Input stream is stored in this array
    ID_Rec = [] #Used to extract the bit value
    
    for i in range(10): #Read 10 bits
        inputstream.append(input1.value())
        sleep(freq)
    
    for i in range(10):
        if inputstream.pop(0) == 1:
            return True
    return False
       
    