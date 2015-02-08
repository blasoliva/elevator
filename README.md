## Elevator
Python network programming

####Usage:

Run the main script:
```
./run.py
```

Connect to the socket with telnet client: 
```

blas@computerliebe:~/pyelevator$ telnet computerliebe 2222
Trying 127.0.1.1...
Connected to computerliebe.local.
Escape character is '^]'.

ID: 1 
Top: 13
Position: 0
Clients: 1

/+_+\:
```

Type a number from 0 to X and move the elevator up and down:
```
/+_+\: 6
Moving up from 0 to 6
Moving up from 1 to 6
Moving up from 2 to 6
Moving up from 3 to 6
Moving up from 4 to 6
Moving up from 5 to 6

ID: 1 
Top: 13
Position: 6
Clients: 1

/+_+\: 2
Moving down from 6 to 2
Moving down from 5 to 2
Moving down from 4 to 2
Moving down from 3 to 2

ID: 1 
Top: 13
Position: 2
Clients: 1

/+_+\: 
```

Great fun for nerdy people!

### TODO
* Implement the ***queue*** function to scan the requests as a true elevator
* Use multiple instances of ***elevator***
* Get in and get out of the elevator
* Call the elevator from outside
* Move the elevator from inside
* Send messages to other clients
