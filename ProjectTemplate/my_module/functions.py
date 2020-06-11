"""A collection of functions for doing my project."""

import webbrowser

# From A3 ChatBot
def string_concatenator ( string1, string2, separator):
    """Adds strings together with separator between them
    Parameters
    ----------
    string1: string
        The front string to add 
    string2: string
        The following string to add
    separator: string 
        The string that goes between two strings
    Returns
    -------
            string
        Added string of two strings with the separator 
    """
    return string1+separator+string2

def prepare_text(input_string):
    """Helper method to split the string into words and make all lower case. 
    Parameters
    ----------
    input_string: string
        A string that user input 
    Returns
    -------
    out_list: list
        List representation of input after modifying
    """
    temp_string = input_string.lower()
    out_list = temp_string.split()
    return out_list

def list_to_string (input_list, separator):
    """Helper method to change the list to string with separator between them
    Parameters
    ----------
    input_list: list
        list that contains user input
    separator: string
        A string that goes between each string 
    Returns
    -------
    output: string
        String representation of the list with separator 
    """
    output = input_list[0]
    for item in input_list[1:]:
        output = string_concatenator(output, item, separator)
    return output

def end_chat (input_list):
    """Ends the chat if the input matches 'quit'
    Parameters
    ----------
    input_list: list
        the list that contains user input
    Returns
    -------
            boolean
        Whether the input was quit or exit or none 
    """
    if 'quit' in input_list:
        return True
    else:
        return False
        
def is_in_list(list_one, list_two):
    """ Check if any element of list_one is in list_two.
    Parameters
    ----------
    list_one: list 
        List to check if its inside the two
    list_two: list
        List to see if one belongs inside 
        
    Returns
    -------
            boolean
        Boolean whether list_one exists or not 
    """
    for element in list_one:
        if element in list_two:
            return True
    return False

# My own functions
def petitions():
    """Helper method to create chatbot response about petitions
    Parameters
    ----------
        NONE
    Returns
    -------
    output: string
        Chatbot response 
    """
    output = "Yay, signing petitions is a great way to push for change!"
    output += "\n \t I sent you to a list of petitions that have yet to reach their goals." 
    output += "\n \t Is there anything else I can help you with? To quit, reply with 'QUIT'."
    webbrowser.open('https://pendingpetition.carrd.com')
    return output

def call():
    """Helper method to create chatbot response about calling
    Parameters
    ----------
        NONE
    Returns
    -------
    output: string
        Chatbot response 
    """
    output = "Yay, calling is a great way to push for change!"
    output += "\n \t There's a lot of people you can contact via text/call/email."
    output += "\n \t Is there anything else I can help you with? To quit, reply with 'QUIT'."
    webbrowser.open('https://blacklivesmatters.carrd.com/#text')
    return output
    
def donate():
    """Helper method to create chatbot response about donating
    Parameters
    ----------
        NONE
    Returns
    -------
    output: string
        Chatbot response 
    """
    output = "Donating is a great way to support and push for change!"
    output += "\n \t This is a great Google Doc that gets updated daily."
    output += "\n \t Is there anything else I can help you with? To quit, reply with 'QUIT'."
    url = 'https://docs.google.com/document/d/12y7-Wa4gi8HUeFTv17gPcbMGuVX5cqIudLJmhOrq1-k/edit?usp=sharing'
    webbrowser.open(url)
    return output

def learn():
    """Helper method to create chatbot response about learning
    Parameters
    ----------
        NONE
    Returns
    -------
    output: string
        Chatbot response 
    """
    output = "An important part to pushing for justice requires people to be educated."
    output += "\n \t Take the time to read/watch these!"
    output += "\n \t Is there anything else I can help you with? To quit, reply with 'QUIT'."
    webbrowser.open('https://blacklivesmatters.carrd.co/#educate')
    return output

def vote():
    """Helper method to create chatbot response about voting
    Parameters
    ----------
        NONE
    Returns
    -------
    output: string
        Chatbot response 
    """
    output = "To make change, we need YOU to vote because EVERY vote counts!"
    output += "\n \t You can register to vote at vote.gov :)" 
    output += "\n \t Is there anything else I can help you with? To quit, reply with 'QUIT'."
    webbrowser.open('https://vote.gov')
    return output

def more():
    """Helper method to create chatbot response about more info
    Parameters
    ----------
        NONE
    Returns
    -------
    output: string
        Chatbot response 
    """
    output = "There's so many things we can do to suppport such as streaming a playlist."
    output += "\n \t Proceeds will be donated to causes that support the BLM movement!"
    output += "\n \t Is there anything else I can help you with? To quit, reply with 'QUIT'."
    webbrowser.open('https://www.youtube.com/playlist?list=PLtooIklzheqzORPbQBiEZKsw2T4s6SUxv')
    return output

def response(input_string): 
    """Helper method to check what information the user wants
    Parameters
    ----------
    input_string: string
        User input
    Returns
    -------
    output: string
        Chatbot response 
    """
    if 'petitions' in input_string: 
        output = petitions()
    elif 'call' in input_string: 
        output = call()
    elif 'donate' in input_string: 
        output = donate()
    elif 'vote' in input_string: 
        output = vote()
    elif 'learn' in input_string: 
        output = learn()
    elif 'more' in input_string: 
        output = more()
    else:
        output = "Sorry, I don't understand."
        output += "\n \t Type 'SIGN PETITIONS', 'CALL', 'DONATE', 'VOTE', 'LEARN' or 'MORE'."
    return output

def start_chat():
    """Main function to run bot. """
    start_msg = "Hello, I'm TyTy! How can I assist you today?" 
    start_msg += "\n \t Type 'SIGN PETITIONS', 'CALL', 'DONATE', 'VOTE', 'LEARN' or 'MORE'."
    print('TYTY :\t', start_msg)
    chat = True
    while chat:
        # Get a message from the user
        msg = input('ME : \t')
        out_msg = None

        # Prepare the input msg
        msg = prepare_text(msg)
        
        # Prepare the output msg
        out_msg = response(msg)

        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'I hope I was helpful. Goodbye!'
            chat = False
        
        # Send the output msg
        print('TYTY:\t', out_msg)
        