# greenlet-chatserver-example
Simple chatserver created to learn about greenlets in python

## Installation
pip install -r requirements.txt

##Useage

To send messages:

```
telnet localhost 8080
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
Hello, World from bob
ACK
```

To run the server (listens on localhost:8080):

```
~/greenlet-chatserver-example$ python webserver.py 
Client 127.0.0.1:48941 connected
Client 127.0.0.1:48943 connected
MSG from 127.0.0.1:48941:
Hello, World from bob
MSG from 127.0.0.1:48943:
Hello, World from alice
```
