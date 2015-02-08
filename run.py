#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This file is part of Pyelevator

Pyelevator is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Pyelevator is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero Public License for more details.

You should have received a copy of the GNU Affero Public License
along with Pyelevator.  If not, see <http://www.gnu.org/licenses/>.
"""
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
    # Create an instance of the elevator class (ID / bottom floor / top floor) 
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


