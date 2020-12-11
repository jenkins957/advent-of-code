"""
https://adventofcode.com/2020/day/10

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
Reference: https://www.youtube.com/watch?v=eeYanhLamjg
"""

import unittest

input_file = r'resources/day10_input.txt'


def part1(data):
    # start at zero
    data.append(0)
    data.sort()

    total_diff = 0

    one_jolt_diff = 0
    three_jolt_diff = 0

    j = 1
    for i, num in enumerate(data):
        if j > len(data) - 1:
            break

        next_num = data[j]
        diff = next_num - num
        if diff <= 3:
            if diff == 1:
                one_jolt_diff += 1
            elif diff == 3:
                three_jolt_diff += 1

            total_diff += diff
        j += 1

    total_diff += 3
    three_jolt_diff += 1

    return one_jolt_diff * three_jolt_diff, total_diff


def part2(data):
    data.append(0)
    data.append(max(data) + 3)
    data.sort()

    paths = [0] * (max(data) + 1)
    paths[0] = 1

    for i in range(1, max(data) + 1):
        for x in range(1, 4):
            if i - x in data:
                paths[i] += paths[i - x]

    return paths[-1]


def read_integer_input_data(filename):
    numbers = []

    with open(filename) as file:
        for line in file:
            numbers.append(int(line.strip('\n')))
    return numbers


class TestDay10AdapterArray(unittest.TestCase):
    def test_part_1_0(self):
        data = [3, 9, 6]
        result = part1(data)

        self.assertEqual(0, result[0])
        self.assertEqual(12, result[1])

    def test_part_1_1(self):
        data = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]

        result = part1(data)

        self.assertEqual(35, result[0])

    def test_part_1_2(self):
        data = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19,
                38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
        result = part1(data)

        self.assertEqual(220, result[0])

    def test_part_1(self):
        result = part1(read_integer_input_data(input_file))

        print('Part1:', result)
        self.assertEqual(2346, result[0])

    def test_part_2_1(self):
        data = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        result = part2(data)

        print('Part2:', result)
        self.assertEqual(8, result)

    def test_part_2_2(self):
        result = part2(read_integer_input_data(input_file))

        print('Part2:', result)
        self.assertEqual(6044831973376, result)


if __name__ == '__main__':
    unittest.main()
