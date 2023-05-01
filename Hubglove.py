# hub_example.py
# how to use the wireless library to run a hub
import wireless
import random
import time

Colours = ["green", "blue", "yellow", "purple", "cyan", "orange", "pink"]

def randomize_list(original_list):
    # Create a new list with the same elements as the original list
    randomized_list = original_list[:]

    # Shuffle the elements of the new list using the Fisher-Yates shuffle algorithm
    for i in range(len(randomized_list) - 1, 0, -1):
        j = random.randint(0, i)
        randomized_list[i], randomized_list[j] = randomized_list[j], randomized_list[i]

    # Return the new list with randomized values
    return randomized_list

# create a hub object
hub = wireless.Hub()

# start wifi that clients can connect to
# start_wifi(network name, password)
hub.start_wifi('rpi_test', '12345678')

# check if wifi is running like it should
print(hub.wifi_is_active())

# accept socket connections from clients 
connections = []

try:
    while True: 
        connections.append(hub.accept_connection())
except OSError: # specify error and add response?
    print("no more clients")
    pass

# ID array and handtype array
ID = []
RHands = []
LHands = []

for i in range(len(connections)):
    ID.append(int(connections[i].receive(256)))
    HAND = connections[i].receive(100)
    if HAND == "right":
        RHands.append(ID[i])
    elif HAND1 == "left":
        LHands.append(ID[i])
    
print(ID)
print(RHands)

decrement = 20000000000

while hub.wifi_is_active():

    PairH1 = []
    PairH2 = []
    PairV1 = []
    PairV2 = []

    if len(RHands) > 0:
        randompairs = randomize_list(RHands)
        if len(randompairs) >= 2:
            PairH1.append(randompairs.pop(0))
            PairH1.append(randompairs.pop(0))
        if len(randompairs) >= 2:
            PairH2.append(randompairs.pop(0))
            PairH2.append(randompairs.pop(0))

    if len(LHands) > 0:
        randompairs = randomize_list(LHands)
        if len(randompairs) >= 2:
            PairV1.append(randompairs.pop(0))
            PairV1.append(randompairs.pop(0))
        if len(randompairs) >= 2:
            PairV2.append(randompairs.pop(0))
            PairV2.append(randompairs.pop(0))

    randomColour = randomize_list(Colours)
    ClrP1 = randomColour.pop(0)
    ClrP2 = randomColour.pop(0)
    ClrP3 = randomColour.pop(0)
    ClrP4 = randomColour.pop(0)

    if len(PairH1) > 0:
        for i in range(len(ID)):
            if PairH1[0] == ID[i]:
                connections[i].send(str(PairH1[1]))
                connections[i].send(ClrP1)
                connections[i].send(1)
                connections[i].send(decrement)
        for i in range(len(ID)):
            if PairH1[1] == ID[i]:
                connections[i].send(str(PairH1[0]))
                connections[i].send(ClrP1)
                connections[i].send(0)
                connections[i].send(decrement)
                
    if len(PairH2) > 0:
        for i in range(len(ID)):
            if PairH2[0] == ID[i]:
                connections[i].send(str(PairH2[1]))
                connections[i].send(ClrP2)
                connections[i].send(1)
                connections[i].send(decrement)
        for i in range(len(ID)):
            if PairH2[1] == ID[i]:
                connections[i].send(str(PairH2[0]))
                connections[i].send(ClrP2)
                connections[i].send(0)
                connections[i].send(decrement)
                
    if len(PairV1) > 0:
        for i in range(len(ID)):
            if PairV1[0] == ID[i]:
                connections[i].send(str(PairV1[1]))
                connections[i].send(ClrP3)
                connections[i].send(1)
                connections[i].send(decrement)
        for i in range(len(ID)):
            if PairV1[1] == ID[i]:
                connections[i].send(str(PairV1[0]))
                connections[i].send(ClrP3)
                connections[i].send(0)
                connections[i].send(decrement)

    if len(PairV2) > 0:
        for i in range(len(ID)):
            if PairV2[0] == ID[i]:
                connections[i].send(str(PairV2[1]))
                connections[i].send(ClrP4)
                connections[i].send(1)
                connections[i].send(decrement)
        for i in range(len(ID)):
            if PairV2[1] == ID[i]:
                connections[i].send(str(PairV2[0]))
                connections[i].send(ClrP4)
                connections[i].send(0)
                connections[i].send(decrement)

    flag = True
    decrement = decrement - 1000000000

    for i in range(len(connections)):
        response = connections[i].receive(100)
        if response == "False":
            flag = False

    if flag == False:
        for i in range(len(connections)):
            connections[i].send("gameover")
    if flag == True:
        for i in range(len(connections)):
            connections[i].send("gameon")

# close the connection
connections[0].close()
connections[1].close()