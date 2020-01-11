"""
https://adventofcode.com/2015/day/5
"""

import unittest


def is_nice(string):
    invalid_characters = ['ab', 'cd', 'pq', 'xy']
    return contains_vowels(string) and contains_double_character(string) and does_not_contain_string(invalid_characters, string)


def is_nice_version2(string):
    return contains_pair_double_character(string) and char_repeats_with_one_char_inbetween(string)


def contains_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']

    no_of_vowels = 0
    for c in string:
        if c in vowels:
            no_of_vowels += 1

    if no_of_vowels >= 3:
        return True

    return False


def contains_double_character(string):
    previous_char = ''

    for c in string:
        if c == previous_char:
            return True
        previous_char = c

    return False


def does_not_contain_string(criteria, string):
    for chars in criteria:
        if chars in string:
            return False
    return True


def contains_pair_double_character(string):

    index = 0
    while index < len(string) - 1:
        pair = string[index] + string[index + 1]
        if pair in string[index + 2:]:
            return True
        index += 1
    return False


def char_repeats_with_one_char_inbetween(string):
    index = 0
    while index < len(string) - 2:
        first_char = string[index]
        third_char = string[index + 2]

        if first_char == third_char:
            return True
        index += 1

    return False


def read_input_data(filename):
    with open(filename) as file:
        return file.read().splitlines()


class TestDay05(unittest.TestCase):

    def test_contains_3_or_more_vowels(self):
        self.assertTrue(contains_vowels('aei'))
        self.assertTrue(contains_vowels('iou'))
        self.assertTrue(contains_vowels('aeiou'))
        self.assertTrue(contains_vowels('xazegov'))
        self.assertTrue(contains_vowels('aeiouaeiouaeiou'))

    def test_contains_double_character(self):
        self.assertTrue(contains_double_character('aaei'))
        self.assertTrue(contains_double_character('ioxxu'))
        self.assertTrue(contains_double_character('aeiiou'))
        self.assertTrue(contains_double_character('xazzegov'))
        self.assertTrue(contains_double_character('xx'))
        self.assertTrue(contains_double_character('abcdd'))
        self.assertTrue(contains_double_character('abccd'))

    def test_contains_pair_of_double_character(self):
        self.assertTrue(contains_pair_double_character('xyxy'))
        self.assertTrue(contains_pair_double_character('aabcdefgaa'))
        self.assertTrue(contains_pair_double_character('abcdeelkjhgeekj'))

        self.assertFalse(contains_pair_double_character('aaa'))
        self.assertFalse(contains_pair_double_character('aba'))
        self.assertFalse(contains_pair_double_character('abccba'))

    def test_char_repeats_with_one_char_between(self):
        self.assertTrue(char_repeats_with_one_char_inbetween('xyx'))
        self.assertTrue(char_repeats_with_one_char_inbetween('abcdefeghi'))
        self.assertTrue(char_repeats_with_one_char_inbetween('aaa'))

        self.assertFalse(char_repeats_with_one_char_inbetween('abc'))
        self.assertFalse(char_repeats_with_one_char_inbetween('abbc'))
        self.assertFalse(char_repeats_with_one_char_inbetween('abcdee'))

    def test_does_not_contain_chars(self):
        invalid_characters = ['ab', 'cd', 'pq', 'xy']

        self.assertFalse(does_not_contain_string(invalid_characters, 'abeiouaeiouaeiou'))
        self.assertTrue(does_not_contain_string(invalid_characters, 'aeiouaeiouaeiou'))

    def test_is_nice(self):
        self.assertTrue(is_nice('ugknbfddgicrmopn'))
        self.assertTrue(is_nice('aaa'))

    def test_is_naughty(self):
        self.assertFalse(is_nice('jchzalrnumimnmhp'))
        self.assertFalse(is_nice('haegwjzuvuyypxyu'))
        self.assertFalse(is_nice('dvszwmarrgswjxmb'))

    def test_is_nice_version2(self):
        self.assertTrue(is_nice_version2('qjhvhtzxzqqjkmpb'))
        self.assertTrue(is_nice_version2('xxyxx'))

    def test_is_naughty_version2(self):
        self.assertFalse(is_nice('uurcxstgmygtbstg'))
        self.assertFalse(is_nice('ieodomkazucvgmuy'))

    def test_part1(self):
        data = read_input_data(r'resources/day5_input.txt')
        names_on_nice_list = 0
        for name in data:
            if is_nice(name):
                names_on_nice_list += 1

        print('Part1, Number on nice list:', names_on_nice_list)
        self.assertEqual(236, names_on_nice_list)

    def test_part2(self):
        data = read_input_data(r'resources/day5_input.txt')
        names_on_nice_list = 0
        for name in data:
            if is_nice_version2(name):
                names_on_nice_list += 1

        print('Part 2, Number on nice list:', names_on_nice_list)
        self.assertEqual(51, names_on_nice_list)


if __name__ == '__main__':
    unittest.main()
