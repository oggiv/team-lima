# pico_max_test.py
# connects a pico to the hub_max_test

import random
import socket

class Connection:
    
    # interfaces the socket connection
    
    def __init__(self, sock, address):
        self._socket = sock
        self.address = address
    
    def send(self, message):
        # sends message (which must be a str, int or float) over socket
        # message = string || integer || float, else -> TypeError
        # return -> None
        ty = type(message)
        if ty == str or ty == int or ty == float:
            encoded_message = str(message).encode('UTF-8') + b'\r'
            self._socket.sendall(encoded_message)
        else:
            raise TypeError("must be str, int or float, not %s" % ty)
    
    def receive(self, byte_count):
        # reads [bytes] amount of bytes from socket
        # bytes = integer, amount of bytes to receive
        # return -> string
        
        if byte_count == 0:
            byte_count = 2000
        
        data = b''
        bytes_read = 0
        
        while bytes_read < byte_count:
            byte = self._socket.recv(1)
            if byte == b'\r':
                break
            else:
                data += byte
                bytes_read += 1
        
        return data.decode('UTF-8')
    
    def close(self):
        # closes the socket connection
        # return -> None 
        self._socket.close()

class Client:
    
    # interfaces functionality for connecting to a wifi as a client and opening socket connections to the hub
    
    def __init__(self):
        self._socket = socket.socket()
        self.gateway = '192.168.4.1'
        self.ip = ''
    
    def get_connection(self):
        # establishes and returns socket connection to hub
        # return -> Connection, socket interface to hub
        sock = socket.socket()
        sock.connect((self.gateway, 42))
        return Connection(sock, self.gateway)

# create client object
client = Client()

print(True)

# create a socket connection to the hub
conn = client.get_connection()

# receive a 5 byte (5 character) long message from the hub
try:
    while True:
        print(conn.receive(2048))
        conn.send('check ' + str(random.randint(0, 256)))
except OSError as err:
    conn.close
