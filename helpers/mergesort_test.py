from random import random

from .mergesort import mergesort

# values from Wikipedia, as per https://en.wikipedia.org/wiki/Tetration#Examples


def test_mergesort_small():
    numbers = [x for x in range(10)]
    # shuffle
    unsorted = sorted(numbers, key=lambda x: random())
    assert mergesort(unsorted) == numbers


def test_mergesort_large():
    numbers = [x for x in range(100_000)]
    # shuffle
    unsorted = sorted(numbers, key=lambda x: random())
    assert mergesort(unsorted) == numbers
