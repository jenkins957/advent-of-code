"""
https://adventofcode.com/2016/day/3

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""

import unittest


def calculate_number_of_valid_triangles(data, columns=False):
    """
    In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.
    :param data:
    :return: count of valid triangles
    """
    count = 0

    if columns:
        # Data is formatted in columns, 3 rows per column make up a triangle
        for line in data:
            sides = line.split()
            if is_valid_triangles(int(sides[0]), int(sides[1]), int(sides[2])):
                count += 1
    else:
        # Data is formatted in rows
        for line in data:
            sides = line.split()

            if is_valid_triangles(int(sides[0]), int(sides[1]), int(sides[2])):
                count += 1

    return count


def is_valid_triangles(side1, side2, side3):
    """
    In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.
    :param data: The 3 sides
    :return: True is valid triangles
    """
    return side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1


def read_input_data(filename):
    with open(filename) as file:
        return file.read().splitlines()


class TestDay01(unittest.TestCase):
    def test_day2_part1_solution(self):
        data = read_input_data(r'resources/day3_input.txt')

        count = calculate_number_of_valid_triangles(data)
        print(count)
        self.assertEqual(1032, count)

    # def test_day2_part2_solution(self):
    #     data = read_input_data(r'resources/day3_input.txt')
    #
    #     count = calculate_number_of_valid_triangles(data, True)
    #     print(count)
    #     self.assertEqual(-1, count)

if __name__ == '__main__':
    unittest.main()


