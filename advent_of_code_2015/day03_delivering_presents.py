"""
https://adventofcode.com/2015/day/3

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
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


def houses_visited(input):
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

    return locations


def number_of_houses_visited_alternate(input):
    dataset1 = input[::2]
    dataset2 = input[1::2]

    result1 = houses_visited(dataset1)
    result2 = houses_visited(dataset2)
    result3 = result1 | result2
    return len(result3)


def read_input_data(filename):
    with open(filename) as file:
        return file.read()


class TestDay03(unittest.TestCase):

    def test_visit_houses(self):
        self.assertEqual(1, number_of_houses_visited(''))
        self.assertEqual(2, number_of_houses_visited('>'))
        self.assertEqual(4, number_of_houses_visited('^>v<'))
        self.assertEqual(2, number_of_houses_visited('^v^v^v^v^v'))

    def test_visit_houses_alternate_with_robot(self):
        self.assertEqual(3, number_of_houses_visited_alternate('^v'))
        self.assertEqual(3, number_of_houses_visited_alternate('^>v<'))
        self.assertEqual(11, number_of_houses_visited_alternate('^v^v^v^v^v'))

    def test_part1(self):
        instructions = read_input_data('resources/day3_input.txt')
        result = number_of_houses_visited(instructions)
        print('Number of houses visited:', result)
        self.assertEqual(2565, result)

    def test_part2(self):
        instructions = read_input_data('resources/day3_input.txt')
        result = number_of_houses_visited_alternate(instructions)
        print('Number of houses visited by both:', result)
        self.assertEqual(2639, result)


if __name__ == '__main__':
    unittest.main()
