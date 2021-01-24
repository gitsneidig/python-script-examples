#! /usr/bin/python

# open a socket connection to an IP address on port 22 
# will return application, version and operating system
# are running at this address

# import socket module
import socket

# add list of ports to scan
Ports = [21,22]

# loop through the list of ports to listen to
for i in range (0,4):
    
    # assign socket class instance to var s
    sock = socket.socket()

    # assign port for this loop to variable
    Port = Ports[i]

    # use socket connect method to make network connection to IP on port 22
    sock.connect(("192.168.1.101", Port))

    # use receive method to read 1024 bytes from socket
    answer = sock.recv(1024)

    # print response
    print(Port)
    print (answer)

    # close socket connection
    sock.close