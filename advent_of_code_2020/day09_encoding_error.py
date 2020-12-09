"""
https://adventofcode.com/2020/day/9

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""

import unittest

input_file = r'resources/day9_input.txt'


def find_first_number_that_cannot_be_summed(all_numbers, preamble_count):
    # Split preamble and numbers
    preamble = all_numbers[:preamble_count]
    numbers = all_numbers[preamble_count:]

    start = 0
    end = len(preamble)
    for n in numbers:
        result = __two_sum(all_numbers[start:end], n)
        if result is None:
            # This number cannot be summed by any of the previous n numbers. n defined by preamble_count
            return n
        start += 1
        end += 1


def calculate_the_encryption_weakness(numbers, preamble_count):
    """
    Find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.
    Add together the smallest and largest number in this contiguous range
    """
    result = find_first_number_that_cannot_be_summed(numbers, preamble_count)

    for i in range(len(numbers)):
        temp_sum = 0
        sum_nums = []
        for j in range(i, len(numbers)):
            temp_sum += numbers[j]
            sum_nums.append(numbers[j])

            # early out if we are over the target number
            if temp_sum > result:
                break

            if temp_sum == result:
                # found contiguous set of numbers adding up to target, sum lowest and highest
                sum_nums.sort()
                return sum_nums[0] + sum_nums[len(sum_nums) - 1]

    return result


def __two_sum(nums, target):
    required = {}
    for i in range(len(nums)):
        if target - nums[i] in required:
            return [required[target - nums[i]], i]
        else:
            required[nums[i]] = i
    return None


def read_integer_input_data(filename):
    numbers = []

    with open(filename) as file:
        for line in file:
            numbers.append(int(line.strip('\n')))
    return numbers


class TestDay9EncodingError(unittest.TestCase):
    def test_find_first_number_that_cannot_be_summed(self):
        result = find_first_number_that_cannot_be_summed(read_integer_input_data(input_file), 25)

        print('Part1:', result)
        self.assertEqual(25918798, result)

    def test_part_2(self):
        result = calculate_the_encryption_weakness(read_integer_input_data(input_file), 25)

        # too high: 27438220
        print('Part2:', result)
        self.assertEqual(3340942, result)


if __name__ == '__main__':
    unittest.main()
