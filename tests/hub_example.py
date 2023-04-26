# hub_example.py
# how to use the wireless library to run a hub

import wireless

# create a hub object
hub = wireless.Hub()

# start wifi that clients can connect to
# start_wifi(network name, password)
hub.start_wifi('rpi_test', '12345678')

# check if wifi is running like it should
print(hub.wifi_is_active())

# accept a socket connection from a client and make a connection object for it
conn = hub.accept_connection()

# send message to client through the connection
conn.send('hello')

# receive a 4 byte (4 character) long message from the client
print(conn.receive(4))

# close the connection
conn.close()