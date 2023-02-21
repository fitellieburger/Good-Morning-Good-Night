# Author: Taylor Jordan
# GitHub username: Raptor2k1
# Date: 1/29/2023

import zmq
import json
import string
import re
import random


class AssignmentRequest:
    """An object passed along as an information request. Contains data members for a list of strings, a list of image
    file names, and a list of word."""

    def __init__(self):
        self._strings = []
        self._files = []
        self._words = []
        self._string_files_dict = {}
        self._files_subwords = {}

    def get_strings(self):
        return self._strings

    def get_files(self):
        return self._files

    def get_words(self):
        return self._words

    def get_string_files_dict(self):
        return self._string_files_dict

    def get_path_dict(self):
        return self._files_subwords

    def set_strings(self, string_list):
        self._strings = string_list

    def set_files(self, file_list):
        self._files = file_list

    def set_words(self, word_list):
        self._words = word_list

    def init_associations(self):
        """Sets up the initial association dictionary with each requested string matched to an empty array."""

        for request_string in self._strings:
            self._string_files_dict[request_string] = []

    def update_string_files_dict(self, arg_string, file):
        """Adds to or updates an entry in the object's word-image path dictionary."""

        if arg_string not in self._string_files_dict:
            self._string_files_dict[arg_string] = []
        if file not in self._string_files_dict[arg_string]:
            self._string_files_dict[arg_string].append(file)

    def file_for_word(self, word) -> str:
        """Assigns a word (in a request object) to the first matching file name string found."""
        for file in self._files:
            if word.lower() in file.lower():
                return file

    def keywords_from_files(self):
        """Scans the local image directory and returns the list of words found within file names within it."""

        # Get images from library and create dictionary entry, keyed to file paths
        files = self._files
        for file in files:
            self._files_subwords[file] = []

        # Parse image file names and add word substrings to a word list
        word_list = []
        for key in self._files_subwords.keys():
            file_string = key

            # Assumes normal 3 letter convention if period is detected at that index and slices extension off
            if key[-4] == ".":
                file_string = key[:-4]

            # Split apart all the word-ish substrings in the filename
            split_words = re.split('[_\-,.]+', file_string)

            # Check for new words from split and add to sub-word list in respective object dictionary
            for word in split_words:
                if word not in word_list:
                    if len(word) > 2:
                        self._files_subwords[key].append(word)

    def make_selection(self):
        """
        Randomly selects one of matching files in the array assigned to each string. The assignment dictionary is
        updated to match only this single string, instead of an array of possible strings. If the array is empty,
        a default value is assigned instead.
        """

        for req_string in self._string_files_dict:
            print(self._string_files_dict.keys())
            choices_available = len(self._string_files_dict[req_string])
            if choices_available < 1:
                print(self._string_files_dict[req_string])
                self._string_files_dict[req_string] = ".defaultChoice"
            else:
                random_choice = self._string_files_dict[req_string][random.randint(0, choices_available - 1)]
                self._string_files_dict[req_string] = random_choice


def process_request(request_obj):
    """
    Scans the request pipeline for an object containing a list of strings, a list of image file names,
    and list of words. If no list of words is provided, uses the currently-saved internal list.
    If either the image or string list is empty, returns an error explaining why the request is invalid.
    In either case, clears the request pipeline file after the operation is done.
    """

    # Generate list of words available within image file path names
    request_obj.keywords_from_files()

    # Filter out common irrelevant/short words and associated words/strings
    skip_list = ("the", "and", "but", "for", "are")

    # Abort if incorrect object
    if str(type(request_obj)) != "<class '__main__.AssignmentRequest'>":
        return

    # See if any words within the string are contained with an image filename and assign them if they are.
    else:
        # Check if a substring in image name or if a file substring in request substring, then update association
        string_list = request_obj.get_strings()
        check_forward(request_obj, string_list, skip_list)
        check_reverse(request_obj, skip_list)

        # If multiple matches, randomly selects one, then send the updated request object to the outgoing pipeline
        request_obj.make_selection()
        send_info(request_obj)


def check_forward(request_obj, string_list, skip_list):
    """
    Checks if any request object's string's substrings are contained within a file name and updates the string-file
    association if it is.
    """
    print("\nFORWARD SEARCH START")
    for req_string in string_list:
        string_words = req_string.split()
        for word in string_words:
            cleaned_word = remove_special_chars(word)
            if cleaned_word.lower() in skip_list or len(cleaned_word) < 3:
                continue  # Skip this substring if it's a known irrelevant factor
            word_file = request_obj.file_for_word(cleaned_word)
            if word_file:
                request_obj.update_string_files_dict(req_string, word_file)
                print("FORWARD MATCH:", word_file)


def check_reverse(request_obj, skip_list):
    """
    Iterates through strings in the request object and searches for strings still bound to a default image.
    If they are, checks if any filename substrings are contained within the request object's main string.
    Updates the string-file association if it is.
    """
    print("\nREVERSE SEARCH START")
    for each_string in request_obj.get_strings():
        for key in request_obj.get_path_dict():
            for word_in_path in request_obj.get_path_dict()[key]:
                cleaned_img_word = remove_special_chars(word_in_path)
                if cleaned_img_word.lower() in skip_list or len(cleaned_img_word) < 3:
                    continue  # Skip this substring if it's a known irrelevant factor

                if cleaned_img_word.lower() in each_string.lower():
                    request_obj.update_string_files_dict(each_string, key)
                    print("Reverse Match:", request_obj.get_path_dict()[key])


def send_info(request_obj):
    """
    Updates the return pipeline file with a key and path that matches the input string received.
    Takes an array of request objects as a parameter, each having data members for a string, a key,
    an image file name, and a path to the image.
    """
    # open and write self.request's object or its dictionary attribute
    send_data = request_obj.get_string_files_dict()
    socket.send_json(send_data)


# Adapted from explanation of strings module located here:
# https://www.scaler.com/topics/remove-special-characters-from-string-python/
def remove_special_chars(substring: str) -> str:
    """Returns an argument string with special characters removed."""
    word = substring.translate(str.maketrans('', '', string.punctuation))
    return word


# Set up Server's socket container/transport and bind socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.setsockopt(zmq.SNDTIMEO, 500)
socket.setsockopt(zmq.LINGER, 0)
socket.bind("tcp://*:5555")

print("Server started!\n")

while True:
    # Listen for client request
    request_str = socket.recv().decode()
    request_dict = json.loads(request_str)
    print("Received Request JSON...")
    print(request_dict)

    # Error handling - if not both a strings and images key, reply with an error message
    if "strings" not in request_dict or "files" not in request_dict or len(request_dict["strings"]) < 1:
        print("Error: Request contained improper structure. Sending error message.")
        socket.send_string("format_error")
        print("Format error reply sent.")

    else:
        # Create an object for the request
        assignment_request_obj = AssignmentRequest()
        assignment_request_obj.set_files(request_dict["files"])
        assignment_request_obj.set_strings(request_dict["strings"])
        assignment_request_obj.init_associations()

        # Process the request object and send appropriate reply
        process_request(assignment_request_obj)
        print("Attempted to send reply.")


# Need to add a place to make sure all request strings have an empty set at start
