"""
https://adventofcode.com/2020/day/2

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""

import unittest

input_file = r'resources/day2_input.txt'


class Policy:
    def __init__(self, policy_str):
        elements = policy_str.split()

        range = elements[0].split('-')
        self.int1 = int(range[0])
        self.int2 = int(range[1])
        self.char = elements[1].replace(":", "")
        self.password = elements[2]


def validate_passwords_policy1(data):
    valid_passwords = 0

    for line in data:
        policy = Policy(line)

        count = 0

        for c in policy.password:
            if c == policy.char:
                count += 1

        if policy.int1 <= count <= policy.int2:
            valid_passwords += 1

    return valid_passwords


def validate_passwords_policy2(data):
    valid_passwords = 0

    for line in data:
        policy = Policy(line)

        c1 = policy.char == policy.password[policy.int1 - 1]
        c2 = policy.char == policy.password[policy.int2 - 1]

        if c1 != c2:
            valid_passwords += 1

    return valid_passwords


def read_input_data(filename):
    data = []

    with open(filename) as file:
        for line in file:
            data.append(line.strip('\n'))
    return data


class TestPasswordPhilosophy(unittest.TestCase):
    def test_validate_passwords_policy1(self):
        data = ["1-3 a: abcde"]

        result = validate_passwords_policy1(data)
        self.assertEqual(1, result)

    def test_validate_passwords_policy1_part1(self):
        data = read_input_data(input_file)

        result = validate_passwords_policy1(data)
        print('Part1:', result)

        self.assertEqual(564, result)

    def test_validate_passwords_policy2(self):
        data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

        result = validate_passwords_policy2(data)
        self.assertEqual(1, result)

    def test_validate_passwords_policy1_part2(self):
        data = read_input_data(input_file)

        result = validate_passwords_policy2(data)
        print('Part2:', result)

        self.assertEqual(325, result)


if __name__ == '__main__':
    unittest.main()
