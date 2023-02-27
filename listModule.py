"""
GoodRoutines listBuilding and selection support
"""

# Imports
import ast
import time
import zmq
import json


# sets the routine based on time of day
def _getRoutine():

    # if before 12, set morning routine
    if time.localtime().tm_hour > 12:

        with open('GoodMorning.txt') as file:
            routineSet = file.read()
        routineSet = ast.literal_eval(str(routineSet))

    # else, set the night routine
    else:
        with open('GoodNight.txt') as file:
            routineSet = file.read()

        routineSet = ast.literal_eval(str(routineSet))

    return routineSet


"""
    
Sockets
    
"""


# use fileListBuilder.py to build list of all available images,
# from sticker or other directory
# returns list of objects in a directory
def _buildList(directory):

    #  Socket to talk to server
    context = zmq.Context()
    print("Connecting to list building server…")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5557")

    # send argument - directory to build list from
    socket.send_string(directory)

    # receive list as string and transform back to list
    imageList = socket.recv_string()
    imageList = ast.literal_eval(imageList)

    socket.close()

    return imageList


# uses chooseRandom.py to choose phrases for stickers at random
# chooseRandom accepts socket.send_string() and returns a string
# returns a list of random objects
def _setPhrases(allPhrases, numImages):

    phraseList = []

    # set up client in zmq
    context = zmq.Context()
    print("Connecting to chooseRandom server…")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5556")

    for j in range(numImages):
        # fill phrase list randomly
        socket.send_string(str(allPhrases))
        phraseList.append(socket.recv_string())

        # prevent duplicates if possible, but not perfectly
        if 0 < j < len(allPhrases):
            for k in range(j):
                while phraseList[j] == phraseList[k]:
                    # try again
                    socket.send_string(str(phraseList))
                    phraseList[j] = socket.recv_string()

        # if request fails, set default phrase "good"
        if phraseList[j] == "ERROR: Please send a list or an int":
            phraseList[j] = "good"

    socket.close()

    return phraseList


# sets the list of stickers that will be used for this iteration of the routine
# microservice_server.py needs socket.send_json() and returns a json object
# returns list of objects
def _fetchStickers(directory, images, phrases, numImages):

    stickers = []

    # set up client in zmq
    context = zmq.Context()
    print("Connecting to microservice server…")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    # using the phrase list and the image list, request a search to match keywords
    request_JSON = {"strings": phrases,
                    "files": images}

    print(request_JSON)
    print("Sending JSON")
    socket.send_json(request_JSON)

    # set sticker defaults if response fails
    if socket.poll(500) == 0:
        stickers = _defaultStickers(stickers, numImages)

    # if successful, decode reply
    else:
        print("reply received!")
        reply_json = socket.recv().decode()
        if reply_json != "format_error":
            reply_json = json.loads(reply_json)
            print(reply_json)

            # make list with stickers
            for k in range(numImages):
                stickers.append(directory + "/" + reply_json[phrases[k]])

        # if not, set defaults
        else:
            stickers = _defaultStickers(stickers, numImages)

    # close socket
    socket.close()

    return stickers


# Assign objects to list in event of microservice error
# returns list of objects
def _defaultStickers(stickerArray, numImages):

    if numImages > 1:
        for i in range(numImages):
            stickerArray.append("stickers/good_21.png")

    else:
        stickerArray.append("stickers/good_4.png")

    return stickerArray
