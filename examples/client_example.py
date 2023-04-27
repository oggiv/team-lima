# client_example.py
# how to use the wireless library to run a client

import wireless

# create client object
client = wireless.Client()

# connect to wifi network
# connect_to_wifi(network name, password)
client.connect_to_wifi('rpi_test', '12345678')

# check if wifi is connected
print(client.connected_to_wifi())

# create a socket connection to the hub
conn = client.get_connection()

# receive a 5 byte (5 character) long message from the hub
message = conn.receive(2048)
print(message)

# send message to the hub through the connection
conn.send('why did you tell me: %s' % message)

# close the connection
conn.close()