from um import count

def test_count_sentence():
    assert count('um') == 1
    assert count('Um, thanks for the album') == 1
    assert count('Um, thanks, um...') == 2

def test_count_words():
    assert count('yum') == 0
    assert count('yummy') == 0

def test_count_combo():
    assert count('Um this cake is yum') == 1
    assert count('Oh God this is so yummy') == 0
