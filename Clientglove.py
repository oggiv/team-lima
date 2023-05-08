import wireless
from Alive import playerStatus, outOfRound
from PhyComProtocol import ID, Handtype
import time
from LED import lights

def Client(ssid):
    # create client object
    client = wireless.Client()

    # connect to wifi network
    # connect_to_wifi(network name, password)
    client.connect_to_wifi(ssid, '12345678')

    # check if wifi is connected
    print(client.connected_to_wifi())
    lights("connected")

    # create a socket connection to the hub
    conn = client.get_connection()

    conn.send(str(ID())) # Send THIS units ID
    conn.send(Handtype()) # Send THIS units Handtype

    def Gamecycle(): #Runs one cycle of the game
        partnerID = int(conn.receive(100)) # Receive partners ID
        colour = conn.receive(100) # Receive given pair colour
        time_playerout = int(conn.receive(100000000000)) # Recieve round timer (in NS)
        SWcolour = conn.receive(100) # Receive eventual switcharoo colour
        if(partnerID == 0 and colour == "0" and SWcolour == "0"):
            returner = outOfRound(time_playerout)
            if returner: # If correct hand was shook:
                conn.send("True") # Send "True" to hub
            elif not returner: # If incorrect hand was shook:
                conn.send("False") # Send "False" to hub
        else:
            successfulHandshake = playerStatus(partnerID, colour, time_playerout, SWcolour) # Check if correct hand was shook whithin time
            if successfulHandshake: # If correct hand was shook:
                conn.send("True") # Send "True" to hub
            elif not successfulHandshake: # If incorrect hand was shook:
                conn.send("False") # Send "False" to hub

    gameStatus = "gameon" # Initialize game status flag
    while gameStatus != "gameover": # While game is not over
        Gamecycle() # Run gamecycle
        lifeStatus = conn.receive(100)
        if lifeStatus == "loselife":
            lights("lostlife")
        gameStatus = conn.receive(100) # Check if game is over

    lights("gameover") # Game is over, Run gameover lightshow
    conn.close() # close the connection
