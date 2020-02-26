"""
https://adventofcode.com/2015/day/4

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""


import hashlib
import unittest


def calculate_passcode(input):
    passcode = []

    offset = 0
    for _ in range(8):
        result = find_hash_starting_with_matching_prexfix(input, offset)
        passcode.append(result[0][5:6])
        offset = int(result[1]) + 1

    return passcode


def calculate_passcode_part2(input):
    passcode = ['-1', '-1', '-1', '-1', '-1', '-1', '-1', '-1']

    offset = 0
    digits_found = 0
    while digits_found < 8:
        result = find_hash_starting_with_matching_prexfix(input, offset)

        position = result[0][5:6]
        if position.isdigit():
            digit = (result[0][6:7])
            index = int(position)
            if index >= 0 and index < 8 and passcode[index] == '-1':
                passcode[index] = digit
                digits_found += 1

        offset = int(result[1]) + 1

    return passcode


def find_hash_starting_with_matching_prexfix(input, offset, prefix='00000'):
    for i in range(offset, 999999999):
        hash_input = input + str(i)
        res = calculate_hash(hash_input)
        if prefix == res[:len(prefix)]:
            return res, i
    return None


def calculate_hash(input):
    m = hashlib.md5()
    m.update(input.encode('utf-8'))
    return m.hexdigest()


class TestDay05(unittest.TestCase):

    def test_hash(self):
        self.assertEqual('00000', calculate_hash('abcdef609043')[:5])
        self.assertEqual('00000', calculate_hash('pqrstuv1048970')[:5])
        self.assertEqual('00000', calculate_hash('abc3231929')[:5])

    def test_6th_char_at_hash(self):
        result = find_hash_starting_with_matching_prexfix('abc', 3231929)
        self.assertEqual(1, int(result[0][5:6]))

    def test_position_char_at_hash(self):
        result = find_hash_starting_with_matching_prexfix('abc', 3231929)
        self.assertEqual(1, int(result[0][5:6]))
        self.assertEqual(5, int(result[0][6:7]))

    def test_part1(self):
        passcode = calculate_passcode('ojvtpuvg')

        print('Part 1:', ''.join(passcode))
        self.assertEqual('4543c154', ''.join(passcode))

    def test_part2(self):
        passcode = calculate_passcode_part2('ojvtpuvg')

        print('Part 2:', ''.join(passcode))
        self.assertEqual('1050cbbd', ''.join(passcode))


if __name__ == '__main__':
    unittest.main()
