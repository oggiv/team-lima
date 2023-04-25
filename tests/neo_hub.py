# neo_hub.py
# WiFi access point test

import gc
import network
import usocket as socket
from machine import Pin, reset

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

client_ip, subnet, gateway, DNS = accesspoint.ifconfig()

print("Done.")
print("Client ip is %s and gateway ip is %s" % (client_ip, gateway))

# --- Socket ---
print("Initializing socket... ", end="")

# Socket settings
port = 420
max_clients = 5000 # don't know what this does

# Socket configuration
sock = socket.socket() # (address family = IPv4, socket type = stream (= tcp))
sock.bind(('0.0.0.0', port)) # tuple (address, port)
sock.listen(max_clients)

print("Done.")

while True:
    
    gc.collect()

    print("Listening for connection... ", end="")
    # Listen for socket connection
    client_socket, address = sock.accept()
    print("Done.")
    
    print("Reading message... ", end="")
    message = client_socket.recv(4)
    print("Done.")

    client_socket.close()

    print("The received message was: %s" % message)
    
    # Check message and potentially turn on LED
    print("")
    if message == b"test":
        print("Turning on LED... ", end="")
        led.on()
        print("Done.")
