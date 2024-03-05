from plates import is_valid

def test_is_valid():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False
    assert is_valid('CS50P') == False

def test_is_valid_No_punctuation():
    assert is_valid('PI3.14') == False

def test_is_valid_letterslimit():
    assert is_valid('H') == False
    assert is_valid('OUTATIME') == False

def test_is_valid_start_at_letter():
    assert is_valid('123CS') == False

def test_star_with_twoletter():
    assert is_valid('AA') == True
    assert is_valid('A2') == False
    assert is_valid('2A') == False
    assert is_valid('22') == False
