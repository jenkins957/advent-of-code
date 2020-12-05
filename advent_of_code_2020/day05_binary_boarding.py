"""
https://adventofcode.com/2020/day/5

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""

import unittest

input_file = r'resources/day5_input.txt'


def find_highest_seat_number(boarding_passes):
    highest_seat_no = 0

    for boarding_pass in boarding_passes:
        highest_seat_no = max(decode_seat_id(boarding_pass), highest_seat_no)

    return highest_seat_no


def find_missing_seat(boarding_passes):
    seats = []
    for boarding_pass in boarding_passes:
        seats.append(decode_seat_id(boarding_pass))

    seats.sort()

    seat_no = seats[0]

    for i in range(len(seats)):
        if seats[i + 1] != seat_no + 1:
            return seats[i] + 1
        seat_no += 1


def decode_seat_id(seat_reference):
    seat_range = (0, 127)

    for c in seat_reference[:7]:
        seat_range = binary_decode(c, seat_range)

    row_range = (0, 7)
    for c in seat_reference[7:]:
        row_range = binary_decode(c, row_range)

    return seat_range[0] * 8 + row_range[0]


def binary_decode(char, num):
    mid_point = int((num[1] - num[0]) / 2)

    if char == 'F' or char == 'L':
        result = (num[0], num[0] + mid_point)
    if char == 'B' or char == 'R':
        result = (num[0] + mid_point + 1, num[1])

    return result


def read_input_data(filename):
    data = []

    with open(filename) as file:
        for line in file:
            data.append(line.strip('\n'))
    return data


class TestDay5BinaryBoarding(unittest.TestCase):
    def test_binary_decode(self):
        id = decode_seat_id('FBFBBFFRLR')
        self.assertEqual(357, id)

        id = decode_seat_id('FFFBBBFRRR')
        self.assertEqual(119, id)

        id = decode_seat_id('BBFFBBFRLL')
        self.assertEqual(820, id)

    def test_find_highest_seat_numberpart_1(self):
        data = read_input_data(input_file)

        result = find_highest_seat_number(data)
        print('Part1:', result)
        self.assertEqual(906, result)

    def test_find_missing_seat_numberpart_2(self):
        data = read_input_data(input_file)
        result = find_missing_seat(data)

        print('Part2:', result)
        self.assertEqual(519, result)


if __name__ == '__main__':
    unittest.main()
