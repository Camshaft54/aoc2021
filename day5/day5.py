import math
import os
import shapely
from shapely.geometry import LineString, Point

# file = open(f'{os.path.dirname(os.path.realpath(__file__))}/test.txt').read()
file = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt').read()
# nums = list(map(int, file.split("\n")))
items = file.split("\n")


def part1():
    lines = []
    for item in items:
        endpoints = item.split(" -> ")
        lines.append([tuple(map(int, endpoints[0].split(","))), tuple(map(int, endpoints[1].split(",")))])
    print(lines)

    dangerous = set([])
    for i, line1 in enumerate(lines):
        for j, line2 in enumerate(lines):
            if i != j:
                d = intersect(line1, line2)
                # print(f"d of {line1} and {line2}: {d}")
                if d != 0 and d is not None:
                    for p in d:
                        dangerous.add(p)

    print(len(dangerous))


def part2():
    pass


def intersect(a, b):
    line1 = LineString(a)
    line2 = LineString(b)

    int_pt = line1.intersection(line2)
    if int_pt.is_empty:
        return 0

    a_start = a[0]
    a_end = a[1]
    b_start = b[0]
    b_end = b[1]
    # print(f"{a}: {a_start[0] != a_end[0] and a_start[1] != a_end[1]}")
    # if (a_start[0] != a_end[0] and a_start[1] != a_end[1]) or (b_start[0] != b_end[0] and b_start[1] != b_end[1]):
    #     return 0
    if a_start[0] == a_end[0]:
        if a_start[1] > a_end[1]:
            a_start, a_end = a_end, a_start
        if b_start[0] == b_end[0]:
            if b_start[1] > b_end[1]:
                b_start, b_end = b_end, b_start
            r = range(max(a_start[1], b_start[1]), min(b_end[1], a_end[1]) + 1)
            if len(r) > 0:
                return list(zip([b_start[0]] * len(r),
                                set(range(a_start[1], a_end[1] + 1)).intersection(range(b_start[1], b_end[1] + 1))))
            else:
                return 0
        elif b_start[1] == b_end[1]:
            if b_start[0] > b_end[0]:
                b_start, b_end = b_end, b_start
            if a_start[0] <= b_start[0] <= a_end[0]:
                return [(a_start[0], b_start[1])]
            elif b_start[0] <= a_start[0] <= b_end[0]:
                return [(a_start[0], b_start[1])]
            else:
                return 0
        else:
            return handle_diagonal_lines(a, b, 0, 2)
    elif a_start[1] == a_end[1]:
        if a_start[0] > a_end[0]:
            a_start, a_end = a_end, a_start
        if b_start[1] == b_end[1]:
            if b_start[0] > b_end[0]:
                b_start, b_end = b_end, b_start
            r = range(max(a_start[0], b_start[0]), min(b_end[0], a_end[0]) + 1)
            if len(r) > 0:
                return list(zip(set(range(a_start[0], a_end[0] + 1)).intersection(range(b_start[0], b_end[0] + 1)),
                                [b_start[1]] * len(r)))
        elif b_start[0] == b_end[0]:
            if b_start[1] > b_end[1]:
                b_start, b_end = b_end, b_start
            if a_start[1] <= b_start[1] <= a_end[1]:
                return [(b_start[0], a_start[1])]
            elif b_start[1] <= a_start[1] <= b_end[1]:
                return [(b_start[0], a_start[1])]
            else:
                return 0
        else:
            return handle_diagonal_lines(a, b, 1, 2)
    else:
        if b_start[0] == b_end[0]:
            return handle_diagonal_lines(a, b, 2, 0)
        elif b_start[1] == b_end[1]:
            return handle_diagonal_lines(a, b, 2, 1)
        else:
            return handle_diagonal_lines(a, b, 2, 2)


# type - 0 means x coords of endpoints are same, 1 is y coords are same, 2 is diagonal
def handle_diagonal_lines(a, b, a_type, b_type):
    # return set(lineToPoints(a, a_type)).intersection(lineToPoints(b, b_type))
    if a_type == 2 and abs(a[0][0] - a[1][0]) != abs(a[0][1] - a[1][1]):
        return None
    if b_type == 2 and abs(b[0][0] - b[1][0]) != abs(b[0][1] - b[1][1]):
        return None
    line1 = LineString(a)
    line2 = LineString(b)
    int_pt = line1.intersection(line2)
    if type(int_pt) is Point:
        return [(int(int_pt.x), int(int_pt.y))]
    else:
        print(int_pt.length)
        xy = []
        for f in range(0, int(round(int_pt.length)) + 1):
            p = int_pt.interpolate(f).coords[0]
            pr = tuple(map(round, p))
            if pr not in xy:
                xy.append(pr)
        print(xy)
        return xy


def lineToPoints(a, a_type):
    a_start = a[0]
    a_end = a[1]
    a_points = []
    if a_type == 0:
        for y in range(min(a_start[1], a_end[1]), max(a_start[1], a_end[1]) + 1):
            a_points.append((a_start[0], y))
    elif a_type == 1:
        for x in range(min(a_start[0], a_end[0]), max(a_start[0], a_end[0]) + 1):
            a_points.append((x, a_start[1]))
    else:
        if a_start[1] < a_end[1]:
            print("swapped start and end")
            a_start, a_end = a_end, a_start

        if a_start[0] < a_end[0]:
            for amt in range(a_end[0] - a_start[0] + 1):
                a_points.append((a_start[0] + amt, a_start[1] + amt))
        else:
            for amt in range(a_start[0] - a_end[0] + 1):
                a_points.append((a_start[0] - amt, a_start[1] - amt))
        print(f"{a_start}, {a_end}: {a_points}")
    return a_points


part1()
part2()
