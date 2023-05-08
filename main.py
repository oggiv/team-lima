import wireless
from Hubglove import Hub
from Clientglove import Client

def connect(): # Connect to 'LAPTOP-4036F672'
    try:
        Client('LAPTOP-4036F672')
    except OSError:
        try:
            Hub('LAPTOP-4036F672')
        except OSError:
            pass

while True:
    connect()