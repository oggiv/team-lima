#SYNKA
    Lista av connections som snackar med hubben
    if(connection == true)
    light all lights in the same colour
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

while(true)
    flash all lights
    flash 3 lights
    flash 2 lights
    flash 1 light
    flash 0 lights
    break;
    #break down into pseudo code

#MATCHA PAR
    Lista av handskar
    bocka av vilka handksar som har vilken färg och därmed matchar
    OBS! Max 2 handskar med samma färg
    Färg ID:ar par som ska kopplas fysiskt
    Rundan startar, timer räknar ner 
    #break down into pseudo code
    

#MATCHA
    Kolla att fysisk kontakt etableras
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
    
    
    
    
    

