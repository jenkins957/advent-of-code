"""
https://adventofcode.com/2015/day/4

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""


import hashlib
import unittest


def find_hash_starting_with_matching_prexfix(input, offset, prefix='00000'):
    for i in range(offset, 99999999):
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

    # def test_find_lowest_number_to_produce_hash_starting_5zeros(self):
    #     result = find_hash_starting_with_matching_prexfix('abcdef')
    #     print('Result:', result)
    #     self.assertEqual(609043, result)
    #
    #     result = find_hash_starting_with_matching_prexfix('pqrstuv')
    #     print('Result:', result)
    #     self.assertEqual(1048970, result)
    #
    def test_6th_char_at_hash(self):
        result = find_hash_starting_with_matching_prexfix('abc', 3231929)

        print(result)
        self.assertEqual(1, int(result[0][5:6]))

    def test_part1(self):
        passcode = []

        offset = 0
        for _ in range(8):
            result = find_hash_starting_with_matching_prexfix('ojvtpuvg', offset)
            passcode.append(result[0][5:6])
            offset = int(result[1]) + 1

        print('Part 1:', passcode)
        self.assertEqual('4543c154', ''.join(passcode))

    # def test_part2(self):
    #     result = find_hash_starting_with_matching_prexfix('ckczppom', '000000')
    #     print('Part 2:', result)
    #     self.assertEqual(3938038, result)


if __name__ == '__main__':
    unittest.main()
