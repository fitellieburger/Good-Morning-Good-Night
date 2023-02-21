"""
File List Builder
by Elle Burger

Makes a list from files in a directory

"""

import zmq
import os

# set up server
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5557")

while True:

    #  Wait for next request from client
    directoryName = socket.recv_string()

    fileList = os.listdir(directoryName)

    # return list
    socket.send_string(str(fileList))
