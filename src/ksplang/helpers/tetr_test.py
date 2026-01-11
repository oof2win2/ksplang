from .tetr import tetr

# values from Wikipedia, as per https://en.wikipedia.org/wiki/Tetration#Examples


def test_tetr_two():
    assert tetr(2, 2) == 4
    assert tetr(2, 3) == 16
    assert tetr(2, 4) == 65_536


def test_tetr_three():
    assert tetr(3, 2) == 27
    assert tetr(3, 3) == 7_625_597_484_987


def test_tetr_zero():
    assert tetr(2, 0) == 1
    assert tetr(3, 0) == 1
