"""
chooseRandom.py
2/6/23 Ellie Burger

Microservice to return a random value from a list,
OR an int for the index of list


References

PyZMQ docs by Brian E. Granger & Min Ragan-Kelley
https://pyzmq.readthedocs.io/en/v17.1.1/unicode.html

Debugging with support from OpenAI chatGPT
Jan 30 Version

"""


# imports
import zmq
import random
import ast

# set up server
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")

while True:
    #  Wait for next request from client
    # request should be a list, however there may be client error
    currentList = socket.recv_string()

    # convert a string of a list to a list
    if currentList[0] == "[" or currentList[0] == "(":
        currentList = ast.literal_eval(currentList)

    # if the string is not a list, check if it is an int
    else:
        try:
            currentList = int(currentList)
        except:
            currentList = currentList

    # if currentList is a list
    if isinstance(currentList, list):
        chooseIndex = random.randint(0, 4294967295) % len(currentList)-1

        # return value at selected index
        socket.send_string(str(currentList[chooseIndex]))

    # if currentList is an int
    elif isinstance(currentList, int):
        returnInt = random.randint(0, 4294967295) % currentList

        # return int value so client can use to select an index
        socket.send_string(str(returnInt))

    # else, return an error message
    else:
        socket.send(b"ERROR: Please send a list or an int")



