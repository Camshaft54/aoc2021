import math
import os

# file = open(f'{os.path.dirname(os.path.realpath(__file__))}/test.txt').read()
file = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt').read()
lines = file.split("\n")


def part1():
    tot = 0
    incomplete_lines = []
    for line in lines:
        curr = check_line(list(line))
        if curr == 0:
            incomplete_lines.append(list(line))
        else:
            tot += check_line(list(line))
    print(tot)


def check_line(line: list):
    open_chars = []
    char_type = {")": "(", "]": "[", "}": "{", ">": "<"}
    point_val = {")": 3, "]": 57, "}": 1197, ">": 25137}
    points = 0
    for i, char in enumerate(line):
        if char in ["(", "[", "{", "<"]:
            open_chars.append(char)
        elif char in [")", "]", "}", ">"]:
            if char_type[char] != open_chars[-1]:
                points += point_val[char]
                # print(f"Expected {open_chars[-1]} but found {char} instead")
                return points
            else:
                open_chars.pop(-1)
    return points

def complete_line(line: list):
    open_chars = []
    char_type = {"(": ")", "[": "]", "{": "}", "<": ">"}
    point_val = {")": 1, "]": 2, "}": 3, ">": 4}
    for i, char in enumerate(line):
        if char in ["(", "[", "{", "<"]:
            open_chars.append(char)
        elif char in [")", "]", "}", ">"]:
            open_chars.pop(-1)

    points = 0
    str_to_add = ""
    for char in reversed(open_chars):
        points *= 5
        str_to_add += char_type[char]
        points += point_val[str_to_add[-1]]
    return points


def part2():
    scores = []
    for line in lines:
        curr = check_line(list(line))
        if curr == 0:
            scores.append(complete_line(list(line)))
            # print(complete_line(list(line)))
    print(sorted(scores)[len(scores)//2])

# part1()
part2()