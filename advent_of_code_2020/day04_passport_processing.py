"""
https://adventofcode.com/2020/day/4

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""

import unittest
import re

input_file = r'resources/day4_input.txt'


class Passport:
    field_validators = {'byr': '19[2-9][0-9]|200[0-2]',
                        'iyr': '201[0-9]|2020',
                        'eyr': '202[0-9]|2030',
                        'hgt': '((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in)',
                        'hcl': '#[a-f0-9]{6}$',
                        'ecl': 'amb|blu|brn|gry|grn|hzl|oth',
                        'pid': '^[0-9]{9}$'}

    def __init__(self, passport):
        self.fields = {}

        for line in passport:
            pairs = line.split()
            for kv_pair in pairs:
                elements = kv_pair.split(':')
                self.fields[elements[0]] = elements[1]

    def contains_required_fields(self):
        return all(k in self.fields for k in Passport.field_validators)

    def validate_fields(self):
        for key, value in self.fields.items():
            if key in Passport.field_validators and re.search(Passport.field_validators[key], value) is None:
                return False

        return True


def parse_passport_data(data):
    passports = []
    passport = []

    for line in data:
        if len(line) < 1:
            passports.append(passport)
            passport = []
        passport.append(line)
    passports.append(passport)

    return passports


def validate_passports(data, part=1):
    passports = parse_passport_data(data)
    valid_passports = 0

    for passport in passports:
        if validate_passport(passport, part):
            valid_passports += 1

    return valid_passports


def validate_passport(passport, part):
    passport_fields = Passport(passport)

    result = passport_fields.contains_required_fields()

    if result and part == 2:
        result = passport_fields.validate_fields()

    return result


def read_input_data(filename):
    with open(filename) as file:
        data = [line.strip() for line in file.readlines()]

    return data


class TestDay4PassportProcessing(unittest.TestCase):
    def test_part_1(self):
        valid_passports = validate_passports(read_input_data(input_file))

        print('Part1:', valid_passports)
        self.assertEqual(170, valid_passports)

    def test_part_2(self):
        valid_passports = validate_passports(read_input_data(input_file), 2)

        print('Part2:', valid_passports)
        self.assertEqual(103, valid_passports)


if __name__ == '__main__':
    unittest.main()
