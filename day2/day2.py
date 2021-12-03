import math
import os

# file = open(f'{os.path.dirname(os.path.realpath(__file__))}/test.txt', 'r').read()
file = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', 'r').read()
# nums = list(map(int, file.split("\n")))
items = file.split("\n")


def part1():
    forward = 0
    depth = 0
    for item in items:
        item_parsed = item.split(" ")
        if item_parsed[0] == 'forward':
            forward += int(item_parsed[1])
        elif item_parsed[0] == 'down':
            depth += int(item_parsed[1])
        else:
            depth -= int(item_parsed[1])
    print(f"forward: {forward} depth: {depth}")
    print(f"Part 1: forward * depth = {forward * depth}")


def part2():
    forward = 0
    depth = 0
    aim = 0
    for item in items:
        item_parsed = item.split(" ")
        if item_parsed[0] == 'forward':
            forward += int(item_parsed[1])
            depth += aim * int(item_parsed[1])
        elif item_parsed[0] == 'down':
            aim += int(item_parsed[1])
        else:
            aim -= int(item_parsed[1])
    print(f"forward: {forward} depth: {depth} aim: {aim}")
    print(f"Part 2: forward * aim = {forward * aim}")


part1()
part2()
