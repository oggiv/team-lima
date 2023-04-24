# neo_client.py
# WiFi connection and socket test

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

# Connect to WiFi
wlan = network.WLAN(network.STA_IF) # Start interface as client on network
wlan.active(True)
wlan.connect(ssid, password)

# Wait for WiFi to connect
while not wlan.isconnected() or wlan.status() >= 0:
    pass

# Get network information
# The gateway is the hub's ip address
client_ip, subnet, gateway, DNS = wlan.ifconfig()

print("Done.")
print("Client ip is %s and gateway ip is %s" % (client_ip, gateway))

# --- Socket ---

print("Transmitting through socket... ", end="")

# Send message
socket.sendto("test", gateway)

print("Done.")

# Light LED
print("Program done. Turning on led.")
led.on()