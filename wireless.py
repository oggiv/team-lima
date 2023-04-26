# wireless.py
# functions for communicating over WiFi

import network
import socket

class Connection:
    
    def __init__(self, sock):
        self._socket = sock
    
    def send(self, message):
        # message = string || integer || float, else -> bruh
        #
        # note to self: use type() to identify type and convert if necessary
        ty = type(message)
        if ty == str or ty == int or ty == float:
            self._socket.sendall(str(message).encode('UTF-8'))
        else:
            raise TypeError("must be str, int or float, not %s" % ty)
    
    def receive(self, bytes):
        # bytes = integer, amount of bytes to receive
        # return -> string
        message = self._socket.recv(bytes)
        return message.decode('UTF-8')
    
    def close(self):
        # closes connection on this end
        self._socket.close()

class Hub:
    
    def __init__(self):
        # configure interface as wifi access point
        self._accesspoint = network.WLAN(network.AP_IF)
        self.ip = ''

        # Socket configuration
        self._socket = socket.socket()
        self._socket.bind(('0.0.0.0', 42)) # (address, port)
        self._socket.listen(5000)
        self._socket.settimeout(12.0)
    
    def start_wifi(self, ssid, password):
        # ssid = string, name of network
        # password = string, password to network
        # return -> my_ip, gateway_ip
        #
        # note to self: hiding the ssid
        
        # create interface object, ap means access point as in hub or hotspot
        self._accesspoint.config(essid=ssid, password=password) # , hidden=True
        self._accesspoint.active(True)
        while not self._accesspoint.active():
            pass
        
        self.ip, subnet, self.gateway, DNS = self._accesspoint.ifconfig()
        return (self.ip, subnet, self.gateway, DNS)
        
    def stop_wifi(self):
        # shut down WiFi access point
        self._accesspoint.active(False)
        while self._accesspoint.active():
            pass
    
    def wifi_is_active(self):
        # returns a boolean of the wifi status
        return self._accesspoint.active()
    
    def scan(self, ssid):
        # scans for a hub network
        # return -> True, if network exists
        #        -> False, if there's no network
        network_list = self._accesspoint.scan()
        for net in network_list:
            if net[0] == ssid:
                return True
        return False
    
    def accept_connection(self):
        # return -> Connection, address
        #
        # note to self: hard code port for now
        client_socket, address = self._socket.accept()
        return Connection(client_socket), address
    
class Client:
    
    def __init__(self):
        # configure interface as client on network
        self._wlan = network.WLAN(network.STA_IF)
        self._socket = socket.socket()
        self.gateway = ''
        self.ip = ''
    
    def connect_to_wifi(self, ssid, password):
        # ssid = string, name of network
        # password = string, password to network
        # return -> client_ip, gateway_ip
        #
        # note to self: remember gateway_ip for connecting to hub later
        self._wlan.active(True)
        self._wlan.connect(ssid, password)
        while not self._wlan.isconnected() and self._wlan.status() >= 0:
            pass

        # Get network information
        # The gateway is the hub's ip address
        self.ip, subnet, self.gateway, DNS = wlan.ifconfig()
        return (self.ip, subnet, self.gateway, DNS)
        
    def connected_to_wifi(self):
        return self._wlan.is_connected()
    
    def scan(self, ssid):
        # scans for a hub network
        # return -> True, if network exists
        #        -> False, if there's no network
        network_list = self._wlan.scan()
        for net in network_list:
            if net[0] == ssid:
                return True
        return False
    
    def connect_to_hub(self):
        # return -> Connection, socket interface to hub
        self._socket = socket.socket()
        self._socket.connect((self.gateway, 42))