"""
https://adventofcode.com/2020/day/8

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""

import unittest

input_file = r'resources/day8_input.txt'


def execute_program_part1(data):
    accumulator = 0

    instructions = parse_instructions(data)

    # Keep track of all the unique instructions (via the pointer) to find first duplicate instruction executed
    ins_pointers = set()

    instruction_pointer = 0
    while instruction_pointer < len(instructions):

        # find the infinite loop and break out of the program - first duplicate instruction encountered
        if instruction_pointer in ins_pointers:
            break

        ins_pointers.add(instruction_pointer)

        ins = instructions[instruction_pointer]
        op = ins[0]
        val = ins[1]

        if op == 'acc':
            accumulator += val
            instruction_pointer += 1
        elif op == 'jmp':
            instruction_pointer += val
        else:
            # nop
            instruction_pointer += 1

    return accumulator


def identify_and_fix_infinite_loop(data):

    # Try replacing nop with jmp then jmp wth nop to fix the infinte loop
    result = __identify_and_fix_infinite_loop(data, 'jmp', 'nop')
    if result[0] == -1:
        result = __identify_and_fix_infinite_loop(data, 'nop', 'jmp')

    return result[1]


def __identify_and_fix_infinite_loop(data, source_ins, target_ins):

    # result holds program exit code and accumulator result
    result = (-1, 0)

    line_index = 0

    # brute force. Try replacing evey jmp with nop and retry program after each change, looking for a normal exit
    for _ in range(len(data)):
        # read instructions from file to ensure fresh
        instructions = parse_instructions(data)

        # modify next instruction
        instructions = modify_program(instructions, line_index, source_ins, target_ins)
        line_index = instructions[1]

        result = execute_program_part2(instructions[0])
        if result[0] == 0:
            break

    return result


def modify_program(instructions, line_index, source, target):

    for i in range(line_index, len(instructions)):
        ins = instructions[i]

        if ins[0] == source:
            line_index = i
            instructions[i] = (target, ins[1])
            break

    return instructions, line_index + 1


def execute_program_part2(instructions):
    accumulator = 0

    # Process instructions
    ins_pointers = set()

    instruction_pointer = 0
    while instruction_pointer < len(instructions):

        if instruction_pointer in ins_pointers:
            return -1, accumulator

        ins_pointers.add(instruction_pointer)

        ins = instructions[instruction_pointer]
        op = ins[0]
        val = ins[1]

        if op == 'acc':
            accumulator += val
        if op == 'jmp':
            instruction_pointer += val - 1

        instruction_pointer += 1

    return 0, accumulator


def parse_instructions(data):
    instructions = []

    for line in data:
        elements = line.split()

        ins = (elements[0])
        val = int(elements[1][1:])

        if '-' in elements[1]:
            val *= -1

        instructions.append((ins, val))

    return instructions


def read_input_data(filename):
    with open(filename) as file:
        data = [line.strip() for line in file.readlines()]

    return data


class TestDay8HandheldHalting(unittest.TestCase):
    def test_part_1(self):
        result = execute_program_part1(read_input_data(input_file))

        print('Part1:', result)
        self.assertEqual(1487, result)

    def test_part_2(self):
        result = identify_and_fix_infinite_loop(read_input_data(input_file))

        print('Part2:', result)
        self.assertEqual(1607, result)


if __name__ == '__main__':
    unittest.main()
