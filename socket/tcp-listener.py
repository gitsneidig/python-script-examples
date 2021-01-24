#! /usr/bin/python

# import socket module
import socket

# assign parameter values to variables
TCP_IP = "192.168.181.190"
TCP_PORT = 6996
BUFFER_SIZE = 60

# define the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to an IP address and port
s.bind((TCP_IP, TCP_PORT))
# specify listen method
s.listen (1)

# capture IP and port of connecting system using accept method
conn, addr = s.accept()
# print IP and port
print ('Connection address: ', addr)

# while 1 to keep checking for data indefinitly until program is stopped
# returns HTTP method, and user agent
while 1:
    data=conn.recv(BUFFER_SIZE)
    if not data:break
    print ("Received data: ", data)
        conn.send(data) #echo

conn.close