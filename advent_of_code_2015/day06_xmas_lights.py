"""
https://adventofcode.com/2015/day/6

Note: Implemented for speed in terms of solving the solution, not for efficiency or scalability
"""

import unittest


def create_lighting_grid(length, height, light_state=0):
    lights = {}

    for row in range(height):
        for col in range(length):
            lights[(row, col)] = light_state

    return lights


def number_of_lights_on(lights):
    lights_on = 0

    for v in lights.values():
        lights_on += v
    return lights_on


def turn_on_light(lights, location):
    lights[location] = 1


def turn_off_light(lights, location):
    lights[location] = 0


def toggle_light(lights, location):
    value = lights[location]
    if value == 0:
        lights[location] = 1
    elif value == 1:
        lights[location] = 0


def __set_lights(lights, start_range, end_range, turn_on=True, toggle=False):
    elements = start_range.split(',')
    start_x = int(elements[0])
    start_y = int(elements[1])

    elements = end_range.split(',')
    end_x = int(elements[0])
    end_y = int(elements[1])

    locations = []
    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            locations.append((x,y))

    for location in locations:
        if toggle:
            toggle_light(lights, location)
        else:
            if turn_on:
                turn_on_light(lights, location)
            else:
                turn_off_light(lights, location)

    return lights


def turn_on_lights(lights, start_range, end_range):
    return __set_lights(lights, start_range, end_range)


def turn_off_lights(lights, start_range, end_range):
    return __set_lights(lights, start_range, end_range, turn_on=False)


def toggle_lights(lights, start_range, end_range):
    return __set_lights(lights, start_range, end_range, turn_on=False, toggle=True)


def read_input_data(filename):
    with open(filename) as file:
        return file.read().splitlines()


class TestDay06(unittest.TestCase):

    def test_number_of_lights_on(self):
        self.assertEquals(0, number_of_lights_on(create_lighting_grid(10, 10)))
        self.assertEquals(100, number_of_lights_on(create_lighting_grid(10, 10, 1)))

    def test_turn_on_lights(self):
        #turn on all lights
        #turn on 0,0 through 9,9
        lights = create_lighting_grid(10, 10)
        lights = turn_on_lights(lights, '0,0', '9,9')
        self.assertEquals(100, number_of_lights_on(lights))

    def test_turn_off_lights(self):
        #turn off all lights
        #turn off 0,0 through 9,9
        lights = create_lighting_grid(10, 10, 1)
        lights = turn_off_lights(lights, '0,0', '9,9')
        self.assertEquals(0, number_of_lights_on(lights))


    def test_toggle_lights(self):
        lights = create_lighting_grid(999, 999)
        lights = turn_on_lights(lights, '0,0', '999,0')
        self.assertEquals(1000, number_of_lights_on(lights))


    def test_part1(self):
        #toggle 118,413 through 736,632
        #turn off 798,782 through 829,813
        #turn on 798,782 through 829,813

        lights = create_lighting_grid(999,999)
        data = read_input_data(r'resources/day6_input.txt')
        for line in data:
            if line.startswith('toggle'):
                elements = line.split(' ')
                lights = toggle_lights(lights, elements[1], elements[3])
            elif line.startswith('turn on'):
                elements = line.split(' ')
                lights = turn_on_lights(lights, elements[2], elements[4])
            elif line.startswith('turn off'):
                elements = line.split(' ')
                lights = turn_off_lights(lights, elements[2], elements[4])

        result = number_of_lights_on(lights)
        print('Part1, Number of lights on:', result)
        self.assertEquals(569999, result)

if __name__ == '__main__':
    unittest.main()
