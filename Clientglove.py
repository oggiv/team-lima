# client_example.py
# how to use the wireless library to run a client
import wireless
from Alive import playerStatus
from PhyComProtocol import ID, Handtype
import time
from LED import lights

# create client object
client = wireless.Client()

# connect to wifi network
# connect_to_wifi(network name, password)
client.connect_to_wifi('rpi_test', '12345678')

# check if wifi is connected
print(client.connected_to_wifi())
lights("connected")

# create a socket connection to the hub
conn = client.get_connection()

conn.send(str(ID()))
conn.send(Handtype())

def Gamecycle(): #Runs one cycle of the game
    partnerID = int(conn.receive(100))
    print(partnerID)
    colour = conn.receive(100)
    print(colour)
    recieverflag = int(conn.receive(100))
    print(recieverflag)
    time_playerout = int(conn.receive(100000000000))

    successfulHandshake = playerStatus(partnerID, colour, recieverflag, time_playerout)
    if successfulHandshake:
        conn.send("True")
    elif not successfulHandshake:
        conn.send("False")

gameStatus = "gameon"
while gameStatus != "gameover":
    Gamecycle()
    gameStatus = conn.receive(100)

lights("gameover")
# close the connection
conn.close()