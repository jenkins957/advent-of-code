"""
https://adventofcode.com/2016/day/2

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""

import unittest


def calculate_key_code(keypad, start_position, data):
    x = start_position[0]
    y = start_position[1]

    code = []
    for line in data:
        for c in line:
            if c == 'U' and y > 0 and read_value(keypad, x, y - 1) != ' ':
                y -= 1
            elif c == 'D' and y < len(keypad) - 1 and read_value(keypad, x, y + 1) != ' ':
                y += 1
            elif c == 'R' and x < len(keypad[y]) - 1 and read_value(keypad, x + 1, y) != ' ':
                x += 1
            elif c == 'L' and x > 0 and read_value(keypad, x - 1, y) != ' ':
                x -= 1

        code.append(read_value(keypad, x, y))
    return code


def read_value(keypad, x, y):
    return keypad[y][x]


def create_key_pad():
    row1 = ['1', '2', '3']
    row2 = ['4', '5', '6']
    row3 = ['7', '8', '9']
    return [row1, row2, row3]


def create_key_pad_part2():
    row1 = [' ', ' ', '1', ' ', ' ']
    row2 = [' ', '2', '3', '4', ' ']
    row3 = ['5', '6', '7', '8', '9']
    row4 = [' ', 'A', 'B', 'C', ' ']
    row5 = [' ', ' ', 'D', ' ', ' ']

    return [row1, row2, row3, row4, row5]


def read_input_data(filename):
    with open(filename) as file:
        return file.read().splitlines()


class TestDay01(unittest.TestCase):

    def test_example_pin_code_part1(self):
        keypad = create_key_pad()

        code = calculate_key_code(keypad, (1,1), ['ULL', 'RRDDD', 'LURDL', 'UUUUD'])
        print(code)
        self.assertEqual(['1', '9', '8', '5'], code)

    def test_example_pin_code_part2(self):
        keypad = create_key_pad_part2()

        code = calculate_key_code(keypad, (0,2), ['ULL', 'RRDDD', 'LURDL', 'UUUUD'])
        print(code)
        self.assertEqual(['5', 'D', 'B', '3'], code)

    def test_day2_part1_solution(self):
        keypad = create_key_pad()
        data = read_input_data(r'resources/day2_input.txt')

        code = calculate_key_code(keypad, (1,1), data)
        print(code)
        self.assertEqual(['7', '8', '9', '8', '5'], code)

    def test_day2_part2_solution(self):
        keypad = create_key_pad_part2()
        data = read_input_data(r'resources/day2_input.txt')

        code = calculate_key_code(keypad, (0,2), data)
        print(code)
        self.assertEqual(['5', '7', 'D', 'D', '8'], code)


if __name__ == '__main__':
    unittest.main()


