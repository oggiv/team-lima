#SYNKA
    Lista av connections som snackar med hubben
    if(connection == true)
    light all lights in the same colour
    

    #kanske går att ha en Connect method som tar
    #en client som parameter?
    #så ha en lista med unconnected och en lista
    #med connected. flytt från ena till andra
    #successivt
#break down into pseudo code

#HEALTH och HP
     Health = 3 (3 liv)
     
#TIMER
    Timer = 10; (t ex)

#HANDSHAKE
# COME BACK TO
    X = 0;
    while(X == 0)
    keep checking if connection is established
    if (connection established)
    X = 1;
    #break down into pseudo code

#COUNTDOWN
if (sensor detects handhake) --> countdown == true;

#Väldigt simpelt exempel
while true:
  led1.on()
  led2.on()
  led3.on()
  led4.on()
  sleep(1)
  led1.off()
  sleep(1)
  led2.off()
  sleep(1)
  led3.off()
  sleep(1)
  led4.off()
  sleep(1)
  break

#kanske bättre med en rgb led som dimmas, färre pins
#som går åt?
from machine  import Pin
from utime import sleep

red = Pin(16, Pin.OUT)
green = Pin(18, Pin.OUT)
blue = Pin(20, Pin.OUT)

while True:
  red.value(0) # red
  green.value(1)
  blue.value(1)
  sleep(1)
  red.value(0) # yellow
  green.value(0)
  blue.value(1)
  sleep(1)
  red.value(1) # green
  green.value(0)
  blue.value(1)
  sleep(1)
  for i in range(8):
      red.value(1) 
      green.value(1)
      blue.value(1)
      sleep(0.1)
      red.value(1)
      green.value(0)
      blue.value(1)
      sleep(0.1)
  
  sleep(1)
  
#går åt lika många pins men snyggare kanske
#sekvensen är röd -> gul -> grön sen blinka grön snabbt

#MATCHA PAR
    Lista av handskar
    bocka av vilka handskar som har vilken färg och därmed matchar
    OBS! Max 2 handskar med samma färg
    Färg ID:ar par som ska kopplas fysiskt
    Rundan startar, timer räknar ner 
    #break down into pseudo code
    

#MATCHA
    Kolla att fysisk kontakt etableras # Interrupt request?
    #irq för den pin som sensorn är på?
    Kolla handske 1 ID (färg) och sedan handske 2 ID
    Se om ID 1 = ID 2, då är handskakningen korrekt
    Flasha gröna lampor
    Gå till lyckad runda
    Om nej
    Flasha röda lampor
    if HP > 0, decrement HP with 1
    Gå till ny runda
    else GAME OVER
    
#LYCKAD RUNDA
    Timer - 1;
    Gå tillbaka till matcha par
    
#NY RUNDA
    Resetta
    Gå till matcha par
    Spelat har börjat om igen

#GAME OVER
    Blinka lampor random
    Spelet är över
    Resetta till skaka hand 
    Skaka hand för att börja om
    
    
    
    
    

