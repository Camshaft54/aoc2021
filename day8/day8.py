import math
import os

file = open(f'{os.path.dirname(os.path.realpath(__file__))}/test.txt').read()
# file = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt').read()
notes = file.split("\n")


def part1():
    count = 0
    for note in notes:
        output = note.split(" | ")[1].split(" ")
        for val in output:
            if len(val) in [2, 3, 4, 7]:
                count += 1
    print(count)


def part2():
    tot = 0
    for idx, note in enumerate(notes):
        digits = [""] * 10
        input = note.split(" | ")[0].split(" ")
        output = note.split(" | ")[1].split(" ")

        five_len = []
        six_len = []
        for val in input:
            if len(val) == 2:
                digits[1] = val
            elif len(val) == 3:
                digits[7] = val
            elif len(val) == 4:
                digits[4] = val
            elif len(val) == 7:
                digits[8] = val
            elif len(val) == 5:
                five_len.append(val)
            elif len(val) == 6:
                six_len.append(val)
        for i in range(3):
            p = set(digits[1]).difference(six_len[i])
            if len(p) == 1:
                digits[6] = six_len.pop(i)
                break

        left_bottom = ''
        for i in range(3):
            p = set(digits[6]).difference(five_len[i])
            if len(p) == 1:
                digits[5] = five_len.pop(i)
                left_bottom = p.pop()
                break

        if left_bottom in six_len[1]:
            six_len.reverse()
        digits[0] = six_len[0]
        digits[9] = six_len[1]

        if left_bottom in five_len[1]:
            five_len.reverse()
        digits[2] = five_len[0]
        digits[3] = five_len[1]

        # output time
        res = ""
        for val in output:
            for digit in digits:
                if set(digit) == set(val):
                    res += str(digits.index(digit))
        print(f"{idx}: {res}")
        tot += int(res)
    print(tot)


part1()
part2()
