import unittest
from collections import OrderedDict
import re
"""
https://adventofcode.com/2016/day/4

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""


def parse_input(input_string):
    number = re.findall(r'\d+', input_string)

    m = re.search(r"\[([A-Za-z0-9_]+)\]", input_string)

    string = ''
    for c in input_string:
        if c.isdigit():
            break
        string += c

    return string[:-1], number[0], m.group(1), input_string


def perform_checksum(input_string):
    characters = {}
    for c in input_string:
        if c >= 'a' <= 'z':
            if c not in characters:
                characters[c] = (1000 - ord(c))
            else:
                characters[c] += (1000 - ord(c))

    ordered_dictionary = dict(OrderedDict(sorted(characters.items(), reverse=True, key=lambda t: t[1])))
    checksum_value = []
    for key, value in ordered_dictionary.items():
        checksum_value.append(key)
        if len(checksum_value) == 5:
            break

    assert len(checksum_value) == 5, 'checksum_value should be 5 characters in length'

    return ''.join(checksum_value)


def process_data(data):
    total = 0
    for string in data:
        input = parse_input(string)
        checksum = perform_checksum(input[0])
        if checksum == input[2]:
            assert input[1].isdigit(), 'sector id is not an integer'
            total += int(input[1])
    return total


def read_input_data(filename):
    with open(filename) as file:
        return file.read().splitlines()


class TestDay01(unittest.TestCase):
    def test_parse_input(self):
        result = parse_input('aaaaa-bbb-z-y-x-123[abxyz]')

        self.assertEqual('aaaaa-bbb-z-y-x', result[0])
        self.assertEqual('123', result[1])
        self.assertEqual('abxyz', result[2])

    def test_checksum_example_data(self):

        self.assertEqual('abxyz', perform_checksum('aaaaa-bbb-z-y-x'))
        self.assertEqual('abcde', perform_checksum('a-b-c-d-e-f-g-h'))
        self.assertEqual('oarel', perform_checksum('not-a-real-room'))

        self.assertEqual('abcde', perform_checksum('aabbccddeefg'))
        self.assertEqual('gabcd', perform_checksum('aabbccddeefggg'))
        self.assertEqual('abdef', perform_checksum('aabbcddeeffgg'))
        self.assertEqual('abdeg', perform_checksum('aabbcddeefgg'))
        self.assertEqual('abcde', perform_checksum('gfeeddccbbaa'))

    def test_day4_part1_example_data(self):
        input_data = ['aaaaa-bbb-z-y-x-123[abxyz]', 'a-b-c-d-e-f-g-h-987[abcde]', 'not-a-real-room-404[oarel]', 'totally-real-room-200[decoy]']
        sum = process_data(input_data)
        print('Part1 Example Data:', sum)
        self.assertEqual(1514, sum)

    def test_day4_part1_solution(self):
        data = read_input_data(r'resources/day4_input.txt')
        sum = process_data(data)
        print('Part1:', sum)
        self.assertEqual(409147, sum)


if __name__ == '__main__':
    unittest.main()


