"""
https://adventofcode.com/2020/day/22

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""

import unittest

input_file = r'resources/day22_input.txt'


def part1(data):
    total = 0

    player1Deck = []
    player2Deck = []

    p1 = True

    for line in data:
        if len(line) == 0 or 'Player 1:' in line:
            continue

        if 'Player 2:' in line:
            p1 = False
            continue

        if p1:
            player1Deck.append(line)
        else:
            player2Deck.append(line)

    winning_stack = __play(player1Deck, player2Deck)

    index = len(winning_stack)
    while len(winning_stack) > 0:
        total += int(winning_stack.pop(0)) * index
        index -= 1

    return total


def __play(player1Deck, player2Deck):
    while len(player1Deck) > 0 and len(player2Deck) > 0:
        p1 = int(player1Deck.pop(0))
        p2 = int(player2Deck.pop(0))

        if p1 > p2:
            player1Deck.append(p1)
            player1Deck.append(p2)
        else:
            player2Deck.append(p2)
            player2Deck.append(p1)

    return  player1Deck if len(player1Deck) > 0 else player2Deck


def read_input_data(filename):
    with open(filename) as file:
        data = [line.strip() for line in file.readlines()]

    return data


class TestDay22(unittest.TestCase):
    def test_part_1_test_data(self):
        data = []
        data.append('Player 1:')
        data.append('9')
        data.append('2')
        data.append('6')
        data.append('3')
        data.append('1')
        data.append('')
        data.append('Player 2:')
        data.append('5')
        data.append('8')
        data.append('4')
        data.append('7')
        data.append('10')

        result = part1(data)
        self.assertEqual(306, result)

    def test_part_1(self):
        data = read_input_data(input_file)

        result = part1(data)
        self.assertEqual(31781, result)


if __name__ == '__main__':
    unittest.main()
