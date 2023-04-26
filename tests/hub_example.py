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
conn1 = hub.accept_connection()
conn2 = hub.accept_connection()

# send message to client through the connection
conn1.send('you are connection 1')
conn2.send('you are connection 1')
print("conn1: %s" % conn1.receive(1024))
print("conn2: %s" % conn2.receive(1024))

# close the connection
conn.close()