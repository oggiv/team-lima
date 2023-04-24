# neo_client.py
# WiFi connection and socket test

# --- WiFi ---
# WiFi settings
ssid = 'test_rpi'
password = '12345678'

# Connect to WiFi
wlan = network.WLAN(network.STA_IF) # Start interface as client on network
wlan.active(True)
wlan.connect(ssid, password)

# Wait for WiFi to connect
while not wlan.isconnected() or wlan.status() >= 0:
    pass

# Get network information
# The gateway is the hub's ip address
client_ip, subnet, gateway, DNS = wlan.ifconfig()

# Send greeting
# Wait for response
#  - Check response
#   - Light LED