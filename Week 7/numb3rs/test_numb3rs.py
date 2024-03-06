from numb3rs import validate
import sys

def test_validate_number():
    # checking valid ip adresses
    assert validate('255.255.255.255') == True
    assert validate('512.512.512.512') == False
    assert validate('1.2.3.1000') == False
    assert validate("255.0.0.0") == True
    assert validate("256.0.0.0") == False
    assert validate("255.255.0.0") == True
    assert validate("255.256.0.0") == False
    assert validate("255.255.255.0") == True
    assert validate("255.255.256.0") == False
    assert validate("255.255.255.255") == True
    assert validate("255.255.255.256") == False


def test_validate_string():
    # checking if ip adresses is a string
    assert validate("cAT") == False
    assert validate("What's happening?") == False

#def check_IPv4():

