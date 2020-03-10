"""
https://adventofcode.com/2018/day/2

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""


import unittest


def contains_exactly_2_identical_letters(string):
    letters = {}

    for c in string:
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1

    for key, value in letters.items():
        if value == 2:
            return True

    return False


def contains_exactly_3_identical_letters(string):
    letters = {}

    for c in string:
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1

    for key, value in letters.items():
        if value == 3:
            return True

    return False


def read_input_data(filename):
    with open(filename) as file:
        return file.read().splitlines()


class TestDay02(unittest.TestCase):

    def test_contains_exactly_2_identical_letters(self):
        self.assertTrue(contains_exactly_2_identical_letters('aa'))
        self.assertTrue(contains_exactly_2_identical_letters('aba'))
        self.assertTrue(contains_exactly_2_identical_letters('bababc'))
        self.assertTrue(contains_exactly_2_identical_letters('aabcdd'))

    def test_contains_exactly_3_identical_letters(self):
        self.assertTrue(contains_exactly_3_identical_letters('aaa'))
        self.assertTrue(contains_exactly_3_identical_letters('abcaea'))
        self.assertTrue(contains_exactly_3_identical_letters('bababc'))
        self.assertTrue(contains_exactly_3_identical_letters('ababab'))


    def test_part1(self):
        count_2_letters = 0
        count_3_letters = 0

        for string in read_input_data(r'resources/day2_input.txt'):
            if contains_exactly_2_identical_letters(string):
                count_2_letters += 1
            if contains_exactly_3_identical_letters(string):
                count_3_letters += 1

        self.assertEqual(3952, count_2_letters * count_3_letters)


    # def test_part2(self):
    #     result = calculate_frequency_first_reached_twice(read_input_data(r'resources/day1_input.txt'))
    #     self.assertEqual(566, result)


if __name__ == '__main__':
    unittest.main()
