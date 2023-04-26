# wireless.py
# functions for communicating over WiFi

import network
import socket

class Connection:
    
    def __init__(self, sock):
        self._socket = sock
    
    def send(message):
        # message = string || integer || float, else -> bruh
        #
        # note to self: use type() to identify type and convert if necessary
        ty = type(message)
        if ty == str or ty == int or ty == float:
            sock.sendall(str(message).encode('UTF-8'))
        else:
            raise TypeError("must be str, int or float, not %s" % ty)
    
    def receive(bytes):
        # bytes = integer, amount of bytes to receive
        # return -> string
        message = client_socket.recv(bytes)
        return message.decode('UTF-8')
    
    def close():
        # closes connection on this end
        _socket.close()

class Hub:
    
    def __init__(self):
        # configure interface as wifi access point
        self._accesspoint = network.WLAN(network.AP_IF)

        # Socket configuration
        sock = socket.socket()
        sock.bind(('0.0.0.0', 42)) # (address, port)
        sock.listen(5000)
        sock.settimeout(12.0)
        
        self._socket = sock
    
    def start_wifi(ssid, password):
        # ssid = string, name of network
        # password = string, password to network
        # return -> my_ip, gateway_ip
        #
        # note to self: hiding the ssid
        
        # create interface object, ap means access point as in hub or hotspot
        _accesspoint.config(essid=ssid, password=password, hidden=True)
        _accesspoint.active(True)
        while not _accesspoint.active():
            pass
        
        client_ip, subnet, gateway_ip, DNS = wlan.ifconfig()
        return client_ip, gateway_ip
        
    def stop_wifi():
        # shut down WiFi access point
        _accesspoint.active(False)
        while _accesspoint.active():
            pass
    
    def wifi_is_active():
        # returns a boolean of the wifi status
        return _accesspoint.active()
    
    def scan(ssid):
        # scans for a hub network
        # return -> True, if network exists
        #        -> False, if there's no network
        network_list = _accesspoint.scan()
        for net in network_list:
            if net[0] == ssid:
                return True
        return False
    
    def accept_connection():
        # return -> Connection, address
        #
        # note to self: hard code port for now
        client_socket, address = _socket.accept()
        client_conn = Connection(client_socket), address
        return client_conn
    
class Client:
    
    def __init__():
        # configure interface as client on network
        self._wlan = network.WLAN(network.STA_IF)
        self._socket = socket.socket()
        self._gateway = ''
    
    def connect_to_wifi(ssid, password):
        # ssid = string, name of network
        # password = string, password to network
        # return -> client_ip, gateway_ip
        #
        # note to self: remember gateway_ip for connecting to hub later
        _wlan.active(True)
        _wlan.connect(ssid, password)
        while not _wlan.isconnected() and _wlan.status() >= 0:
            pass

        # Get network information
        # The gateway is the hub's ip address
        client_ip, subnet, self._gateway, DNS = wlan.ifconfig()
        return client_ip, self._gateway
        
    def connected_to_wifi():
        return _wlan.is_connected()
    
    def scan(ssid):
        # scans for a hub network
        # return -> True, if network exists
        #        -> False, if there's no network
        network_list = _wlan.scan()
        for net in network_list:
            if net[0] == ssid:
                return True
        return False
    
    def connect_to_hub():
        # return -> Connection, socket interface to hub
        self._socket = socket.socket()
        _socket.connect((_gateway, 42))
