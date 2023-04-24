# server battery

# start
import socket
import network
import gc
import time
# from wifi_config import ssid, password, port

# garbage collector
gc.collect()
gc.enable()

time.sleep(1)

ssid = 'test_rpi'
password = '12345678'
port = 82
max_clients = 10 # maybe nr of unaccepted client?

# starta wifi
ap = network.WLAN(network.AP_IF) # create interface obj, ap = access point
ap.config(essid=ssid, password=password) # , password=password   , security=network.WLAN.AUTH_OPEN
ap.active(True)

while ap.active() == False :
    pass

print('Interface activated.')
print(ap.ifconfig())
print('')

gc.collect()

# starta socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # (address family = IPv4, socket type = stream -> tcp)
sock.bind(('192.168.4.1', port)) # tuple (self, port)
sock.listen(max_clients) # allow to accept max_clients amount of clients

print('Waiting for connections...')
# vänta på connection från klient
while True :
    conn, addr = sock.accept()
    print('Connection accepted from %s' % str(addr))
    
    # skicka meddelande
    conn.send(str(5)) # sending the nr 5
    
    while True:
        resp = int(conn.recv(1024))
        print('Seconds passed since connection: ' + resp)
        if resp == 900:
            break
    conn.close()