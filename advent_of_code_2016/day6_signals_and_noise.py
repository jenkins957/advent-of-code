"""
https://adventofcode.com/2016/day/6

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""


import unittest
from collections import OrderedDict


def clean_up_signal(data, most_common=True):
    lines = []
    for line in data:
        row = []
        for c in line:
            row.append(c)
        lines.append(row)

    return find_common_characters(lines, most_common)


def find_common_characters(list, most_common=True):
    word = ''
    index = 0

    while index < len(list[0]):
        characters = {}
        for row in list:
            c = row[index]
            if c not in characters:
                characters[c] = 1
            else:
                characters[c] += 1

        ordered_dictionary = dict(OrderedDict(sorted(characters.items(), reverse=not most_common, key=lambda t: t[1])))
        print(ordered_dictionary)
        word += ordered_dictionary.popitem()[0]
        index += 1

    return word


def read_input_data(filename):
    with open(filename) as file:
        return file.read().splitlines()


class TestDay06(unittest.TestCase):

    def test_example_data_part1(self):
        result = clean_up_signal(read_input_data(r'resources/day6_test_input.txt'))
        print(result)
        self.assertEqual('easter', result)

    def test_part1(self):
        result = clean_up_signal(read_input_data(r'resources/day6_input.txt'), False)
        print(result)
        self.assertEqual('owlaxqvq', result)


if __name__ == '__main__':
    unittest.main()
