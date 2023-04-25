# neo_client.py
# WiFi connection and socket test

import gc
import network
import socket
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

# Connect to WiFi
wlan = network.WLAN(network.STA_IF) # Start interface as client on network
wlan.active(True)
wlan.connect(ssid, password)

# Wait for WiFi to connect
while not wlan.isconnected() and wlan.status() >= 0:
    pass

# Get network information
# The gateway is the hub's ip address
client_ip, subnet, gateway, DNS = wlan.ifconfig()

print("Done.")
print("Client ip is %s and gateway ip is %s" % (client_ip, gateway))

# --- Socket ---
print("Transmitting through socket... ", end="")

# Socket settings
port = 420

# Initialize socket
sock = socket.socket() #socket.AF_INET, socket.SOCK_STREAM
sock.settimeout(20.0)

# Send message
#try:
#sock.sendto("test".encode(), (gateway, port))
sock.connect(('192.168.4.1', port))
sock.send(b'test')
sock.close()
#except OSError as err:
#    if err.errno == 107: # ENOTCONN error -> socket not connected
#        print("Failed.")
#        print("Socket connection could not be established. Are you connected to a WLAN?")

print("Done.")

# Light LED
print("Program done. Turning on led.")
led.on()

reset()