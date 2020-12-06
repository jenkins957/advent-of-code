"""
https://adventofcode.com/2020/day/6

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""

import unittest

input_file = r'resources/day6_input.txt'


def count_questions_answered_yes(groups):
    count = 0

    for group in groups:
        # Keep track of all unique questions per group
        yes_answers = set()
        for line in group:
            for c in line:
                yes_answers.add(c)
                
        count += len(yes_answers)

    return count


def count_questions_everyone_answered_yes(groups):
    count = 0

    for group in groups:
        yes_answers = {}

        # Count up all questions answered 'yes
        for line in group:
            for c in line:
                if c in yes_answers:
                    yes_answers[c] += 1
                else:
                    yes_answers[c] = 1

        # Sum up ho wmany questions everyone in the group answered yes
        for value in yes_answers.values():
            if value == len(group):
                count += 1

    return count


def parse_input_data(filename):
    groups = []
    group = []

    with open(filename) as file:
        for line in file:
            line = line.strip('\n')
            if len(line) > 0:
                group.append(line)
            else:
                groups.append(group)
                group = []

        groups.append(group)

    return groups


class TestDay6(unittest.TestCase):
    def test_part_1(self):
        result = count_questions_answered_yes(parse_input_data(input_file))

        print('Part1:', result)
        self.assertEqual(6930, result)

    def test_part_2(self):
        result = count_questions_everyone_answered_yes(parse_input_data(input_file))

        print('Part2:', result)
        self.assertEqual(3585, result)


if __name__ == '__main__':
    unittest.main()
