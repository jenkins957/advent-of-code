import unittest


class IntComputer:
    def __init__(self):
        self.program = []

    def reset(self):
        self.program = []

    def load_program(self, program):
        self.program = program

    def __get_indirect_value(self, index):
        op1_index = self.program[index]
        return self.program[op1_index]

    @staticmethod
    def __perform_operation(op_code, op1, op2):
        if op_code == 1:
            return op1 + op2
        return op1 * op2

    def execute(self):
        index = 0

        while index < len(self.program):
            instruction = int(self.program[index])

            if instruction == 1 or instruction == 2:
                op1 = self.__get_indirect_value(index + 1)
                op2 = self.__get_indirect_value(index + 2)
                result_index = self.program[index + 3]
                self.program[result_index] = self.__perform_operation(instruction, op1, op2)
                index += 4
            elif instruction == 99:
                return self.program
            else:
                raise SyntaxError('Invalid OpCode:' + str(instruction))

        return self.program


class TestIntComputer(unittest.TestCase):
    def test_should_halt_program(self):
        int_computer = IntComputer()
        int_computer.load_program([99])
        result = int_computer.execute()

        self.assertEqual([99], result)

        int_computer.load_program([99, 99])
        result = int_computer.execute()

        self.assertEqual([99, 99], result)

    def test_should_halt_program_with_error_for_when_unknown_op_code(self):
        int_computer = IntComputer()
        int_computer.load_program('7'.split(','))
        self.assertRaises(SyntaxError, int_computer.execute)

    def test_should_add_2_numbers_and_store_result(self):
        int_computer = IntComputer()
        # Add 10 + 11 and store result in index 3
        int_computer.load_program([1, 5, 6, 3, 99, 10, 11])
        self.assertEqual([1, 5, 6, 21, 99, 10, 11], int_computer.execute())

    def test_should_multiply_2_numbers_and_store_result(self):
        int_computer = IntComputer()
        # Multiply 10 + 11 and store result in index 3
        int_computer.load_program([2, 5, 6, 3, 99, 10, 11])
        self.assertEqual([2, 5, 6, 110, 99, 10, 11], int_computer.execute())

    def test_should_execute_program_and_return_result(self):
        int_computer = IntComputer()
        int_computer.load_program([1, 0, 0, 0, 99])
        self.assertEqual([2, 0, 0, 0, 99], int_computer.execute())

        int_computer = IntComputer()
        int_computer.load_program([2, 3, 0, 3, 99])
        self.assertEqual([2, 3, 0, 6, 99], int_computer.execute())

        int_computer = IntComputer()
        int_computer.load_program([2, 4, 4, 5, 99, 0])
        self.assertEqual([2, 4, 4, 5, 99, 9801], int_computer.execute())

        int_computer = IntComputer()
        int_computer.load_program([1, 1, 1, 4, 99, 5, 6, 0, 99])
        self.assertEqual([30, 1, 1, 4, 2, 5, 6, 0, 99], int_computer.execute())


if __name__ == '__main__':
    unittest.main()
