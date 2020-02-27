"""
https://adventofcode.com/2016/day/6

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""


import unittest
import re


def supports_tls(text, palindrome_len):
    #test no abba in []
    for abba in get_text_in_brackets(text):
        if contains_palindrome(abba, palindrome_len):
            return False

    if contains_palindrome(text, palindrome_len):
        return True
    return False


def contains_palindrome(text, palindrome_lenth):
    offset = 0

    while offset < len(text):
        s = text[offset:palindrome_lenth + offset]
        if len(s) >= palindrome_lenth and is_palindrome(s):
            return True
        offset += 1

    return False


def get_text_in_brackets(text):
    return re.findall('\[.*?\]', text)


def is_abba(text):
    if len(text) != 4:
        return False

    chars = set()
    for c in text:
        chars.add(c)

    if len(chars) == 2 and text == text[::-1]:
        return True

    return False


def is_palindrome(string):

    if len(string) != 4:
        return False

    chars = set()
    for c in string:
        chars.add(c)

    if len(chars) == 1:
        return False

    if string == string[::-1]:
            return True
    return False


def read_input_data(filename):
    with open(filename) as file:
        return file.read().splitlines()


class TestDay07(unittest.TestCase):

    def test_is_valid_abba(self):
        self.assertTrue(is_abba('abba'))
        self.assertTrue(is_abba('xyyx'))
        self.assertTrue(is_abba('qwwq'))

    def test_is_not_valid_abba(self):
        self.assertFalse(is_abba('aaaa'))
        self.assertFalse(is_abba('xyyy'))
        self.assertFalse(is_abba(''))
        self.assertFalse(is_abba('aaa'))
        self.assertFalse(is_abba('aaabbaaa'))

    def test_supports_tls(self):
        self.assertTrue(supports_tls('abba[mnop]qrst', 4))
        self.assertTrue(supports_tls('ioxxoj[asdfgh]zxcvbn', 4))

    def test_does_not_support_tls(self):
        self.assertFalse(supports_tls('abcd[bddb]xyyx', 4))
        self.assertFalse(supports_tls('aaaa[qwer]tyui', 4))

    def test_part1(self):
        data = read_input_data(r'resources/day7_input.txt')
        count = 0
        for text in data:
            if supports_tls(text, 4):
                count += 1
        print(count)


if __name__ == '__main__':
    unittest.main()
