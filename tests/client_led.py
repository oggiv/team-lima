# client

import network
import socket
from machine import Pin
from wifi_config import ssid, password, port, server_address

# turn of LED
led = Pin('LED', Pin.OUT)
led.off()

# connect to wifi
wlan = network.WLAN(network.STA_IF) # start interface as client on network
wlan.active(True)
wlan.connect(ssid, password)

print('Connecting to WiFi...', end=' ')
while not wlan.isconnected() and wlan.status() >= 0:
    pass

print('Done.')
print(wlan.ifconfig())
print('')

# open socket
addr_interface = socket.getaddrinfo(server_address, port) # special address object for the socket. Is a 2D array
addr_info = addr_interface[0][-1]

print('Creating socket...', end=' ')
sock = socket.socket()
sock.connect(addr_info)
print('Done.')

# wait for response
response = int(sock.recv(64)) # read 1 byte from buffer
print('Received message: %s' % response)

# evaluate message / turn on LED
if response == 5:
    print('LED turned on')
    led.on()

# end
sock.close()
    
