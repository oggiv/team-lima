from machine import Pin, PWM
import time
import random
import gc

#gc.collect()
#gc.enable()


Led_R = PWM(Pin(2))
Led_G = PWM(Pin(8))
Led_B = PWM(Pin(12))

# Define the frequency
Led_R.freq(2000)
Led_G.freq(2000)
Led_B.freq(2000)

def rgb(a, b, c):
    Led_R.duty_u16(a * 257)
    Led_G.duty_u16(b * 257)
    Led_B.duty_u16(c * 257)
    
def lights(colour):
    
    if (colour == "off" or colour == "all"):
         rgb(0, 0, 0)
         if(colour == "all"):
             time.sleep(1)
    
    if (colour == "white" or colour == "all"):
         rgb(255, 255, 255)
         if(colour == "all"):
             time.sleep(1)
         
    if (colour == "red" or colour == "all"):
         rgb(255, 0, 0)
         if(colour == "all"):
             time.sleep(1)
         
    if (colour == "green" or colour == "all"):
         rgb(0, 255, 0)
         if(colour == "all"):
             time.sleep(1)
         
    if (colour == "blue" or colour == "all"):
         rgb(0, 0, 255)
         if(colour == "all"):
             time.sleep(1)
         
    if (colour == "yellow" or colour == "all"):
         rgb(255, 255, 0)
         if(colour == "all"):
             time.sleep(1)
         
    if (colour == "purple" or colour == "all"):
         rgb(255, 0, 255)
         if(colour == "all"):
             time.sleep(1)
         
    if (colour == "cyan" or colour == "all"):
         rgb(0, 255, 255)
         if(colour == "all"):
             time.sleep(1)
             
    if (colour == "lightshow"):
        
        for l in range(5):
            for i in range(255):
                rgb(255, i, 0)
                time.sleep(0.001)
        
            for j in range(255, 0, -1):
                rgb(j, 255, 0)
                time.sleep(0.001)
        
            for k in range(255):
                rgb(0, 255, k)
                time.sleep(0.001)
                
            for m in range(255, 0, -1):
                rgb(0, m, 255)
                time.sleep(0.001)
                
            for n in range(255):
                rgb(n, 0, 255)
                time.sleep(0.001)
                
            for o in range(255, 0, -1):
                rgb(255, 0, o)
                time.sleep(0.001)       
        rgb(0, 0, 0)
        
lights("lightshow")