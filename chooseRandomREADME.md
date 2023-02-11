# ChooseRandom.py Microservice
# Requirements
Python 3.x
ZMQ Module

# Explanation
This microservice returns a random selection from a list. It may also return an index when given a list length. The microservice, once started, will listen for requests and return the appropriate item.

# Use
Open a command-line terminal window and run chooseRandom.py from it’s directory.
Run the program which will send the request.

# Sending Requests
Open a socket with the following code:
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5556")

# Send a string using the send string function:
socket.send_string(str(list))
Or
socket.send_string(str(len(list))

The server will return a string with the recv_string() function:
message = socket.recv_string()

If client sent an int value, client should change the returned string to an int and use it as the index in your list.
If the value from the client is not an int or a list, the client will return an error message.

**Example Call: Valid Client Requests**
![ExampleCall](https://github.com/fitellieburger/CS361/blob/643b5292488133a0ca7664c54ae6c2fd1a55ee8a/client_test.jpg)

**Sequence UML Diagram**
![chooseRandomUML](https://github.com/fitellieburger/CS361/blob/643b5292488133a0ca7664c54ae6c2fd1a55ee8a/chooseRandomUML.jpg)
