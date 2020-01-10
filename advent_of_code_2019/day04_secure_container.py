"""
https://adventofcode.com/2019/day/4
"""


"""
Returns true if string contains at least 2 adjacent characters
i.e 12334 or 112233 or 111111
"""


def contains_2_adjacent_digits(input_string):
    prev_number = -1
    result = False

    for n in input_string:
        num = int(n)
        if num == prev_number:
            result = True
            break
        prev_number = num

    return result


"""
Returns true is the numeric string contains a list of numbers either the 
same or in ascending order
i.e 1234, 11223, 
Examples of an invalid string, 112340 132 11223354
"""


def digits_same_or_increase(input_string):
    prev_number = string[0]
    result = True

    for n in input_string:
        if n < prev_number:
            result = False
            break
        prev_number = n

    return result


"""
Returns true is the string contains 2 adjacent characters.
Digits are not part of a larger group
i.e 12334 is valid, 123334 is not
111122 is valid because of the adjacent 2s
"""


def contains_2_adjacent_digits_strict(input_string):
    num_count = {}
    prev_number = -1

    for n in input_string:
        num = int(n)
        if num == prev_number:
            if n in num_count.keys():
                num_count[n] = num_count[n] + 1
            else:
                num_count[n] = 2
        prev_number = num

    for k, v in num_count.items():
        if v == 2:
            return True
    return False


if __name__ == "__main__":
    total_combinations = 0
    for i in range(999999):
        string = "{:06d}".format(i)
        if contains_2_adjacent_digits(string) and digits_same_or_increase(string) and i >= 145852 and i <= 616942:
                total_combinations += 1

    print('Total Combinations (Part1):', total_combinations)

    total_combinations = 0
    for i in range(999999):
        string = "{:06d}".format(i)

        if contains_2_adjacent_digits_strict(string) and digits_same_or_increase(string) and i >= 145852 and i <= 616942:
                total_combinations += 1
    print('Total Combinations (Part2):', total_combinations)

