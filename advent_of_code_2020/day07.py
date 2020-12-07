"""
https://adventofcode.com/2020/day/6

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""

import unittest

input_file = r'resources/day7_input.txt'


def part_1(data):
    for line in data:
        print(line)

    return -1


def read_input_data(filename):
    with open(filename) as file:
        data = [line.strip() for line in file.readlines()]

    return data


class TestDay7(unittest.TestCase):
    def test_part_1(self):
        result = part_1(read_input_data(input_file))

        print('Part1:', result)
        self.assertEqual(0, result)


if __name__ == '__main__':
    unittest.main()
