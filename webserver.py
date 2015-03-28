#! /usr/bin/env python

import gevent
import socket


MAX_CONN = 5
MAX_MSG_LEN = 2048

def init(host, port, max_connections = MAX_CONN):
    '''
    Initializes the listening socket and returns it
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(max_connections)
    return s

def handle_connections(s):
    '''
    Loops through connections and kicks them off to greenlets 
    to process
    '''

    while 1:
        client, addr = s.accept()
        gevent.spawn(handle_client, client, addr)
        gevent.sleep(0)
        

def handle_client(c, addr):
    '''
    Prints out the client's message and acks the response
    '''
    print "Client {}:{} connected".format(addr[0], addr[1])
    msg = c.recv(MAX_MSG_LEN)
    print "MSG from {}:{}:".format(addr[0], addr[1])
    print msg

    c.send("ACK\n")

def main():

    HOST = "localhost"
    PORT = 8080

    s = init(HOST, PORT)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen = gevent.spawn(handle_connections, s)
    gevent.joinall([listen])

if __name__ == '__main__':
    main()

