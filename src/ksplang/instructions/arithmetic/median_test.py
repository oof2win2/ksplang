from math import floor
from statistics import median

from .median import MedianInstruction


def test_median_single(execute_single_instruction):
    assert execute_single_instruction(MedianInstruction, [1]) == [1]


def test_median_multiple(execute_single_instruction):
    assert execute_single_instruction(MedianInstruction, [1, 2, 3, 4, 5]) == [3]


def test_median_even(execute_single_instruction):
    assert execute_single_instruction(MedianInstruction, [1, 2, 3, 4]) == [2]


def test_median_unsorted(execute_single_instruction):
    assert execute_single_instruction(MedianInstruction, [4, 3, 2, 1, 5]) == [3]


def test_median_many(execute_single_instruction):
    # numbers from 1 to 10k inclusive
    stack = [x for x in range(1, 10_001)]
    med = floor(median(stack))

    print(median(stack), med)
    assert execute_single_instruction(MedianInstruction, stack) == [med]
