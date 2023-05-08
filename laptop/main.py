import wireless
#from Hubglove import Hub
from Clientglove import Client
from LED import lights

def connect(): # Connect to 'LAPTOP-4036F672'
    try:
        Client('LAPTOP-4036F672')
    except OSError: # Catch no connection found
        lights("yellow") # Display yellow colour
        pass
    
while True:
    connect()