#! /usr/bin/env python

import argparse
import gevent
import socket
import time
import fcntl
import os
import errno

def parse_args():
    p = argparse.ArgumentParser(description = \
    '''
    Connect to a chatserver and send some messages
    ''')
    p.add_argument('--host', type=str, default='localhost', help='host to connect to')
    p.add_argument('--port', type=int, default=8080, help='host to connect to')
    p.add_argument('--size', type=int, default=1024, help='size, in bytes of each message')
    p.add_argument('--num', type=int, default=10, help='number of messages to send')
    return p.parse_args()

def construct_message(size):
    return 'a'*size

def send_message(s, msg, num=10):

    for i in range(num):
        s.send(msg)
    time.sleep(5)
        

def main():
    args = parse_args()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((args.host, args.port))
    msg = construct_message(args.size)
    send_message(s, msg)

if __name__ == '__main__':
    main()

