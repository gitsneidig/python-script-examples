#! /usr/bin/python

# open a socket connection to an IP address on port 22 
# will return application, version and operating system
# are running at this address

# import socket module
import socket

# assign socket class instance to var s
sock = socket.socket()

# use socket connect method to make network connection to IP on port 22
sock.connect(("192.168.1.101", 22))

# use receive method to read 1024 bytes from socket
answer = sock.recv(1024)

# print response data
print (answer)

# close socket connection
sock.close