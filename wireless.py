# wireless.py
# functions for communicating over WiFi

import network
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
            self._socket.sendall(str(message).encode('UTF-8'))
        else:
            raise TypeError("must be str, int or float, not %s" % ty)
    
    def receive(self, bytes):
        # reads [bytes] amount of bytes from socket
        # bytes = integer, amount of bytes to receive
        # return -> string
        message = self._socket.recv(bytes)
        return message.decode('UTF-8')
    
    def close(self):
        # closes the socket connection
        # return -> None 
        self._socket.close()
    
class Hub:
    
    # interfaces functionality for hosting a wifi as a hub and accepting socket connections from clients
    
    def __init__(self):
        self._accesspoint = network.WLAN(network.AP_IF)
        self.gateway = ''
        self.ip = ''

        # socket configuration
        self._socket = socket.socket()
        self._socket.bind(('0.0.0.0', 42)) # (address, port)
        self._socket.listen(5000)
        self._socket.settimeout(12.0)
    
    def start_wifi(self, ssid, password):
        # configures and starts wifi access point
        # ssid = string, name of network
        # password = string, password to network
        # return -> (client_ip, subnet_mask, hub_ip, dns_ip)
        #
        # note to self: ssid isn't hidden
        
        # create interface object, ap means access point as in hub or hotspot
        self._accesspoint.config(essid=ssid, password=password)
        self._accesspoint.active(True)
        while not self._accesspoint.active():
            pass
        
        self.ip, subnet, self.gateway, DNS = self._accesspoint.ifconfig()
        return (self.ip, subnet, self.gateway, DNS)
        
    def stop_wifi(self):
        # shuts down wifi access point
        # return -> None
        self._accesspoint.active(False)
        while self._accesspoint.active():
            pass
    
    def wifi_is_active(self):
        # checks the wifi access point status
        # return -> True, if a wifi is currently being hosted on the access point
        #           False, if no wifi is currently being hosted on the access point
        return self._accesspoint.active()
    
    def scan(self, ssid):
        ### WARNING: does not work
        # scans for a wifi network with the given ssid
        # return -> True, if network exists
        #        -> False, if there's no network
        network_list = self._accesspoint.scan()
        for net in network_list:
            if net[0] == ssid:
                return True
        return False
    
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
        self._wlan = network.WLAN(network.STA_IF)
        self._socket = socket.socket()
        self.gateway = ''
        self.ip = ''
    
    def connect_to_wifi(self, ssid, password):
        # ssid = string, name of network
        # password = string, password to network
        # return -> (client_ip, subnet_mask, hub_ip, dns_ip)
        #
        # note to self: remember gateway_ip for connecting to hub later
        self._wlan.active(True)
        self._wlan.connect(ssid, password)
        while not self._wlan.isconnected() and self._wlan.status() >= 0:
            pass

        # Get network information. The gateway is the hub's ip address.
        self.ip, subnet, self.gateway, DNS = self._wlan.ifconfig()
        if self.ip == '0.0.0.0':
            raise OSError("Could not connect to WiFi. Is the ssid correct?")
        else:
            return (self.ip, subnet, self.gateway, DNS)
        
    def connected_to_wifi(self):
        # checks if the client is currently connected to a wifi or not
        # return -> True, if connected to a network
        #           False, if not connected to a network
        return self._wlan.isconnected()
    
    def scan(self, ssid):
        ### WARNING: does not work
        # scans for a hub network
        # return -> True, if network exists
        #        -> False, if there's no network
        network_list = self._wlan.scan()
        for net in network_list:
            if net[0] == ssid:
                return True
        return False
    
    def get_connection(self):
        # establishes and returns socket connection to hub
        # return -> Connection, socket interface to hub
        sock = socket.socket()
        sock.connect((self.gateway, 42))
        return Connection(sock, self.gateway)
