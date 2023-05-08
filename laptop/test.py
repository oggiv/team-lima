#SERVER
from playsound import playsound
import socket
import random

Colours = ["green", "blue", "yellow", "purple", "cyan", "orange"] # List of available colours

# Definition of Connection object
class Connection:
    
    # interfaces the socket connection
    def __init__(self, sock, address):
        self._socket = sock
        self.address = address
    
    def send(self, message):
        # sends message (which must be a str, int or float) over socket
        # message = string || integer || float, else -> TypeError
        # return -> None
        ty = type(message)
        if ty == str or ty == int or ty == float:
            encoded_message = str(message).encode('UTF-8') + b'\r'
            self._socket.sendall(encoded_message)
        else:
            raise TypeError("must be str, int or float, not %s" % ty)
    
    def receive(self, byte_count):
        # reads [bytes] amount of bytes from socket
        # bytes = integer, amount of bytes to receive
        # return -> string
        
        if byte_count == 0:
            byte_count = 2000
        
        data = b''
        bytes_read = 0
        
        while bytes_read < byte_count:
            byte = self._socket.recv(1)
            if byte == b'\r':
                break
            else:
                data += byte
                bytes_read += 1
        
        return data.decode('UTF-8')
    
    def close(self):
        # closes the socket connection
        # return -> None 
        self._socket.close()

def randomize_list(original_list):
    # Create a new list with the same elements as the original list
    randomized_list = original_list[:]

    # Shuffle the elements of the new list using the Fisher-Yates shuffle algorithm
    for i in range(len(randomized_list) - 1, 0, -1):
        j = random.randint(0, i)
        randomized_list[i], randomized_list[j] = randomized_list[j], randomized_list[i]

    # Return the new list with randomized values
    return randomized_list

def Main():
    
    # Set up AP within manually enabled hotspot
    print(socket.gethostname())
    Socket = socket.socket()
    Socket.bind(('0.0.0.0', 42))
    Socket.settimeout(30.0)
    Socket.listen(10)
    
    connections = []
    print(connections)
    try: # accept connections until socket is timed out
        while True:
            print("connect...")
            conn, addr = Socket.accept()
            connections.append(Connection(conn, addr))
            print("connected")
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
        elif HAND == "left": # If hand is left
            LHands.append(ID[i]) # Append its ID to the list of left hands

    decrement = 20000000000 # Initializing round timer
    lives = 3 # Initializing game lives
    Gameover = False # Initializing game status flag
    RSinceSwaroo = 0

    while True: # While we are a hub
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
        if len(PairH1) == 2:                                ##
           for i in range(len(ID)):                         ##
                if PairH1[0] == ID[i]:                      ##
                    connections[i].send(str(PairH1[1]))     ##
                    connections[i].send(ClrP1)              ##               
                    connections[i].send(decrement)          ##
                    connections[i].send(ClrP1)              ##
                if PairH1[1] == ID[i]:                      ##
                    connections[i].send(str(PairH1[0]))     ##
                    connections[i].send(ClrP1)              ##
                    connections[i].send(decrement)          ##
                    if switcharooR == 1:                    ##
                        connections[i].send(ClrP2)          ##
                    else:                                   ##
                        connections[i].send(ClrP1)          ##
        elif len(PairH1) == 1:                              ##
            for i in range(len(ID)):                        ##
                if PairH1[0] == ID[i]:                      ##
                    connections[i].send(0)                  ##
                    connections[i].send(0)                  ##               
                    connections[i].send(0)                  ##
                    connections[i].send(0)                  ##
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

        for i in range(len(connections)): # Check if all units conducted a successful handshake:
            response = connections[i].receive(100) # Retrieve one response
            print("Response" + str(i) + ": " + response)
            if response == "False": # If response was false:
                flag = False

        if flag == False: # If any of the handshakes were unsuccessful
            lives = lives - 1 # Subtract one life
            for i in range(len(connections)): # Send "loselife" to all units
                connections[i].send("loselife")
            if lives == 0:
                for i in range(len(connections)): # Send "gameover" to all units
                    connections[i].send("gameover")
                    print("Sent " + str(i))
                Gameover = True
                
        elif flag == True: # If none of the handshakes were unsuccessful
            for i in range(len(connections)): # Send "continue" to all units
                connections[i].send("continue")
            
        if Gameover == True: # If game is over:
            break # Break game loop
        
        elif Gameover == False: # If game is not over:
            for i in range(len(connections)): # Send "continue" to all units
                connections[i].send("continue")
                
        if (decrement >= 4000000000) and (flag == True): # Reduce round timer if round was successful and roundtimer is larger than 7s        
            decrement = decrement - 1000000000 # Reduce round timer
        if (RSinceSwaroo < 9): # Edge case for random function
            RSinceSwaroo = RSinceSwaroo + 1 # Increment rounds since switcharoo counter

    # close the connection, happens when game loop is broken
    print("out")
    for i in range(len(connections)):
        connections[i].close()
Main()
