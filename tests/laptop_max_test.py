# pico_max_test.py
# connects a pico to the hub_max_test

import wireless_laptop
import random

# create client object
client = wireless_laptop.Client()

print(True)

# create a socket connection to the hub
conn = client.get_connection()

# receive a 5 byte (5 character) long message from the hub
try:
    while True:
        print(conn.receive(2048))
        conn.send('check ' + str(random.randint(0, 256)))
except OSError as err:
    conn.close

