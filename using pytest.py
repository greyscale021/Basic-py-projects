#installed pytest by "pip install pytest"
def is_even(n):
    return n%2 == 0
def test_is_even():
    assert is_even(2) == True
def test_is_odd():
    assert is_even(3) == False