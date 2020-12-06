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
        for answers in group:
            for answer in answers:
                yes_answers.add(answer)

        count += len(yes_answers)

    return count


def count_questions_everyone_answered_yes(groups):
    count = 0

    for group in groups:
        yes_answers = {}

        # Count up all questions answered 'yes
        for answers in group:
            for answer in answers:
                if answer in yes_answers:
                    yes_answers[answer] += 1
                else:
                    yes_answers[answer] = 1

        # Sum up how many questions everyone in the group answered yes
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


class TestDay6CustomCustoms(unittest.TestCase):
    def test_part_1_simplified_solution(self):
        # Simplified solution counting answers as it reads the data from file.
        count = 0
        yes_answers = set()
        with open(r'resources/day6_input.txt') as file:
            for answers in file:
                answers = answers.strip('\n')
                if len(answers) < 1:
                    count += len(yes_answers)
                    yes_answers = set()

                for answer in answers:
                    yes_answers.add(answer)

            count += len(yes_answers)

        print('Part1:', count)
        self.assertEqual(6930, count)

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
