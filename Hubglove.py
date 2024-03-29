import wireless
import random
import time
from PhyComProtocol import ID, Handtype
from Alive import playerStatus
from LED import lights

Colours = ["green", "blue", "yellow", "purple", "cyan", "orange"] # List of available colours
thisID = ID() # Extract this gloves ID

def randomize_list(original_list):
    # Create a new list with the same elements as the original list
    randomized_list = original_list[:]

    # Shuffle the elements of the new list using the Fisher-Yates shuffle algorithm
    for i in range(len(randomized_list) - 1, 0, -1):
        j = random.randint(0, i)
        randomized_list[i], randomized_list[j] = randomized_list[j], randomized_list[i]

    # Return the new list with randomized values
    return randomized_list

def Hub(ssid):
    # create a hub object
    hub = wireless.Hub()

    # start wifi that clients can connect to
    # start_wifi(network name, password)
    hub.start_wifi(ssid, '12345678')

    # check if wifi is running like it should
    print(hub.wifi_is_active())

    # accept socket connections from clients 
    connections = []

    try: # accept connections until socket is timed out
        while True: 
            connections.append(hub.accept_connection())
    except OSError: # Catch socket timeout
        print("no more clients")
        pass

    # ID list and handtype lists
    ID = []
    RHands = []
    LHands = []

    for i in range(len(connections)): # For all connected units
        ID.append(int(connections[i].receive(256))) # Recieve ID as an integer
        HAND = connections[i].receive(100) # Recieve Handtype as a string
        if HAND == "right": # If hand is right
            RHands.append(ID[i]) # Append its ID to the list of right hands
        elif HAND1 == "left": # If hand is left
            LHands.append(ID[i]) # Append its ID to the list of left hands

    decrement = 20000000000 # Initializing round timer
    lives = 3 # Initializing game lives
    Gameover = False # Initializing game status flag
    RSinceSwaroo = 0

    while hub.wifi_is_active(): # While we are a hub
        PairsAmountR = 0
        PairsAmountL = 0
        switcharooR = 0
        switcharooL = 0

    # Lists in which pairs are created
        PairH1 = []
        PairH2 = []
        PairV1 = []
        PairV2 = []

        if len(RHands) > 0: # If any right hands are connected 
            randompairs = randomize_list(RHands) # Randomize the list of their IDs
            if len(randompairs) >= 1: # If there exists one unassigned right hand
                PairH1.append(randompairs.pop(0)) # Append pair with this hubgloves ID
            if len(randompairs) >= 1: # If there exists one unassigned right hand
                PairH1.append(randompairs.pop(0)) # Append pair with the first randomized ID
                PairsAmountR = PairsAmountR + 1
            if len(randompairs) >= 1: # If there exists two more unassigned right hands
                PairH2.append(randompairs.pop(0)) # Append pair with the next randomized ID
            if len(randompairs) >= 1: # If there exists one unassigned right hand
                PairH2.append(randompairs.pop(0)) # Append pair with the next randomized ID
                PairsAmountR = PairsAmountR + 1

        if len(LHands) > 0: # If any left hands are connected
            randompairs = randomize_list(LHands) # Randomize the list of their IDs
            if len(randompairs) >= 1: #If there exists two unassigned left hands
                PairV1.append(randompairs.pop(0)) # Append pair with the first randomized ID
            if len(randompairs) >= 1: #If there exists two unassigned left hands
                PairV1.append(randompairs.pop(0)) # Append pair with the next randomized ID
                PairsAmountL = PairsAmountL + 1
            if len(randompairs) >= 1: # If there exists two more unassigned left hands
                PairV2.append(randompairs.pop(0)) # Append pair with the next randomized ID
            if len(randompairs) >= 1: #If there exists two unassigned left hands
                PairV2.append(randompairs.pop(0)) # Append pair with the next randomized ID
                PairsAmountL = PairsAmountL + 1

        randomColour = randomize_list(Colours) # Randomize the list of colours
        ClrP1 = randomColour.pop(0) # Extract one colour
        ClrP2 = randomColour.pop(0) # Extract another colour
        ClrP3 = randomColour.pop(0) # Extract another colour
        ClrP4 = randomColour.pop(0) # Extract another colour
        
        if PairsAmountR >= 2: # If there are more than 2 right hands
            switcharooR = random.randint(0, 10 - RSinceSwaroo) # Returns random value between 0 and 10-1
            if switcharooR == 1: # If the random value is 1
                decrement = decrement + 2000000000 # Add time to the round
                RSinceSwaroo = 0 # Reset the chance of a switcharoo 
        elif PairsAmountL >= 2: # If there are more than 2 left hands
            switcharooL = random.randint(0, 10 - RSinceSwaroo) # Returns random value between 0 and 10-1
            if switcharooL == 1: # If the random value is 1
                RSinceSwaroo = 0 # Reset the chance of a switcharoo
                if switcharooR != 1: # If right switcharoo is not occuring
                    decrement = decrement + 2000000000 # Add time to the round
        
        
    ##########################################################
    ##  Check which connection each id belongs to and send  ##
    ##   their partners ID, pair colour, round timer and    ##
    ##                  switcharoo colour                   ##
    ##########################################################
        for i in range(len(ID)):                            ##
            if PairH1[1] == ID[i]:                          ##
                connections[i].send(str(PairH1[0]))         ##
                connections[i].send(ClrP1)                  ##
                connections[i].send(decrement)              ##
                if switcharooR == 1:                        ##
                    connections[i].send(ClrP2)              ##
                else:                                       ##
                    connections[i].send(ClrP1)              ##
                                                            ##
        if len(PairH2) == 2:                                ##
            for i in range(len(ID)):                        ##
                if PairH2[0] == ID[i]:                      ##
                    connections[i].send(str(PairH2[1]))     ##
                    connections[i].send(ClrP2)              ##               
                    connections[i].send(decrement)          ##
                    connections[i].send(ClrP2)              ##
            for i in range(len(ID)):                        ##
                if PairH2[1] == ID[i]:                      ##
                    connections[i].send(str(PairH2[0]))     ##
                    connections[i].send(ClrP2)              ##                
                    connections[i].send(decrement)          ##
                    if switcharooR == 1:                    ##
                        connections[i].send(ClrP1)          ##
                    else:                                   ##
                        connections[i].send(ClrP2)          ##
        elif len(PairH2) == 1:                              ##
            for i in range(len(ID)):                        ##
                if PairH2[0] == ID[i]:                      ##
                    connections[i].send(0)                  ##
                    connections[i].send(0)                  ##               
                    connections[i].send(0)                  ##
                    connections[i].send(0)                  ##
                                                            ##
        if len(PairV1) == 2:                                ##
            for i in range(len(ID)):                        ##
                if PairV1[0] == ID[i]:                      ##
                    connections[i].send(str(PairV1[1]))     ##
                    connections[i].send(ClrP3)              ##
                    connections[i].send(decrement)          ##
                    connections[i].send(ClrP3)              ##                                                            
            for i in range(len(ID)):                        ##
                if PairV1[1] == ID[i]:                      ##
                    connections[i].send(str(PairV1[0]))     ##
                    connections[i].send(ClrP3)              ##
                    connections[i].send(decrement)          ##
                    if switcharooL == 1:                    ##
                        connections[i].send(ClrP4)          ##
                    else:                                   ##
                        connections[i].send(ClrP3)          ##
        elif len(PairV1) == 1:                              ##
            for i in range(len(ID)):                        ##
                if PairV1[0] == ID[i]:                      ##
                    connections[i].send(0)                  ##
                    connections[i].send(0)                  ##               
                    connections[i].send(0)                  ##
                    connections[i].send(0)                  ##
                                                            ##
        if len(PairV2) == 2:                                ##
            for i in range(len(ID)):                        ##
                if PairV2[0] == ID[i]:                      ##
                    connections[i].send(str(PairV2[1]))     ##
                    connections[i].send(ClrP4)              ##
                    connections[i].send(decrement)          ##
                    connections[i].send(ClrP4)              ##  
            for i in range(len(ID)):                        ##
                if PairV2[1] == ID[i]:                      ##
                    connections[i].send(str(PairV2[0]))     ##
                    connections[i].send(ClrP4)              ##
                    connections[i].send(decrement)          ##
                    if switcharooL == 1:                    ##
                        connections[i].send(ClrP3)          ##
                    else:                                   ##
                        connections[i].send(ClrP4)          ##
        elif len(PairV2) == 1:                              ##
            for i in range(len(ID)):                        ##
                if PairV2[0] == ID[i]:                      ##
                    connections[i].send(0)                  ##
                    connections[i].send(0)                  ##               
                    connections[i].send(0)                  ##
                    connections[i].send(0)                  ##
    ##########################################################
    ##########################################################
                    
        flag = True # Parameter used for determining whether the handshakes were successful
        successfulHandshake = playerStatus(PairH1[1], ClrP1, decrement, ClrP1) # Check if THIS handshake was successful
        print("done w shaking hands")
        if not successfulHandshake: # If THIS handshake was unsuccessful:
            flag = False

        for i in range(len(connections)): # Check if all units conducted a successful handshake:
            response = connections[i].receive(100) # Retrieve one response
            print("Response" + str(i) + ": " + response)
            if response == "False": # If response was false:
                flag = False

        if flag == False: # If any of the handshakes were unsuccessful
            lives = lives - 1 # Subtract one life
            for i in range(len(connections)): # Send "loselife" to all units
                    connections[i].send("loselife")
            lights("lostlife") # Run "lostlife" lightshow on THIS unit (the hub unit)
            if lives == 0:
                for i in range(len(connections)): # Send "gameover" to all units
                    connections[i].send("gameover")
                    print("Sent " + str(i))
                lights("gameover") # Run "gameover" lightshow on THIS unit (the hub unit)
                Gameover = True
                
        elif flag == True: # If none of the handshakes were unsuccessful
            for i in range(len(connections)): # Send "continue" to all units
                    connections[i].send("continue")
            
        if Gameover == True: # If game is over:
            break # Break game loop
        
        elif Gameover == False: # If game is not over:
            for i in range(len(connections)): # Send "continue" to all units
                connections[i].send("continue")
                
        if (decrement >= 7000000000) and (flag == True): # Reduce round timer if round was successful and roundtimer is larger than 7s        
            decrement = decrement - 1000000000 # Reduce round timer
        if (RSinceSwaroo < 9): # Edge case for random function
            RSinceSwaroo = RSinceSwaroo + 1 # Increment rounds since switcharoo counter

    # close the connection, happens when game loop is broken
    print("out")
    for i in range(len(connections)):
        connections[i].close()
        
