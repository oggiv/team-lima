# wireless_laptop.py
# functions for communicating with the picos from laptops via sockets
# you must configure / connect to the wifi manually from your laptop

import socket
import time

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
    
class Hub:
    
    # interfaces functionality for hosting a wifi as a hub and accepting socket connections from clients
    
    def __init__(self):
        self.gateway = ''
        self.ip = ''

        # socket configuration
        self._socket = socket.socket()
        self._socket.bind(('0.0.0.0', 42)) # (address, port)
        self._socket.listen(5000)
        self._socket.settimeout(12.0)
    
    def accept_connection(self):
        # listens for, createsa and returns a socket connection
        # return -> Connection, address
        #
        # note to self: port is hard coded
        #               timeout is not specified
        client_socket, address = self._socket.accept()
        return Connection(client_socket, address)

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

