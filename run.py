#!/usr/bin/python
# -*- coding: utf-8 -*-

from elevator import *
from thread import *
import socket
import sys
import time

def main(conn):

    while True:
        # Send current status to the client
        conn.send(e.status())
        conn.send('/+_+\: ')

        # Get data from client
        data = conn.recv(1024)
        if data:
            try:
                # Iterate over items
                for i in e.goto( int(data) ):
                    # Send response to the client
                    conn.send(i)
                    time.sleep(1)
            except:
                pass
    conn.close()
        
if __name__ == "__main__":
    # Create an instance of the elevator class (ID / bottom / top) 
    e = elevator(1, 0, 13)
    # Default hostname
    host = socket.gethostname()
    # Default socket port
    port = 2222
    # Create a socket
    s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    # Bind socket
    try:
        s.bind((host, port))
    except socket.error , msg:
        print "[" + str(msg[0]) + '] ' + msg[1]
        sys.exit()
    # Start listening
    s.listen(10)
    # Keep talking with the client
    while 1:
        # Wait to accept a connection
        conn, addr = s.accept()
        e.catchclient(addr[0] + ':' + str(addr[1]))
        # Start a thread
        start_new_thread(main , (conn,))
    s.close()


