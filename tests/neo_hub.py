# neo_hub.py
# WiFi access point test

import gc
import network
import socket

# Garbage collect to clear network interface settings
gc.enable()
gc.collect()

# --- WiFi ---
# WiFi settings
ssid = 'test_rpi'
password = '12345678'

# Start WiFi
ap = network.WLAN(network.AP_IF) # create interface object, ap means access point as in hub or hotspot
ap.config(essid=ssid, password=password)
ap.active(True)

# Wait for network interface to start WiFi
while not ap.active():
    pass

# --- Socket ---
# Socket settings
port = 420
max_clients = 5 # don't know what this does

# Socket configuration
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # (address family = IPv4, socket type = stream (= tcp))
sock.bind(('', port)) # tuple (self, port)
sock.listen(max_clients)

# Listen for socket connections
while True:
    conn, addr = sock.accept()
    

#  - Check for greeting
#   - Send number