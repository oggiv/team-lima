from machine import Pin, PWM
import time
import random
import gc

#gc.collect()
#gc.enable()

# Toggling pins for each colour
Led_R = PWM(Pin(2))
Led_G = PWM(Pin(8))
Led_B = PWM(Pin(12))

# Define the frequency
Led_R.freq(2000)
Led_G.freq(2000)
Led_B.freq(2000)


# Method used to toggle each colour
def rgb(a, b, c):
    Led_R.duty_u16(a * 257)
    Led_G.duty_u16(b * 257)
    Led_B.duty_u16(c * 257)
    
# Definition of prebuilt colours
def lights(colour):
    
    if (colour == "off" or colour == "all"):
         rgb(0, 0, 0)
         if(colour == "all"):
             time.sleep(1)
    
    if (colour == "white" or colour == "all"):
         rgb(255, 255, 200)
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
         rgb(255, 50, 0)
         if(colour == "all"):
             time.sleep(1)
         
    if (colour == "purple" or colour == "all"):
         rgb(255, 0, 255)
         if(colour == "all"):
             time.sleep(1)
         
    if (colour == "cyan" or colour == "all"):
         rgb(0, 80, 120)
         if(colour == "all"):
             time.sleep(1)
    
    if (colour == "orange" or colour == "all"):
        rgb(255, 18, 0)
        if(colour == "all"):
            time.sleep(1)
            
    if (colour == "pink" or colour == "all"):
        rgb(255, 40, 60)
        if(colour == "all"):
            time.sleep(1)
             
    if (colour == "lightshow"):
        
        for x in range(3):
            b = 0.001
            for i in range(255):
                rgb(255, i, 0)
                time.sleep(b)
        
            for j in range(255, 0, -1):
                rgb(j, 255, 0)
                time.sleep(b)
        
            for k in range(255):
                rgb(0, 255, k)
                time.sleep(b)
                
            for m in range(255, 0, -1):
                rgb(0, m, 255)
                time.sleep(b)
                
            for n in range(255):
                rgb(n, 0, 255)
                time.sleep(b)
                
            for o in range(255, 0, -1):
                rgb(255, 0, o)
                time.sleep(b)
    
    if (colour == "gameover"):
        b = 0.005
        for x in range(5):
            time.sleep(0.1)
            for i in range(255):
                rgb(255, i, i)
                time.sleep(b)
            rgb(255, 0, 0)
    
    if (colour == "connected"):
        b = 0.005
        for x in range(5):
            time.sleep(0.1)
            for i in range(255):
                rgb(i, i, 255)
                time.sleep(b)
            rgb(0, 0, 255)
            
    if (colour == "lostlife"):
        b = 0.003
        for x in range(7):
            #time.sleep(0.1)
            for i in range(255):
                rgb(i, 0, 0)
                time.sleep(b)
            rgb(255, 0, 0)

def playerColour(ID): # Run the lightshow and then present the given playercolour
    lights("lightshow")
    lights(ID)

# generates nr_of_pairs amount of colours in the array colours
# array consists of (x, y, z) values as tuples
# usage: rgb(colours[0][0], colours[0][1], colours[0][2])
def random_colour(nr_of_pairs):
    r = 0
    g = 0
    b = 0
    
    func = [r, g, b]
    colours = []
    
    # add all colours to return array
    for i in range(0, nr_of_pairs):
        x = random.randint(0, 255)
        print(x)
        
        # add the rgb value to the operating function
        func[i % 3] = (func[i % 3] + x) % 255
        
        if i > 2:
            while True:
                abs_i = (i-1) % 3
                # #2
                if (abs(func[i % 3] - func[abs_i]) < 70):
                   x = random.randint(0, 255)
                   func[i % 3] = (func[i % 3] + x) % 255
                # #3
                abs_i = (i-2) % 3
                if (abs(func[i % 3] - func[abs_i])):
                   x = random.randint(0, 255)
                   func[i % 3] = (func[i % 3] + x) % 255
                else:
                    break
                
                func[i % 3] = (func[i % 3] + x) % 255
                print(abs(func[i % 3] - func[abs_i]))
            
        # place func into array
        colours.append((func[0], func[1], func[2]))
    return(colours)

    
clr = random_colour(5)
print(clr)

rgb(clr[0][1], clr[0][0], clr[0][2])
time.sleep(1)

rgb(clr[1][1], clr[1][0], clr[1][2])
time.sleep(1)

rgb(clr[2][1], clr[2][0], clr[2][2])
time.sleep(1)

rgb(clr[3][1], clr[3][0], clr[3][2])
time.sleep(1)

rgb(clr[4][1], clr[4][0], clr[4][2])
time.sleep(1)