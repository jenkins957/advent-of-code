"""
https://adventofcode.com/2015/day/3
"""


import unittest


def number_of_houses_visited(input):
    x = 0
    y = 0
    locations = set()
    locations.add((x, y))

    for c in input:
        if c == '^':
            y += 1
        elif c == 'v':
            y -= 1
        elif c == '>':
            x += 1
        elif c == '<':
            x -= 1

        locations.add((x,y))

    return len(locations)


def read_input_data(filename):
    with open(filename) as file:
        return file.read()


class TestDay03(unittest.TestCase):

    def test_visit_houses(self):
        self.assertEqual(1, number_of_houses_visited(''))
        self.assertEqual(2, number_of_houses_visited('>'))
        self.assertEqual(4, number_of_houses_visited('^>v<'))
        self.assertEqual(2, number_of_houses_visited('^v^v^v^v^v'))

    def test_part1(self):
        instructions = read_input_data('resources/day3_input.txt')
        print(instructions)
        result = number_of_houses_visited(instructions)
        print('Number of houses visited:', result)
        self.assertEqual(2565, result)


if __name__ == '__main__':
    unittest.main()
