# neo_hub.py
# WiFi access point test

import gc
import network
import socket
from machine import Pin

# Garbage collect to clear network interface settings
gc.enable()
gc.collect()

# --- LED ---
# Initialize and turn off LED
led = Pin('LED', Pin.OUT)
led.off()

# --- WiFi ---

print("Initializing WiFi... ", end="")

# WiFi settings
ssid = 'test_rpi'
password = '12345678'

# Start WiFi
accesspoint = network.WLAN(network.AP_IF) # create interface object, ap means access point as in hub or hotspot
accesspoint.config(essid=ssid, password=password)
accesspoint.active(True)

# Wait for network interface to start WiFi
while not accesspoint.active():
    pass

print("Done.")

# --- Socket ---

print("Initializing socket... ", end="")

# Socket settings
port = 420
max_clients = 5 # don't know what this does

# Socket configuration
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # (address family = IPv4, socket type = stream (= tcp))
sock.bind(('', port)) # tuple (self, port)
sock.listen(max_clients)

print("Done.")

while True:
    print("Listening for connection... ", end="")
    # Listen for socket connection
    client_socket, address = sock.accept()
    print("Done.")
    print("Reading message... ", end="")
    message = client_socket.recv(256)
    print("Done.")
    client_socket.close()
    
    # Check message and potentially turn on LED
    print("The received message was: " + message)
    if message == "test":
        print("Turning on LED... ", end="")
        led.on()
        print("Done.")
