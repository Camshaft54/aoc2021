import math
import os

# file = open(f'{os.path.dirname(os.path.realpath(__file__))}/test.txt', 'r').read()
file = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', 'r').read()
# items = list(map(int, file.split("\n")))
items = file.split("\n")


def part1():
    # Invert columns and rows of items and find most common character in each sublist
    most_common = "".join(map(lambda a: max(set(a), key=a.count), zip(*items)))
    inverse = most_common.translate({ord("0"): "1", ord("1"): "0"})
    print(f"Part 1: {int(most_common, 2) * int(inverse, 2)}\n")


def part2():
    co2 = items[:]
    o2 = items[:]
    o2_final = ''
    co2_final = ''
    for i in range(len(items[0])):
        if len(co2) == 1:
            co2_final = co2[0]
        if len(o2) == 1:
            o2_final = o2[0]

        co2_counted = list(map(lambda a: int(a[i]), co2))
        if co2_counted.count(0) <= co2_counted.count(1):
            co2 = list(filter(lambda a: a[i] == '0', co2))
        else:
            co2 = list(filter(lambda a: a[i] == '1', co2))

        o2_counted = list(map(lambda a: int(a[i]), o2))
        if o2_counted.count(0) > o2_counted.count(1):
            o2 = list(filter(lambda a: a[i] == '0', o2))
        else:
            o2 = list(filter(lambda a: a[i] == '1', o2))
    if len(co2) == 1:
        co2_final = co2[0]
    if len(o2) == 1:
        o2_final = o2[0]

    print(f"co2: {co2_final} o2: {o2_final}")

    if co2_final != '' and o2_final != '':
        print(f"Part 2: {int(co2_final, 2) * int(o2_final, 2)}")
    else:
        print("Could not solve")


part1()
part2()
