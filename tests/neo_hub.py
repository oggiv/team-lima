# neo_hub.py
# WiFi access point test

import gc
import network
import socket

# Garbage collect to clear network interface settings
gc.enable()
gc.collect()

# WiFi configuration
ssid = 'test_rpi'
password = '12345678'

# Start WiFi
ap = network.WLAN(network.AP_IF) # create interface object, ap means access point as in hub or hotspot
ap.config(essid=ssid, password=password)
ap.active(True)

# Listen for socket connections
#  - Check for greeting
# Send number