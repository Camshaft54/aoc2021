import math
import os
import copy

# file = open('test.txt').read()
file = open('input.txt').read()


def valid(combo):
    if combo[0] < 0 or combo[0] >= len(data) or combo[1] < 0 or combo[1] >= len(data[0]):
        return False
    else:
        return True


def flash(marked, i, j):
    if (i, j) in marked:
        return
    marked.add((i, j))
    combos = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j),
              (i + 1, j + 1)]
    for c in combos:
        if valid(c):
            data[c[0]][c[1]] += 1
            if data[c[0]][c[1]] > 9:
                flash(marked, c[0], c[1])


def simulate(times, is_part2=False):
    flashes = 0
    for i in range(times):
        marked = set()
        for row in range(len(data)):
            for col in range(len(data[row])):
                data[row][col] = int(data[row][col])
                data[row][col] += 1

        for row in range(len(data)):
            for col in range(len(data[row])):
                if data[row][col] > 9:
                    flash(marked, row, col)
        flashes += len(marked)
        for c in marked:
            data[c[0]][c[1]] = 0

        if is_part2 and len(data) * len(data[0]) == len(marked):
            return i + 1
    return flashes


unparsed = file.split("\n")
original_data = []
for i in range(10):
    original_data.append(list(map(int, list(unparsed[i]))))
data = copy.deepcopy(original_data)
print(simulate(100))
data = copy.deepcopy(original_data)
print(simulate(100000, True))
