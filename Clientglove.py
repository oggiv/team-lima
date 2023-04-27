# client_example.py
# how to use the wireless library to run a client
import wireless
from Alive import playerStatus
from PhyComProtocol import ID

# create client object
client = wireless.Client()

# connect to wifi network
# connect_to_wifi(network name, password)
client.connect_to_wifi('rpi_test', '12345678')

# check if wifi is connected
print(client.connected_to_wifi())

# create a socket connection to the hub
conn = client.get_connection()
conn.send(str(ID()))
conn.send(Handtype())

def Gamecycle(): #Runs one cycle of the game
    partnerID = int(conn.recieve(3))
    colour = conn.recieve(100) 
    recieverflag = conn.recieve(100) 

    successfulHandshake = playerStatus(partnerID, colour, recieverflag)
    if successfulHandshake:
        conn.send("True")
    elif not successfulHandshake:
        conn.send("False")
        
Gamecycle()
    

# close the connection
conn.close()