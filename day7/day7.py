import math
import os

# file = open(f'{os.path.dirname(os.path.realpath(__file__))}/test.txt').read()
file = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt').read()
nums = list(map(int, file.split(",")))


def calc_fuel_consumption(fuel_fx):
    fuels = []
    for i in range(min(nums), max(nums)):
        tot_fuel = 0
        for j in nums:
            tot_fuel += fuel_fx(i, j)
        fuels.append(tot_fuel)
    print(min(fuels))


def part2_calc_fuel(start, end):
    d = abs(start - end)
    return int(d * (d + 1) / 2)


def part1_calc_fuel(start, end):
    return abs(start - end)


print("Part 1:")
calc_fuel_consumption(part1_calc_fuel)
print("Part 2:")
calc_fuel_consumption(part2_calc_fuel)
