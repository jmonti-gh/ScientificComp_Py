''' A puntual Web Browser request '''

# Using - telnet IP port - you can do it:
# $ telnet www.dr-chuck.com 80
# Trying IP...
# Connected to....
# GET http://www.dr-ch....

# ___ data recived.....

trin = 'Pythön'
print(trin, type(trin))
print(trin.encode(), type(trin.encode()))
print()

# Using Python
 
import socket

# mk a STREAM-based socket obj. 'mysock' for going across INET
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect it to 'data.pr4e.org', port 80 if it is running
mysock.connect(('data.pr4e.org', 80))
# Perpare the cmd i'll send to the running server:
# GET (form HTTP doc), \n\n: return & the blank line needed
# .encode() string method: prepare data to go across the INET
cmd = 'GET http://date.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
# And now send the cmd (little string encoded) across the INET
mysock.send(cmd)

# I choose to recieve from server
while True:
    data = mysock.recv(512)
    if len(data) < 1: break
    print(data.decode())
mysock.close()

