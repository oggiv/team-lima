# SERVER

# start
import socket
import network
import gc
# from wifi_config import ssid, password, port

# garbage collector
gc.collect()

ssid = 'test_rpi'
password = '12345678'
port = 80
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

# starta socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # (address family = IPv4, socket type = stream -> tcp)
sock.bind(('', port)) # tuple (self, port)
sock.listen(max_clients) # allow to accept max_clients amount of clients

print('Waiting for connections...')
# vänta på connection från klient
while True :
    conn, addr = sock.accept()
    print('Connection accepted from %s' % str(addr))
    
    # skicka meddelande
    conn.send(str(5)) # sending the nr 5
    conn.close()
