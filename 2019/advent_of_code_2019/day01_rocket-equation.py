"""
https://adventofcode.com/2019/day/1
"""


import math
import unittest


input_file = r'resources/day1_input.txt'


def calc_required_fuel(mass, include_fuel_in_calc=False):
    mass = int(math.floor((mass / 3)) - 2)

    if include_fuel_in_calc:
        if mass > 0:
            mass += calc_required_fuel(mass, include_fuel_in_calc)
        else:
            return 0
    
    return mass


def read_input_data(filename):
    with open(filename) as file: 
        return file.readlines()


class TestRocketEquation(unittest.TestCase):
    def test_part1(self):
        total = 0
        for line in read_input_data(input_file):
            line = line.strip()
            total += calc_required_fuel(int(line))

        print('Part1:', total)
        self.assertEqual(3262356, total)

    def test_part2(self):
        total = 0
        for line in read_input_data(input_file):
            line = line.strip()
            total += calc_required_fuel(int(line), True)

        print('Part2:', total)
        self.assertEqual(4890664, total)


if __name__ == '__main__':
    unittest.main()
