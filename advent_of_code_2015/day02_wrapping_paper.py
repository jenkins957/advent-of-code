"""
https://adventofcode.com/2015/day/2
"""


import unittest


def calculate_wrapping_required(h, w, l):
    return 2 * (l * w) + 2 * (w * h) + 2 * (h * l)


def calculate_extra_wrapping_required(h, w, l):
    a = l * w
    b = w * h
    c = h * l
    return min(a, min(b, c))


def calculate_total_wrapping_required(h, w, l):
    return calculate_wrapping_required(h, w, l) + calculate_extra_wrapping_required(h, w, l)


def calculate_ribbon_for_present_required(h, w, l):
    dimensions = [h, w, l]
    dimensions.sort()
    return dimensions[0] * 2 + dimensions[1] * 2


def calculate_ribbon_for_bow_required(h, w, l):
    return h * w * l


def calculate_total_ribbon_required(h, w, l):
    return calculate_ribbon_for_present_required(h, w, l) + calculate_ribbon_for_bow_required(h, w, l)


def read_input_data(filename):
    with open(filename) as file:
        return file.read().splitlines()


def calculate_total_wrapping(lines):
    total = 0
    for line in lines:
        h, w, l = line.split('x')
        total += calculate_total_wrapping_required(int(h), int(w), int(l))
    return total


def calculate_total_ribbon(lines):
    total = 0
    for line in lines:
        h, w, l = line.split('x')
        total += calculate_total_ribbon_required(int(h), int(w), int(l))
    return total


class TestDay02(unittest.TestCase):

    def test_wrapping_required(self):
        self.assertEqual(52, calculate_wrapping_required(2, 3, 4))
        self.assertEqual(42, calculate_wrapping_required(1, 1, 10))

    def test_extra_wrapping_required(self):
        self.assertEqual(6, calculate_extra_wrapping_required(2, 3, 4))
        self.assertEqual(1, calculate_extra_wrapping_required(1, 1, 10))

    def test_total_wrapping_required(self):
        self.assertEqual(58, calculate_total_wrapping_required(2, 3, 4))
        self.assertEqual(43, calculate_total_wrapping_required(1, 1, 10))

    def test_ribbon_required(self):
        self.assertEqual(10, calculate_ribbon_for_present_required(2, 3, 4))
        self.assertEqual(4, calculate_ribbon_for_present_required(1, 1, 10))

    def test_ribbon_for_bow_required(self):
        self.assertEqual(24, calculate_ribbon_for_bow_required(2, 3, 4))
        self.assertEqual(10, calculate_ribbon_for_bow_required(1, 1, 10))

    def test_total_ribbon_required(self):
        self.assertEqual(34, calculate_total_ribbon_required(2, 3, 4))
        self.assertEqual(14, calculate_total_ribbon_required(1, 1, 10))

    def test_part1(self):
        result = calculate_total_wrapping(read_input_data(r'resources/day2_input.txt'))
        print('Total Wrapping Required', result)
        self.assertEqual(1586300, result)

    def test_part2(self):
        result = calculate_total_ribbon(read_input_data(r'resources/day2_input.txt'))
        print('Total Ribbon Required', result)
        self.assertEqual(3737498, result)


if __name__ == '__main__':
    unittest.main()
