"""
https://adventofcode.com/2019/day/2
"""

import unittest


def gravity_assist_calc(data):
    opcode_index = 0

    while (opcode_index < len(data)):
        opcode = data[opcode_index]

        if not is_valid_instruction(opcode):
            print('Invalid OPCode:', opcode)
            exit(-1)

        if opcode == 99:
            # print('HALT')
            break
        elif opcode == 1 or opcode == 2:
            input1Index = data[opcode_index + 1]
            input2Index = data[opcode_index + 2]
            outputIndex = data[opcode_index + 3]

            num1 = data[input1Index]
            num2 = data[input2Index]
            res_index = outputIndex

            if opcode == 1:
                sum = num1 + num2
            elif opcode == 2:
                sum = num1 * num2

            data[res_index] = sum

        opcode_index += 4

    return data


def is_valid_instruction(ins):
    return ins == 1 or ins == 2 or ins == 99


def reset_program_memory():
    return [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 9, 1, 19, 1, 19, 5, 23, 1, 9, 23, 27, 2, 27, 6, 31, 1,
            5, 31, 35, 2, 9, 35, 39, 2, 6, 39, 43, 2, 43, 13, 47, 2, 13, 47, 51, 1, 10, 51, 55, 1, 9, 55, 59, 1, 6, 59,
            63, 2, 63, 9, 67, 1, 67, 6, 71, 1, 71, 13, 75, 1, 6, 75, 79, 1, 9, 79, 83, 2, 9, 83, 87, 1, 87, 6, 91, 1,
            91, 13, 95, 2, 6, 95, 99, 1, 10, 99, 103, 2, 103, 9, 107, 1, 6, 107, 111, 1, 10, 111, 115, 2, 6, 115, 119,
            1, 5, 119, 123, 1, 123, 13, 127, 1, 127, 5, 131, 1, 6, 131, 135, 2, 135, 13, 139, 1, 139, 2, 143, 1, 143,
            10, 0, 99, 2, 0, 14, 0]


def calcualte_noun_verb():
    # part 2
    for noun in range(3, 99):
        for verb in range(3, 99):
            data = reset_program_memory()
            data[1] = noun
            data[2] = verb
            data = gravity_assist_calc(data)

            if data[0] == 19690720:
                return 100 * noun + verb
    return 0


# Unit Tests
class TestStrinTestGravityAssistCalculatorgMethods(unittest.TestCase):
    def test_add(self):
        data = [1, 0, 0, 3, 99]
        gravity_assist_calc(data)

        self.assertEqual([1, 0, 0, 2, 99], data)

    def test_multiply(self):
        data = [2, 0, 0, 3, 99]
        gravity_assist_calc(data)

        self.assertEqual([2, 0, 0, 4, 99], data)

    def test_halt(self):
        data = [99, 1, 0, 0, 3]
        gravity_assist_calc(data)

        self.assertEqual([99, 1, 0, 0, 3], data)

    def test_part1(self):
        data = reset_program_memory()
        result = gravity_assist_calc(data)
        print('Part 1 Value at index 0: ', data[0])

        self.assertEqual(6568671, int(result[0]))

    def test_part2(self):
        result = calcualte_noun_verb()
        print('Part 2 Value: ', calcualte_noun_verb())

        self.assertEqual(3951, result)


if __name__ == '__main__':
    unittest.main()
