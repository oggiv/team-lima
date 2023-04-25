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
        pass
    
    def receive(bytes):
        # bytes = integer, amount of bytes to receive
        # return -> string
        pass
    
    def close():
        # closes connection on this end
        pass

class Hub:
    
    def __init__(self):
        self._accesspoint = network.WLAN(network.AP_IF)
    
    def start_wifi(ssid, password):
        # ssid = string, name of network
        # password = string, password to network
        # return -> (my_ip, gateway_ip)
        #
        # note to self: enable hiding the network
        
        # create interface object, ap means access point as in hub or hotspot
        _accesspoint.config(essid=ssid, password=password, hidden=True)
        _accesspoint.active(True)
        while not _accesspoint.active():
            pass
        
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
        pass
    
    def accept_connection():
        # return -> Connection, socket interface to client
        #
        # note to self: hard code port for now
        pass
    
class Client:
    
    def __init__():
        self._wlan = network.WLAN(network.STA_IF)
    
    def connect_to_wifi(ssid, password):
        # ssid = string, name of network
        # password = string, password to network
        # return -> (client_ip, gateway_ip)
        #
        # note to self: remember gateway_ip for connecting to hub later
        
        # Start interface as client on network
        _wlan.active(True)
        _wlan.connect(ssid, password)

        # Wait for WiFi to connect
        while not _wlan.isconnected() and _wlan.status() >= 0:
            pass

        # Get network information
        # The gateway is the hub's ip address
        client_ip, subnet, gateway_ip, DNS = wlan.ifconfig()
        return (client_ip, gateway_ip)
        
    def connected_to_wifi():
        return _wlan.is_connected()
    
    def connect_to_hub():
        # return -> Connection, socket interface to hub
        pass