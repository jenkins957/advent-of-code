"""
https://adventofcode.com/2020/day/4

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""

import unittest
import re

input_file = r'resources/day4_input.txt'


class Passport:
    mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    def __init__(self, passport):
        self.fields = {}

        for line in passport:
            pairs = line.split()
            for kv_pair in pairs:
                elements = kv_pair.split(':')
                self.fields[elements[0]] = elements[1]

    def contains_all_fields(self):
        return all(k in self.fields for k in Passport.mandatory_fields)

    @staticmethod
    def __is_valid_int_field(value, min_val, max_val):
        return min_val <= value <= max_val

    @staticmethod
    def __is_valid_string_field(value, regex):
        return re.search(regex, value) is not None

    @staticmethod
    def __is_valid_height_field(value):
        if 'cm' in value:
            if 150 <= int(value[:-2]) <= 193:
                return True
        elif 'in' in value:
            if 59 <= int(value[:-2]) <= 76:
                return True

        return False

    def validate_passport_fields(self):
        return self.__is_valid_int_field(int(self.fields['byr']), 1920, 2002) and \
               self.__is_valid_int_field(int(self.fields['iyr']), 2010, 2020) and \
               self.__is_valid_int_field(int(self.fields['eyr']), 2020, 2030) and \
               self.__is_valid_height_field(self.fields['hgt']) and \
               self.__is_valid_string_field(self.fields['hcl'], '#[a-f0-9]{6}$') and \
               self.__is_valid_string_field(self.fields['ecl'], '^(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)') and \
               self.__is_valid_string_field(self.fields['pid'], '^[0-9]{9}$')


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

    result = passport_fields.contains_all_fields()

    if result and part == 2:
        result = passport_fields.validate_passport_fields()

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
