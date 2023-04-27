# client battery test - send data continuously for 15 min.
# count up each send - if 0 then it stopped.


import network
import socket
import gc
import time
from machine import Pin, Timer

ssid = 'test_rpi'
password = '12345678'
port = 82
server_address = '192.168.4.1'

gc.collect()
gc.enable()

# turn of LED
led = Pin('LED', Pin.OUT)
led.off()

# time count
count = 0

# connect to wifi
wlan = network.WLAN(network.STA_IF) # start interface as client on network
wlan.active(True)
wlan.connect(ssid, password)

print('Connecting to WiFi...', end=' ')
while not wlan.isconnected() and wlan.status() >= 0:
    pass

print('Done.')
led.on()
print(wlan.ifconfig())
print('')

# open socket
addr_interface = socket.getaddrinfo(server_address, port) # special address object for the socket. Is a 2D array
addr_info = addr_interface[0][-1]

gc.collect()

print('Creating socket...', end=' ')
led.off()
sock = socket.socket()
sock.connect(addr_info)
print('Done.')
led.on()

# wait for response
response = int(sock.recv(64)) # read 1 byte from buffer
print('Received message: %s' % response)

# evaluate message / turn on LED
if response == 5:
    print('LED turned on')
    led.on()
    time.sleep(1)
    
for secs in range(180):
    sock.send(bytes(secs))
    led.on()
    time.sleep(5)
    led.off()

# end
sock.close()