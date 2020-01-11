"""
https://adventofcode.com/2015/day/4
"""


import hashlib
import unittest


def find_hash_starting_with_matching_prexfix(input, prefix='00000'):
    for i in range(99999999):
        hash_input = input + str(i)
        res = calculate_hash(hash_input)
        if prefix == res[:len(prefix)]:
            return i
    return None


def calculate_hash(input):
    m = hashlib.md5()
    m.update(input.encode('utf-8'))
    return m.hexdigest()


class TestDay04(unittest.TestCase):

    def test_hash(self):
        self.assertEqual('00000', calculate_hash('abcdef609043')[:5])
        self.assertEqual('00000', calculate_hash('pqrstuv1048970')[:5])

    def test_find_lowest_number_to_produce_hash_starting_5zeros(self):
        result = find_hash_starting_with_matching_prexfix('abcdef')
        print('Result:', result)
        self.assertEqual(609043, result)

        result = find_hash_starting_with_matching_prexfix('pqrstuv')
        print('Result:', result)
        self.assertEqual(1048970, result)

    def test_part1(self):
        result = find_hash_starting_with_matching_prexfix('ckczppom')
        print('Part 1:', result)
        self.assertEqual(117946, result)

    def test_part2(self):
        result = find_hash_starting_with_matching_prexfix('ckczppom', '000000')
        print('Part 2:', result)
        self.assertEqual(3938038, result)


if __name__ == '__main__':
    unittest.main()
