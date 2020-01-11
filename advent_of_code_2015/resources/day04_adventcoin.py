"""
https://adventofcode.com/2015/day/4
"""


import hashlib
import unittest


def find_hash_starting_with_5zeros(input):
    for i in range(99999999):
        hash_input = input + str(i)
        res = calculate_hash(hash_input)
        if '00000' == res[:5]:
            return i
    return None


def calculate_hash(input):
    m = hashlib.md5()
    m.update(input.encode('utf-8'))
    return m.hexdigest()


class TestDay03(unittest.TestCase):

    def test_hash(self):
        self.assertEqual('00000', calculate_hash('abcdef609043')[:5])
        self.assertEqual('00000', calculate_hash('pqrstuv1048970')[:5])

    def test_find_lowest_number_to_produce_hash_starting_5zeros(self):
        result = find_hash_starting_with_5zeros('abcdef')
        print('Result:', result)
        self.assertEqual(609043, result)

        result = find_hash_starting_with_5zeros('pqrstuv')
        print('Result:', result)
        self.assertEqual(1048970, result)

    def test_part1(self):
        result = find_hash_starting_with_5zeros('ckczppom')
        print('Result:', result)
        self.assertEqual(117946, result)


if __name__ == '__main__':
    unittest.main()
