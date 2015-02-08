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

class elevator:

    def __init__(self, uid, bottom, top):
        """ Initialize variables
        uid -- ID
        top -- Top position
        bottom -- Bottom position
        position -- Current position
        direction -- 0 : down / 1 : up 
        queue_up -- Queue up requests
        queue_down -- Queue down requests
        clients -- Connected clients information
        """ 
        self.uid = uid
        self.top = top
        self.bottom = bottom
        self.position = 0
        self.direction = None
        self.queue_up = []
        self.queue_down = []
        self.clients = []
        
    def goto(self, request):
        """ Gets the request and moves up or down, set the current position
        and returns the steps into a list to the main application
        request - Requested position
        position -- Current position
        steps -- Motion's steps
         """
        steps = []

        if request <= self.top \
          and request >= self.bottom:
            # Moving up
            if request > self.position:
                self.direction = 1
                for i in range(request - self.position):
                    steps.append("Moving up from %s to %s\n" % \
                                    (i + self.position, request))
            # Or moving down                        
            elif request < self.position:
                self.direction = 0
                for i in range(self.position - request):
                    steps.append("Moving down from %s to %s\n" % \
                                    (self.position - i, request))
            # Set current position
            self.position = request
            return steps
            
    def status(self):
        """ Return current status """
        return "\nID: %s \nTop: %s\nPosition: %s\nClients: %s\n" % \
          (self.uid, self.top, self.position, len(self.clients)) + "\n"

    def queue(self, request, direction):
        """ Sorts the requests queue
        Scans toward the nearest end and attends along the way.
        Once hits the bottom or top it jumps to the other end and
        moves in the same direction. Something like circular scan.
        """
        if direction is 1 and request not in self.queue_up:
            self.queue_up.append(request)
            self.queue_up.sort()
            q = [ a for a in self.queue_up if a > self.current ] + \
                [ b for b in self.queue_up if b < self.current ]
            self.queue_up = q
            
        elif direction is 0 and request not in self.queue_down:
            self.queue_down.append(request)
            self.queue_down.sort(reverse=True)
            q = [ a for a in self.queue_down if a < self.current ] + \
                [ b for b in self.queue_down if b > self.current ]
            self.queue_down = q

    def catchclient(self, client):
        """ Get connected clients information """
        self.clients.append(client)
