"""
https://adventofcode.com/2016/day/3

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""

import unittest


def calculate_number_of_valid_triangles(data, columns=False):
    """
    In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.
    :param data:
    :param columns: True if triangle data is read veritically in columns or False id read in rows
    :return: count of valid triangles
    """
    count = 0

    if columns:
        # Data is formatted in columns, 3 rows per column make up a triangle
        row_count = 0
        c0 = []
        c1 = []
        c2 = []

        for line in data:
            sides = line.split()

            c0.append(sides[0])
            c1.append(sides[1])
            c2.append(sides[2])
            row_count += 1

            if row_count > 0 and row_count % 3 == 0:
                if is_valid_triangles(int(c0[0]), int(c0[1]), int(c0[2])):
                    count += 1

                if is_valid_triangles(int(c1[0]), int(c1[1]), int(c1[2])):
                    count += 1

                if is_valid_triangles(int(c2[0]), int(c2[1]), int(c2[2])):
                    count += 1
                row_count = 0
                c0 = []
                c1 = []
                c2 = []
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
    def test_day3_part1_solution(self):
        data = read_input_data(r'resources/day3_input.txt')

        count = calculate_number_of_valid_triangles(data)
        print('Part1:', count)
        self.assertEqual(1032, count)

    def test_day3_part2_solution(self):
        data = read_input_data(r'resources/day3_input.txt')

        count = calculate_number_of_valid_triangles(data, True)
        print('Part2:', count)
        self.assertEqual(1838, count)


if __name__ == '__main__':
    unittest.main()


