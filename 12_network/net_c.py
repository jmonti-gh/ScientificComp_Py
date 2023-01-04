''' A puntual Web Browser request '''

# Using - telnet IP port - you can do it:
# $ telnet www.dr-chuck.com 80
# Trying IP...
# Connected to....
# GET http://www.dr-ch....

# ___ data recived.....

# AUX: .encode() -turns tring to bytes & .decode(): vicebersa
def prt_from_var_as_str(st):    # void funct only print idvar, valvar, aand typevar
    id_colon = st + ':'
    var = eval(st)
    tyvar = "'" + type(var).__name__ + "'"  # tyvar2 = var.__class__.__name__
    print("Type: {:<8} -> {:<12}".format(tyvar, id_colon), var)
    
trin = 'Pythön'
prt_from_var_as_str('trin')
trinbyte = trin.encode()
prt_from_var_as_str('trinbyte')
trinagain = trinbyte.decode()
prt_from_var_as_str('trinagain')
print()

# Using Python (instead of telnet showed in first comments)
import socket

# mk a STREAM-based socket obj. 'mysock' for going across INET
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect it to 'data.pr4e.org', port 80 if it is running
mysock.connect(('data.pr4e.org', 80))
# Perpare the cmd i'll send to the running server:
# GET (form HTTP doc), \n\n: return & the blank line needed
# .encode() string method: prepare data to go across the INET
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# And now send the cmd (little string encoded) across the INET
## mysock.send(cmd)
mysock.send(b"GET /romeo.txt HTTP/1.1\r\nHost:data.pr4e.org\r\n\r\n")
#mysock.send(b"GET / HTTP/1.1\r\nHost:data.pr4e.org\r\n\r\n")

# I choose to recieve from server
while True:
    data = mysock.recv(512)
    if len(data) < 1: break
    print(data.decode())
mysock.close()

a = input()
# .connect {mysock.connect(('data.pr4e.org', 80))} is dangerous, for ex. wo/INET:
# Traceback... | socket.gaierror: [Errno 11002] getaddrinfo failed

target_host = "www.google.com" 
target_port = 80  # create a socket object 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
# connect the client 
client.connect((target_host,target_port))  
# send some data 
request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
client.send(request.encode())  
# receive some data 
response = client.recv(4096)  
http_response = repr(response)
http_response_len = len(http_response)
#display the response
# gh_imgui.text("[RECV] - length: %d" % http_response_len)
# gh_imgui.text_wrapped(http_response)
print(response.decode())