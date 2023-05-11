import wireless
#from Hubglove import Hub
from Clientglove import Client
from LED import lights

def connect(): # Connect to 'LAPTOP-4036F672' or given laptop name
    try:
        Client('LAPTOP-3QTGBLP9')
    except OSError: # Catch no connection found
        lights("yellow") # Display yellow colour
        pass
    
while True:
    connect()