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


def calculate_total_brightness(lights):
    lights_on = 0

    for v in lights.values():
        lights_on += v
    return lights_on


def turn_on_light(lights, location, dimmer_mode=False):
    if dimmer_mode:
        lights[location] += 1
    else:
        lights[location] = 1


def turn_off_light(lights, location, dimmer_mode=False):
    if dimmer_mode:
        if lights[location] > 0:
            lights[location] -= 1
    else:
        lights[location] = 0


def toggle_light(lights, location, dimmer_mode=False):
    if dimmer_mode:
        #increase brightness by 2
        lights[location] += 2
    else:
        value = lights[location]
        if value == 0:
            lights[location] = 1
        elif value == 1:
            lights[location] = 0


def __set_lights(lights, start_range, end_range, turn_on=True, toggle=False, dimmer_mode=False):
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
            toggle_light(lights, location, dimmer_mode)
        else:
            if turn_on:
                turn_on_light(lights, location, dimmer_mode)
            else:
                turn_off_light(lights, location, dimmer_mode)

    return lights


def turn_on_lights(lights, start_range, end_range, dimmer_mode=False):
    return __set_lights(lights, start_range, end_range, turn_on=True, toggle=False, dimmer_mode=dimmer_mode)


def turn_off_lights(lights, start_range, end_range, dimmer_mode=False):
    return __set_lights(lights, start_range, end_range, turn_on=False, toggle=False, dimmer_mode=dimmer_mode)


def toggle_lights(lights, start_range, end_range, dimmer_mode=False):
    return __set_lights(lights, start_range, end_range, turn_on=False, toggle=True, dimmer_mode=dimmer_mode)


def read_input_data(filename):
    with open(filename) as file:
        return file.read().splitlines()


class TestDay06(unittest.TestCase):

    def test_number_of_lights_on(self):
        self.assertEquals(0, calculate_total_brightness(create_lighting_grid(10, 10)))
        self.assertEquals(100, calculate_total_brightness(create_lighting_grid(10, 10, 1)))

    def test_turn_on_lights(self):
        #turn on all lights
        #turn on 0,0 through 9,9
        lights = create_lighting_grid(10, 10)
        lights = turn_on_lights(lights, '0,0', '9,9')
        self.assertEquals(100, calculate_total_brightness(lights))

    def test_turn_off_lights(self):
        #turn off all lights
        #turn off 0,0 through 9,9
        lights = create_lighting_grid(10, 10, 1)
        lights = turn_off_lights(lights, '0,0', '9,9')
        self.assertEquals(0, calculate_total_brightness(lights))

    def test_toggle_lights(self):
        lights = create_lighting_grid(1000, 1000)
        lights = toggle_lights(lights, '0,0', '999,0')
        self.assertEquals(1000, calculate_total_brightness(lights))

        lights = create_lighting_grid(1000, 1000)
        lights = toggle_lights(lights, '0,0', '999,0')
        self.assertEquals(1000, calculate_total_brightness(lights))

    def test_toggle_lights_dimmer_mode(self):
        lights = create_lighting_grid(1000, 1000)
        lights = toggle_lights(lights, '0,0', '999,999', True)
        self.assertEquals(2000000, calculate_total_brightness(lights))

    def test_increase_brightness(self):
        lights = create_lighting_grid(10, 10)
        self.assertEquals(0, calculate_total_brightness(lights))
        turn_on_light(lights, (0, 0), True)
        turn_on_light(lights, (0, 0), True)
        turn_on_light(lights, (0, 0), True)
        toggle_light(lights, (0, 0), True)
        turn_on_light(lights, (9, 9), True)

        self.assertEquals(6, calculate_total_brightness(lights))

    def test_decrease_brightness(self):
        lights = create_lighting_grid(10, 10)
        self.assertEquals(0, calculate_total_brightness(lights))
        turn_on_light(lights, (0, 0), True)
        self.assertEquals(1, calculate_total_brightness(lights))
        turn_off_light(lights, (0, 0), True)
        self.assertEquals(0, calculate_total_brightness(lights))
        # Going below 0 not possible
        turn_off_light(lights, (0, 0), True)
        self.assertEquals(0, calculate_total_brightness(lights))


    def test_part1(self):
        #toggle 118,413 through 736,632
        #turn off 798,782 through 829,813
        #turn on 798,782 through 829,813

        lights = create_lighting_grid(1000, 1000)
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

        result = calculate_total_brightness(lights)
        print('Part1, Number of lights on:', result)
        self.assertEquals(569999, result)

    def test_part2(self):
        #Turn on increases brightness, turn off decreases brightness, toggle, inc brightness by 2
        lights = create_lighting_grid(1000, 1000)
        data = read_input_data(r'resources/day6_input.txt')
        for line in data:
            if line.startswith('toggle'):
                elements = line.split(' ')
                lights = toggle_lights(lights, elements[1], elements[3], True)
            elif line.startswith('turn on'):
                elements = line.split(' ')
                lights = turn_on_lights(lights, elements[2], elements[4], True)
            elif line.startswith('turn off'):
                elements = line.split(' ')
                lights = turn_off_lights(lights, elements[2], elements[4], True)

        result = calculate_total_brightness(lights)
        print('Part2, Total Brightness of lights:', result)
        # too low 17325717
        self.assertEquals(17836115, result)


if __name__ == '__main__':
    unittest.main()
