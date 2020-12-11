"""
https://adventofcode.com/2020/day/11

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""

import copy
import unittest

input_file = r'resources/day11_input.txt'


def part1(data):

    grid = []

    for line in data:
        row = []
        for c in line:
            row.append(c)
        grid.append(row)

    previous_occupied_seats = 0

    for _ in range(200):
        grid, changes = __update_grid(grid)
        # print_grid(grid)
        oc = __count_occupied_seats(grid)

        if oc == previous_occupied_seats:
            break

        previous_occupied_seats = oc

    return oc


def __count_occupied_seats(grid):
    count = 0
    for row in grid:
        for c in row:
            if c == '#':
                count += 1
    return count


def __update_grid(grid):
    count = 0
    # return a new grid to ensure all changes are made simultaneously
    new_grid = copy.deepcopy(grid)

    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell == 'L':
                # Check adjacent seats
                changes =  __are_adjacent_seats_occupied(grid, row_index, col_index)
                if changes == 0:
                    new_grid[row_index][col_index] = '#'
                    count += 1
            elif cell == '#':
                changes2 = __are_adjacent_seats_occupied(grid, row_index, col_index)
                if changes2 >= 4:
                    new_grid[row_index][col_index] = 'L'
                    count += 1

        row_index += 1

    return new_grid, count


def __are_adjacent_seats_occupied(grid, row_index, col_index):
    count = 0

    # Check Previous row, if exists
    if row_index > 0:
        prev_row = grid[row_index - 1]
        count += __are_adjacent_seats_occupied_for_row(prev_row, col_index)

    # Next row. if exists
    if row_index < len(grid) - 1:
        next_row = grid[row_index + 1]
        count += __are_adjacent_seats_occupied_for_row(next_row, col_index)

    # current row
    count += __are_adjacent_seats_occupied_for_row(grid[row_index], col_index, check_middle=False)

    return count


def __are_adjacent_seats_occupied_for_row(row, col_index, check_middle=True):
    count = 0

    # Check Previous seat, if exists
    if col_index > 0:
        if row[col_index - 1] == '#':
            count += 1

    if check_middle:
        if row[col_index] == '#':
            count += 1

    # Next row. if exists
    if col_index < len(row) - 1:
        if row[col_index + 1] == '#':
            count += 1

    return count


def print_grid(grid):
    for row in grid:
        row_str = ''
        for c in row:
            row_str += c
        print(row_str)


def read_input_data(filename):
    with open(filename) as file:
        data = [line.strip() for line in file.readlines()]

    return data


class TestDay11SeatingSystem(unittest.TestCase):
    def test_part_1_0(self):
        result = part1(read_input_data(input_file))

        self.assertEqual(2412, result)


if __name__ == '__main__':
    unittest.main()
