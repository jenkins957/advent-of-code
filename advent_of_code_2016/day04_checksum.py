import unittest
from collections import OrderedDict
import re
"""
https://adventofcode.com/2016/day/4

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""


def decrypt_room_name(text, sector_id):
    plain_text = ''

    for c in text:
        if c == '-':
            plain_text += ' '
        else:
            plain_text += chr(get_ascii_value(c, sector_id))
    return plain_text


def get_ascii_value(c, rotations):

    ascii_value = ord(c)

    for i in range(rotations):
        ascii_value += 1
        if ascii_value > 122:
            ascii_value = 97
    return ascii_value


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
    rooms = []
    for string in data:
        input = parse_input(string)
        checksum = perform_checksum(input[0])
        if checksum == input[2]:
            assert input[1].isdigit(), 'sector id is not an integer'
            total += int(input[1])
            rooms.append(decrypt_room_name(input[0], int(input[1])) + ',' + input[1])
    return total, rooms


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

    def test_decrypt_room_name(self):
        self.assertEqual('bcd', decrypt_room_name('abc', 1))
        self.assertEqual('cde', decrypt_room_name('abc', 2))
        self.assertEqual('abc', decrypt_room_name('abc', 26))

        self.assertEqual('very encrypted name', decrypt_room_name('qzmt-zixmtkozy-ivhz', 343))

    def test_day4_part1_example_data(self):
        input_data = ['aaaaa-bbb-z-y-x-123[abxyz]', 'a-b-c-d-e-f-g-h-987[abcde]', 'not-a-real-room-404[oarel]', 'totally-real-room-200[decoy]']
        result = process_data(input_data)
        print('Part1 Example Data:', result[0])
        self.assertEqual(1514, result[0])

    def test_day4_part1_solution(self):
        data = read_input_data(r'resources/day4_input.txt')
        result = process_data(data)
        print('Part1:', result[0])
        self.assertEqual(409147, result[0])

    def test_day4_part2_solution(self):
        data = read_input_data(r'resources/day4_input.txt')
        result = process_data(data)

        name = ''
        sector_id = '991'
        for r in result[1]:
            if 'northpole object storage' in r:
                elements = r.split(',')
                name = elements[0]
                sector_id = elements[1]

        print('Part2:', name, sector_id)
        self.assertEqual('northpole object storage', name)
        self.assertEqual('991', sector_id)


if __name__ == '__main__':
    unittest.main()


