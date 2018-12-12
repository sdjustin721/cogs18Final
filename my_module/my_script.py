import string
import random

# Functions to used for the chatbot
from data import music_genre_interface

def is_question(input_string):
    if '?' in input_string:
        output = True
    else:
        output = False
    return output


def remove_punctuation(input_string):
    out_string = ''
    for char in input_string:
        if char not in string.punctuation:
            out_string += char
    return out_string


def prepare_text(input_string):
    out_list = []
    input_string = input_string.lower()
    input_string = remove_punctuation(input_string)
    out_list = input_string.split()
    return out_list


def selector(input_list, check_list, return_list):
    output = None
    for item in input_list:
        if item in check_list:
            output = random.choice(return_list)
            break
    return output


def string_concatenator(string1, string2, separator):
    output = []
    output = string1 + separator + string2
    return output


def list_to_string(input_list, separator):
    output = input_list[0]
    for item in input_list[1:]:
        output = string_concatenator(output, item, separator)
    return output


def end_chat(input_list):
    output = bool()
    if 'exit' in input_list:
        output = True
    else:
        output = False
    return output


def is_in_list(list_one, list_two):

    for element in list_one:
        if element in list_two:
            return True
    return False


def find_in_list(list_one, list_two):

    for element in list_one:
        if element in list_two:
            return element
    return None


def drock_chat():
    # Function to run the actual chatbot
    inp = None
    while not inp == 'exit':
        genre_selected = input('Please select the music genre you want to talk about (rock or pop): ')
        if genre_selected.lower().startswith('po'):
            genre = 'pop'
            break
        elif genre_selected.lower().startswith('ro'):
            genre = 'rock'
            break
        else:
            print('Please enter a valid choice. Type "exit" to enter')
            continue

    while True:

        msg = input('ME :\t')
        out_msg = None

        genre_dict =  music_genre_interface[genre]

        # Check if input is a question
        question = is_question(msg)

        # Prepare input message
        msg = prepare_text(msg)

        # Checks for end message
        if end_chat(msg):
            out_msg = 'Bye!'
            chat = False
            break

        if not out_msg:
            outs = []
			# topics including greeting, guitar, bass, drum, singers, and billboard chart, etc. 
            outs.append(selector(msg, genre_dict['FIRST_IN'], genre_dict['FIRST_OUT']))
            outs.append(selector(msg, genre_dict['GUITAR_IN'], genre_dict['GUITAR_OUT']))			
            outs.append(selector(msg, genre_dict['BASS_IN'], genre_dict['BASS_OUT']))
            outs.append(selector(msg, genre_dict['DRUM_IN'], genre_dict['DRUM_OUT']))
            outs.append(selector(msg, genre_dict['VOCAL_IN'], genre_dict['VOCAL_OUT']))
            outs.append(selector(msg, genre_dict['TOPCHART_IN'], genre_dict['TOPCHART_OUT']))
			
			# Speical algorithm to spit out famouns musicians
            if is_in_list(msg, genre_dict['FAMOUS_IN']):
                name = find_in_list(msg, genre_dict['FAMOUS_IN'])
                outs.append(list_to_string([genre_dict['FAMOUS_NAMES'][name], name.capitalize(),
                                            selector(msg, genre_dict['FAMOUS_IN'], genre_dict['FAMOUS_OUT'])],
                                           ' '))
            # The chatter prohibited word strings
            if is_in_list(msg, genre_dict['DONOTLIKE_IN']):
                outs.append(list_to_string([selector(msg, genre_dict['DONOTLIKE_IN'], 
											genre_dict['DONOTLIKE_OUT']),
                                            find_in_list(msg, genre_dict['DONOTLIKE_IN'])], ' '))
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)
        # Words DROCK doesn't know
        if not out_msg:
            out_msg = random.choice(genre_dict['OTHERS'])

        print('DROCK:', out_msg)

drock_chat()