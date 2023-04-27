# hub_max_test.py
# tries to connect multiple clients to its wifi and maintain sockets to each of them

import wireless
import time

conn_amount = 2

# create a hub object
hub = wireless.Hub()

# start wifi that clients can connect to
# start_wifi(network name, password)
hub.start_wifi('max_test', '12345678')

# check if wifi is running like it should
print(hub.wifi_is_active())

# accept a socket connection from a client and make a connection object for it
conns = []
while len(conns) < conn_amount:
    try:
        conns.append(hub.accept_connection())
    except OSError as err:
        print("OSError: ", end='')
        print(err)

# send message to client through the connection
for j in range(0, 50):
    i = j % conn_amount
    time.sleep(1)
    conns[i].send('you are connection ' + str(i))
    print(conns[i].receive(64))

# close the connection
for conn in conns:
    conn.close()
    time.sleep(1)
