from aoc import aoc_read_input
from os import path


def transform_input(input_vals: List) -> List:
    return []


def func1(input_vals: List):
    return None


if __name__ == "__main__":
    input_vals = aoc_read_input(path.abspath(__file__))
    input_vals = transform_input(input_vals)
    print(func1(input_vals))
