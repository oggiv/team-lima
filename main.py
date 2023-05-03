import wireless
from Hubglove import Hub
from Clientglove import Client

try:
    Client('rpi_test')
except OSError:
    Hub('rpi_test')