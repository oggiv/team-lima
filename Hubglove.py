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

# accept a socket connection from a client and make a connection object for it
conn1 = hub.accept_connection()
conn2 = hub.accept_connection()

# receive ID + Handtype
ID1 = int(conn1.receive(256))
print(ID1)
HAND1 = conn1.receive(100)
print(HAND1)
ID2 = int(conn2.receive(256))
print(ID2)
HAND2 = conn2.receive(100)
print(HAND2)

randomColour = randomize_list(Colours)
ClrP1 = randomColour.pop(0)
        
conn1.send(str(ID2))
conn1.send(ClrP1)
conn1.send(1)
conn2.send(str(ID1))
conn2.send(ClrP1)
conn2.send(0)

time.sleep(10)

if conn1.receive(100) == "True":
    print("Successful Handshake Conn1")
if conn2.receive(100) == "True":
    print("Successful Handshake Conn2")

ClrP2 = randomColour.pop(0)
ClrP3 = randomColour.pop(0)

conn1.send(str(169))
conn1.send(ClrP2)
conn1.send(1)
print("ins1 sent")
conn2.send(str(237))
conn2.send(ClrP3)
conn2.send(0)
print("ins2 sent")

time.sleep(10)

if conn1.receive(100) == "False":
    print("Unsuccessful Handshake Conn1")
if conn2.receive(100) == "False":
    print("Unsuccessful Handshake Conn2")

# close the connection
conn1.close()
conn2.close()