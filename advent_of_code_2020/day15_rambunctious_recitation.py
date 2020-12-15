"""
https://adventofcode.com/2020/day/15

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""

import unittest


def part1(data, turns):
    numbers = []

    elements = data.split(',')

    for e in elements:
        numbers.append(int(e))

    return play_number_game(numbers, turns)


def play_number_game(starting_numbers, turns):
    prev_num = -1
    number_spoken = -1

    spoken = {}

    for turn in range(1, turns + 1):

        if turn <= len(starting_numbers):
            number_spoken = starting_numbers[turn - 1]
        elif prev_num in spoken and len(spoken[prev_num]) == 1:
            number_spoken = 0
        elif prev_num in spoken:
            number_spoken = spoken[prev_num][-1] - spoken[prev_num][-2]

        # record the turn (position) number was spoken - add to list
        if number_spoken in spoken:
            spoken[number_spoken].append(turn)
        else:
            spoken[number_spoken] = [turn]

        prev_num = number_spoken

    return number_spoken


class TestDay15RambunctiousRecitation(unittest.TestCase):
    def test_play_game_turn_1(self):
        result = part1('0, 3, 6', 1)
        self.assertEqual(0, result)

    def test_play_game_turn_2(self):
        result = part1('0, 3, 6', 2)
        self.assertEqual(3, result)

    def test_play_game_turn_3(self):
        result = part1('0, 3, 6', 3)
        self.assertEqual(6, result)

    def test_play_game_turn_4(self):
        result = part1('0, 3, 6', 4)
        self.assertEqual(0, result)

    def test_play_game_turn_5(self):
        result = part1('0, 3, 6', 5)
        self.assertEqual(3, result)

    def test_play_game_turn_6(self):
        result = part1('0, 3, 6', 6)
        self.assertEqual(3, result)

    def test_play_game_turn_7(self):
        result = part1('0, 3, 6', 7)
        self.assertEqual(1, result)

    def test_play_game_turn_8(self):
        result = part1('0, 3, 6', 8)
        self.assertEqual(0, result)

    def test_play_game_turn_9(self):
        result = part1('0, 3, 6', 9)
        self.assertEqual(4, result)

    def test_play_game_turn_10(self):
        result = part1('0, 3, 6', 10)
        self.assertEqual(0, result)

    def test_part_1_test_data(self):
        result = part1('0, 3, 6', 2020)
        self.assertEqual(436, result)

    def test_part_1(self):
        result = part1('1, 17, 0, 10, 18, 11, 6', 2020)
        print('Part1:', result)
        self.assertEqual(595, result)

    def test_part_2(self):
        result = part1('1, 17, 0, 10, 18, 11, 6', 30000000)
        print('Part2:', result)
        self.assertEqual(1708310, result)


if __name__ == '__main__':
    unittest.main()
