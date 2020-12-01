"""
https://adventofcode.com/2020/day/1

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""

import unittest

input_file = r'resources/day1_input.txt'


def get_product_of_2_entries_that_add_to_target(expense_report, target=2020):
    """
    Find the product of 2 numbers in the list that add up to 2020
    :param expense_report: list of numbers
    :return: product of the 2 numbers
    """

    # TODO : Edge case whereby same number could be used in both loops i.e if first element was 1010
    for num1 in expense_report:
        for num2 in expense_report:
            if num1 + num2 == target:
                print("Result", num1, num2, num1 * num2)
                return num1 * num2
    return -1


def get_product_of_3_entries_that_add_to_target(expense_report, target=2020):
    """
    Find the product of 3 numbers in the list that add up to 2020
    :param expense_report: list of numbers
    :return: product of the 3 numbers
    """
    for num1 in expense_report:
        for num2 in expense_report:
            for num3 in expense_report:
                if num1 + num2 + num3 == target:
                    print("Result", num1, num2, num3, (num1 * num2 * num3))
                    return num1 * num2 * num3

    return -1


def read_integer_input_data(filename):
    numbers = []

    with open(filename) as file:
        for line in file:
            numbers.append(int(line.strip('\n')))
    return numbers


class TestDayOne(unittest.TestCase):
    def test_day1_part1(self):
        numbers = [1721, 979, 366, 299, 675, 1456]
        sum = get_product_of_2_entries_that_add_to_target(numbers)
        self.assertEqual(514579, sum)

    def test_day1_part1_answer(self):
        numbers = read_integer_input_data(input_file)
        sum = get_product_of_2_entries_that_add_to_target(numbers)
        print('Part1:', sum)
        self.assertEqual(982464, sum)

    def test_day1_part2(self):
        numbers = [1721, 979, 366, 299, 675, 1456]
        sum = get_product_of_3_entries_that_add_to_target(numbers)
        self.assertEqual(241861950, sum)

    def test_day1_part2_answer(self):
        numbers = read_integer_input_data(input_file)
        sum = get_product_of_3_entries_that_add_to_target(numbers)
        print('Part2:', sum)
        self.assertEqual(162292410, sum)


if __name__ == '__main__':
    unittest.main()
