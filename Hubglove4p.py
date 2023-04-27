# hub_example.py
# how to use the wireless library to run a hub
import wireless
import random

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

# accept a socket connection from a client and make a connection object for it
conn1 = hub.accept_connection()
conn2 = hub.accept_connection()
conn3 = hub.accept_connection()
conn4 = hub.accept_connection()

# receive ID + Handtype
ID1 = int(conn1.receive(256))
print(ID1)
HAND1 = conn1.receive(100)
print(HAND1)
ID2 = int(conn2.receive(256))
print(ID2)
HAND2 = conn2.receive(100)
print(HAND2)
ID3 = int(conn3.receive(256))
print(ID3)
HAND3 = conn3.receive(100)
print(HAND3)
ID4 = int(conn4.receive(256))
print(ID4)
HAND4 = conn4.receive(100)
print(HAND4)

if HAND1 == "right":
    RHands.append(ID1)
elif HAND1 == "left":
    LHands.append(ID1)
if HAND2 == "right":
    RHands.append(ID2)
elif HAND2 == "left":
    LHands.append(ID2)
if HAND3 == "right":
    RHands.append(ID3)
elif HAND3 == "left":
    LHands.append(ID3)
if HAND4 == "right":
    RHands.append(ID4)
elif HAND4 == "left":
    LHands.append(ID4)

while hub.wifi_is_active(): #Run game
    Pair1 = []
    Pair2 = []
    
    if len(RHands) > 0:
        randompairs = randomize_list(RHands)
        Pair1.append(randompairs.pop(0))
        Pair1.append(randompairs.pop(0))
        Pair2.append(randompairs.pop(0))
        Pair2.append(randompairs.pop(0))
        
    if len(LHands) > 0:
        randompairs = randomize_list(LHands)
        Pair1.append(randompairs.pop(0))
        Pair1.append(randompairs.pop(0))
        Pair2.append(randompairs.pop(0))
        Pair2.append(randompairs.pop(0))

    randomColour = randomize_list(Colours)
    ClrP1 = randomColour.pop(0)
    ClrP2 = randomColour.pop(0)
    
    if Pair1[0] == RHands[0]:
        conn1.send(str(Pair1[1]))
        conn1.send(ClrP1)
        conn1.send(0)
    elif Pair1[0] == RHands[1]:
        conn2.send(str(Pair1[1]))
        conn2.send(ClrP1)
        conn2.send(0)
    elif Pair1[0] == RHands[2]:
        conn3.send(str(Pair1[1]))
        conn3.send(ClrP1)
        conn3.send(0)
    elif Pair1[0] == RHands[3]:
        conn4.send(str(Pair1[1]))
        conn4.send(ClrP1)
        conn4.send(0)
        
    if Pair1[1] == RHands[0]:
        conn1.send(str(Pair1[0]))
        conn1.send(ClrP1)
        conn1.send(1)
    elif Pair1[1] == RHands[1]:
        conn2.send(str(Pair1[0]))
        conn2.send(ClrP1)
        conn2.send(1)
    elif Pair1[1] == RHands[2]:
        conn3.send(str(Pair1[0]))
        conn3.send(ClrP1)
        conn3.send(1)
    elif Pair1[1] == RHands[3]:
        conn4.send(str(Pair1[0]))
        conn4.send(ClrP1)
        conn4.send(1)
        
    if Pair2[0] == RHands[0]:
        conn1.send(str(Pair2[1]))
        conn1.send(ClrP2)
        conn1.send(0)
    elif Pair2[0] == RHands[1]:
        conn2.send(str(Pair2[1]))
        conn2.send(ClrP2)
        conn2.send(0)
    elif Pair2[0] == RHands[2]:
        conn3.send(str(Pair2[1]))
        conn3.send(ClrP2)
        conn3.send(0)
    elif Pair2[0] == RHands[3]:
        conn4.send(str(Pair2[1]))
        conn4.send(ClrP2)
        conn4.send(0)
        
    if Pair2[1] == RHands[0]:
        conn1.send(str(Pair2[0]))
        conn1.send(ClrP2)
        conn1.send(1)
    elif Pair2[1] == RHands[1]:
        conn2.send(str(Pair2[0]))
        conn2.send(ClrP2)
        conn2.send(1)
    elif Pair2[1] == RHands[2]:
        conn3.send(str(Pair2[0]))
        conn3.send(ClrP2)
        conn3.send(1)
    elif Pair2[1] == RHands[3]:
        conn4.send(str(Pair2[0]))
        conn4.send(ClrP2)
        conn4.send(1)
    
    time1 = time.time()
        while(time.time() - time1 < 30):
            try:
                if conn1.receive(256) == "False":
                    conn1.close()
                    conn2.close()
                    conn3.close()
                    conn4.close()
                    
                if conn2.receive(256) == "False":
                    conn1.close()
                    conn2.close()
                    conn3.close()
                    conn4.close()
                    
                if conn3.receive(256) == "False":
                    conn1.close()
                    conn2.close()
                    conn3.close()
                    conn4.close()
                    
                
                if conn4.receive(256) == "False":
                    conn1.close()
                    conn2.close()
                    conn3.close()
                    conn4.close()
                    break
                else:
                    break