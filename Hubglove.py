# hub_example.py
# how to use the wireless library to run a hub
import wireless
import random

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
ID1 = int(conn1.receive(3))
HAND1 = conn1.recieve(100)
ID2 = int(conn2.receive(3))
HAND2 = conn2.recieve(100)

colourID = random.randint(1,5)
    if colourID == 1:
        colour == "green"
    elif colourID == 2:
        colour == "blue"
    elif colourID == 3:
        colour == "yellow"
    elif colourID == 4:
        colour == "purple"
    elif colourID == 5:
        colour == "cyan"
        
conn1.send(str(ID2))
conn1.send(colour)
conn2.send(str(ID1))
conn2.send(colour)

# close the connection
conn1.close()
conn2.close()
