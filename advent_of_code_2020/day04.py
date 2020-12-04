"""
https://adventofcode.com/2020/day/4

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""

import unittest
import re

input_file = r'resources/day4_input.txt'


# TODO : A lot of refactoring! Getting the right result backed with unit tests, so time to refactor.
class PassportFields:
    def __init__(self, passport):

        self.byr = 0
        self.iyr = 0
        self.eyr = 0
        self.hgt = 0
        self.hcl = 0
        self.ecl = 0
        self.pid = 0
        self.cid = 0

        self.fields = {}
        for entry in passport:
            e = entry.split()
            for e1 in e:
                f = e1.split(':')
                self.fields[f[0]] = f[1]

    def contains_all_fields(self):
        return 'byr' in self.fields and 'iyr' in self.fields and 'eyr' in self.fields and 'hgt' in self.fields and 'hcl' in self.fields and 'ecl' in self.fields and 'pid' in self.fields

    def validate_data(self):
        byr = int(self.fields['byr'])
        if byr < 1920 or byr > 2002:
            return False

        iyr = int(self.fields['iyr'])
        if iyr < 2010 or iyr > 2020:
            return False

        eyr = int(self.fields['eyr'])
        if eyr < 2020 or eyr > 2030:
            return False

        hgt = self.fields['hgt']
        if 'cm' in hgt:
            cm = int(hgt[:-2])
            if cm < 150 or cm > 193:
                return False
        elif 'in' in hgt:
            inch = int(hgt[:-2])
            if inch < 59 or inch > 76:
                return False
        else:
            return False

        hcl = self.fields['hcl']
        if re.search('#[a-f0-9]{6}$', hcl) is None:
            return False

        ecl = self.fields['ecl']
        if re.search('^(amb$)|(blu$)|(brn$)|(gry$)|(grn$)|(hzl$)|(oth$)', ecl) is None:
            return False

        pid = self.fields['pid']
        if re.search('^[0-9]{9}$', pid) is None:
            return False

        return True


def validate_passports(data, part=1):

    passports = []
    passport = []

    for line in data:
        if len(line) < 2:
            passports.append(passport)
            passport = []
        passport.append(line)
    passports.append(passport)

    valid_passports = 0

    for passport in passports:
        if validate_passport(passport, part):
            valid_passports += 1

    return valid_passports


def validate_passport(passport, part):
    passport_fields = PassportFields(passport)

    result = passport_fields.contains_all_fields()

    if part == 1:
        return result

    if result:
        return passport_fields.validate_data()

    return False


def read_input_data(filename):
    data = []

    with open(filename) as file:
        for line in file:
            data.append(line.strip('\n'))
    return data


class TestDay4ValidatePassports(unittest.TestCase):
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
