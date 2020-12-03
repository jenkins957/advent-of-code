"""
https://adventofcode.com/2020/day/3

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""

import unittest

input_file = r'resources/day3_input.txt'


def count_trees_on_route(map, right, down):
    """
    Traverse the map (map wraps to the right). Using the supplied route (right and down)
    return a count of how many trees were encountered from top to bottom of the map.
    Tree denoted by the '#' symbol.

    :param map: The map
    :param right: number of squares to move to the right
    :param down: number of squares to move down
    :return: Number of trees encountered
    """
    trees = 0
    y_pos = 0
    x_pos = 0

    while y_pos <= len(map) - 1:
        row = map[y_pos]

        if row[x_pos] == '#':
            trees += 1

        # Map wraps around to the the right
        x_pos = (x_pos + right) % len(row)
        y_pos += down

    return trees


def read_input_data(filename):
    data = []

    with open(filename) as file:
        for line in file:
            data.append(line.strip('\n'))
    return data


class TestTobogganTrajectory(unittest.TestCase):
    def test_route(self):
        map = []

        map.append("..##.......");
        map.append("#...#...#..");
        map.append(".#....#..#.");
        map.append("..#.#...#.#");
        map.append(".#...##..#.");
        map.append("..#.##.....");
        map.append(".#.#.#....#");
        map.append(".#........#");
        map.append("#.##...#...");
        map.append("#...##....#");
        map.append(".#..#...#.#");

        result = count_trees_on_route(map, 3, 1)
        self.assertEqual(7, result)

    def test_count_trees_on_route_part1(self):
        map = read_input_data(input_file)

        result = count_trees_on_route(map, 3, 1)
        print('Part1:', result)
        self.assertEqual(153, result)

    def test_sum_of_trees_on_multiple_routes_part2(self):
        map = read_input_data(input_file)

        # Multiple routes, find product of them all
        r1 = count_trees_on_route(map, 1, 1)
        self.assertEqual(66, r1)

        r2 = count_trees_on_route(map, 3, 1)
        self.assertEqual(153, r2)

        r3 = count_trees_on_route(map, 5, 1)
        self.assertEqual(79, r3)

        r4 = count_trees_on_route(map, 7, 1)
        self.assertEqual(92, r4)

        r5 = count_trees_on_route(map, 1, 2)
        self.assertEqual(33, r5)

        total = r1 * r2 * r3 * r4 * r5

        print('Part2:', total)
        self.assertEqual(2421944712, total)


if __name__ == '__main__':
    unittest.main()
