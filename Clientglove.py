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

conn.send(str(ID())) # Send THIS units ID
conn.send(Handtype()) # Send THIS units Handtype

def Gamecycle(): #Runs one cycle of the game
    partnerID = int(conn.receive(100)) # Receive partners ID
    print(partnerID)
    colour = conn.receive(100) # Receive given pair colour
    print(colour)
    receiverflag = int(conn.receive(100)) # Receive flag whether THIS unit is a sender/receiver
    print(receiverflag)
    time_playerout = int(conn.receive(100000000000)) # Recieve round timer (in NS)

    successfulHandshake = playerStatus(partnerID, colour, receiverflag, time_playerout) # Check if correct hand was shook whithin time
    if successfulHandshake: # If correct hand was shook:
        conn.send("True") # Send "True" to hub
    elif not successfulHandshake: # If incorrect hand was shook:
        conn.send("False") # Send "False" to hub

gameStatus = "gameon" # Initialize game status flag
while gameStatus != "gameover": # While game is not over
    Gamecycle() # Run gamecycle
    gameStatus = conn.receive(100) # Check if game is over

lights("gameover") # Game is over, Run gameover lightshow
conn.close() # close the connection