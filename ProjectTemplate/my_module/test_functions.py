"""Test for my functions."""

from my_module.functions import *
##
##

def test_petitions():
    expected = "Yay, signing petitions is a great way to push for change!" + "\n \t I sent you to a list of petitions that have yet to reach their goals." + "\n \t Is there anything else I can help you with? To quit, reply with 'QUIT'."
    assert petitions() == expected

def test_response():
    sample = "sign petitions"
    prepare_text(sample)
    expected = petitions()
    assert response(sample) == expected
    



         