"""
https://adventofcode.com/2018/day/1

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""


import unittest


def calculate_frequency(input):
    current_frequency = 0

    for line in input:
        op = line[:1]
        number = int(line[1:])

        if op == '+':
            current_frequency += number
        else:
            current_frequency -= number

    return current_frequency


def calculate_frequency_first_reached_twice(input):
    frequencies = set()

    current_frequency = 0

    # Lets not loop forever, give up after n loops
    max_iterations = 1000

    while max_iterations > 0:
        for line in input:
            op = line[:1]
            number = int(line[1:])

            if op == '+':
                current_frequency += number
            else:
                current_frequency -= number

            if current_frequency in frequencies:
                return current_frequency

            frequencies.add(current_frequency)
        max_iterations -= 1

    return None


def read_input_data(filename):
    with open(filename) as file:
        return file.read().splitlines()


class TestDay01(unittest.TestCase):

    def test_calculate_frequency(self):
        input = ['+1', '-2', '+3', '+1']
        self.assertEqual(3, calculate_frequency(input))

    def test_calculate_frequency_reached_twice(self):
        input = ['+1', '-2', '+3', '+1']
        self.assertEqual(2, calculate_frequency_first_reached_twice(input))

    def test_part1(self):
        result = calculate_frequency(read_input_data(r'resources/day1_input.txt'))
        self.assertEqual(454, result)

    def test_part2(self):
        result = calculate_frequency_first_reached_twice(read_input_data(r'resources/day1_input.txt'))
        self.assertEqual(566, result)


if __name__ == '__main__':
    unittest.main()
