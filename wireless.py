# wireless.py
# functions for communicating over WiFi

class Connection:
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
    def start_wifi(ssid, password):
        # ssid = string, name of network
        # password = string, password to network
        # return -> (my_ip, gateway_ip)
        #
        # note to self: enable hiding the network
        pass
    
    def accept_connection():
        # return -> Connection, socket interface to client
        #
        # note to self: hard code port for now
        pass
    
class Client:
    def connect_to_wifi(ssid, password):
        # ssid = string, name of network
        # password = string, password to network
        # return -> (my_ip, gateway_ip)
        #
        # note to self: remember gateway_ip for connecting to hub later
        pass
    
    def connect_to_hub():
        # return -> Connection, socket interface to hub
        pass