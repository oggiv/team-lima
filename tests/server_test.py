import network
import time
import socket
from machine import Pin

led = Pin("LED", Pin.OUT)
led.off()
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('RPI_PICO_AP', '12345678')
# wait for connection
while not wlan.isconnected() : 
    print("Waiting to connect")

wlan.status() # 3 is success
wlan.ifconfig()
print(wlan.ifconfig())

while True:
    ai = socket.getaddrinfo("192.168.4.1", 80) # web server addr
    addr = ai[0][-1]
    
    # create socket, wait for instructions to light led
    s = socket.socket()
    s.connect(addr)
    ss = int(s.recv(1))
    print(ss)
    
    led.on()
    
    s.close()
    time.sleep(0.2)