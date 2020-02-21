"""
https://adventofcode.com/2016/day/1

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""

import unittest


def process_directions(start_position, directions, stop_on_same_location=False):
    north = 0
    east = 1
    south = 2
    west = 3
    
    x_pos = start_position[0]
    y_pos = start_position[1]

    locations_visited = set()
    heading = north

    steps = directions.split(',')
    for step in steps:
        direction = step.strip()[0]
        distance = step.strip()[1:]
        heading = get_heading(heading, direction)

        for i in range(int(distance)):
            if heading == north:
                y_pos += 1
            elif heading == south:
                y_pos -= 1
            elif heading == east:
                x_pos += 1
            elif heading == west:
                x_pos -= 1

            loc = (x_pos, y_pos)

            if stop_on_same_location and loc in locations_visited:
                return loc

            locations_visited.add(loc)

    return x_pos, y_pos


def get_heading(heading, direction):
    new_heading = heading

    if direction == 'R':
        new_heading = heading + 1
    elif direction == 'L':
        new_heading = heading - 1

    if new_heading > 3:
         new_heading = 0
    elif new_heading < 0:
         new_heading = 3

    return abs(new_heading)


def calculate_distance_travelled(start_pos, end_pos):
    x = end_pos[0] - start_pos[0]
    y = end_pos[1] - start_pos[1]

    return abs(x) + abs(y)


class TestDay01(unittest.TestCase):

    def test_part_1_distance_travelled(self):
        position = (0, 0)
        input = 'L5, R1, L5, L1, R5, R1, R1, L4, L1, L3, R2, R4, L4, L1, L1, R2, R4, R3, L1, R4, L4, L5, L4, R4, L5, R1, R5, L2, R1, R3, L2, L4, L4, R1, L192, R5, R1, R4, L5, L4, R5, L1, L1, R48, R5, R5, L2, R4, R4, R1, R3, L1, L4, L5, R1, L4, L2, L5, R5, L2, R74, R4, L1, R188, R5, L4, L2, R5, R2, L4, R4, R3, R3, R2, R1, L3, L2, L5, L5, L2, L1, R1, R5, R4, L3, R5, L1, L3, R4, L1, L3, L2, R1, R3, R2, R5, L3, L1, L1, R5, L4, L5, R5, R2, L5, R2, L1, L5, L3, L5, L5, L1, R1, L4, L3, L1, R2, R5, L1, L3, R4, R5, L4, L1, R5, L1, R5, R5, R5, R2, R1, R2, L5, L5, L5, R4, L5, L4, L4, R5, L2, R1, R5, L1, L5, R4, L3, R4, L2, R3, R3, R3, L2, L2, L2, L1, L4, R3, L4, L2, R2, R5, L1, R2'

        end_position = process_directions(position, input)

        distance = calculate_distance_travelled(position, end_position)
        print('Part 1. Distance Travelled:', distance)

        self.assertEqual(226, distance)

    def test_part_2_distance_travelled_at_first_location_visited_twice(self):
        position = (0, 0)
        input = 'L5, R1, L5, L1, R5, R1, R1, L4, L1, L3, R2, R4, L4, L1, L1, R2, R4, R3, L1, R4, L4, L5, L4, R4, L5, R1, R5, L2, R1, R3, L2, L4, L4, R1, L192, R5, R1, R4, L5, L4, R5, L1, L1, R48, R5, R5, L2, R4, R4, R1, R3, L1, L4, L5, R1, L4, L2, L5, R5, L2, R74, R4, L1, R188, R5, L4, L2, R5, R2, L4, R4, R3, R3, R2, R1, L3, L2, L5, L5, L2, L1, R1, R5, R4, L3, R5, L1, L3, R4, L1, L3, L2, R1, R3, R2, R5, L3, L1, L1, R5, L4, L5, R5, R2, L5, R2, L1, L5, L3, L5, L5, L1, R1, L4, L3, L1, R2, R5, L1, L3, R4, R5, L4, L1, R5, L1, R5, R5, R5, R2, R1, R2, L5, L5, L5, R4, L5, L4, L4, R5, L2, R1, R5, L1, L5, R4, L3, R4, L2, R3, R3, R3, L2, L2, L2, L1, L4, R3, L4, L2, R2, R5, L1, R2'

        end_position = process_directions(position, input, True)

        distance = calculate_distance_travelled(position, end_position)
        print('Part 2. Distance Travelled:', distance)

        self.assertEqual(79, distance)

    def test_part_2_distance_travelled_at_first_location_visited_twice_example_data(self):
        position = (0, 0)
        input = 'R8, R4, R4, R8'

        end_position = process_directions(position, input, True)

        distance = calculate_distance_travelled(position, end_position)
        print('Distance Travelled:', distance)

        self.assertEqual(4, distance)


if __name__ == '__main__':
    unittest.main()

