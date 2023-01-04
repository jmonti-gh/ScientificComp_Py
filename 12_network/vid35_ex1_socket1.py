''' https://www.youtube.com/watch?v=dWLdI143W-g '''

import socket

# open a socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect ad send a command
mysock.connect(('data.pr4e.org', 80))
#cmd = 'GET /romeo.txt HTTP/1.1\r\nHost:data.pr4e.org\r\n\r\n'.encode()
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
# mysock.send(b"GET /romeo.txt HTTP/1.1\r\nHost:data.pr4e.org\r\n\r\n")

# Retrieve the data from server
while True:
    data = mysock.recv(512)
    if len(data) < 1: break
    print(data.decode())
mysock.close()