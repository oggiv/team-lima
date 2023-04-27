# neo_client.py
# Python3 socket test
# Run from laptop which is connected to pico hub's network

import socket

# --- Socket ---
print("Transmitting through socket... ", end="")

# Socket settings
port = 420

# Initialize socket
sock = socket.socket()
sock.settimeout(20.0)

# Send message
#try:
#sock.sendto(b'test', ('192.168.4.1', port))
sock.connect(('192.168.4.1', port))
sock.send(b'1')
message = client_socket.recv(16)
print(message)
sock.send(b'3')
sock.close()
#except OSError as err:
#    if err.errno == 107: # ENOTCONN error -> socket not connected
#        print("Failed.")
#        print("Socket connection could not be established. Are you connected to a WLAN?")

print("Done.")
