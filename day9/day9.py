import math
import os

# file = open(f'{os.path.dirname(os.path.realpath(__file__))}/test.txt').read()
file = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt').read()
# nums = list(map(int, file.split("\n")))
lines = file.split("\n")


def part1():
    parsed = []
    for line in lines:
        l = list(map(int, list(line)))
        print(l)
        parsed.append(l)

    tot = 0
    for i, line in enumerate(parsed):
        for j, n in enumerate(line):
            if j != 0 and line[j-1] <= n:
                continue
            elif j != len(line)-1 and line[j+1] <= n:
                continue
            elif i != 0 and parsed[i-1][j] <= n:
                continue
            elif i != len(parsed)-1 and parsed[i+1][j] <= n:
                continue
            else:
                tot += n + 1
    print(tot)


def get_basin(parsed: list, i, j, res:list):
    this = []
    if j != 0 and parsed[i][j - 1] != '9' and '*' not in parsed[i][j - 1]:
        parsed[i][j-1] += '*'
        this.append(parsed[i][j-1])
        this.extend(get_basin(parsed, i, j-1, res))
    if j != len(parsed[0]) - 1 and parsed[i][j + 1] != '9' and '*' not in parsed[i][j + 1]:
        parsed[i][j + 1] += '*'
        this.append(parsed[i][j + 1])
        this.extend(get_basin(parsed, i, j + 1, res))
    if i != 0 and parsed[i - 1][j] != '9' and '*' not in parsed[i - 1][j]:
        parsed[i - 1][j] += '*'
        this.append(parsed[i - 1][j])
        this.extend(get_basin(parsed, i - 1, j, res))
    if i != len(parsed) - 1 and parsed[i + 1][j] != '9' and '*' not in parsed[i + 1][j]:
        parsed[i + 1][j] += '*'
        this.append(parsed[i + 1][j])
        this.extend(get_basin(parsed, i + 1, j, res))
    return this


def part2():
    parsed = []
    for line in lines:
        l = list(line)
        parsed.append(l)

    basins = []
    for i, line in enumerate(parsed):
        for j, n in enumerate(line):
            if n[-1] != '*' and int(n) != 9:
                parsed[i][j] = n + '*'
                basins.append(1+len(get_basin(parsed, i, j, [n])))
    print(sorted(basins))


part1()
part2()
