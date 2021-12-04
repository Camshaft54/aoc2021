import math
import os

# file = open(f'{os.path.dirname(os.path.realpath(__file__))}/test.txt').read()
file = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt').read()
# nums = list(map(int, file.split("\n")))
items = file.split("\n")

scores = []


def part1and2():
    numbers = items[0].split(",")
    raw_boards = items[2:]
    boards = []
    for i in range(0, len(raw_boards), 6):
        raw_board = raw_boards[i:i + 5]
        board = []
        for j in range(len(raw_board)):
            board.append(raw_board[j].split(" "))
            while "" in board[j]:
                board[j].remove("")
        boards.append(board)

    for i in [int(j) for j in numbers]:
        for board in range(len(boards)):
            for row in range(5):
                for num in range(5):
                    if "^" not in boards[board][row][num] and int(boards[board][row][num]) == i:
                        boards[board][row][num] += "^"

        for board in boards:
            if check_board(board):
                scores.append(unused(board) * i)
                boards.remove(board)
    print(f"Part 1 (first winner): {scores[0]}\nPart 2 (last winner): {scores[-1]}")


def check_board(board):
    for row in board:
        if all("^" in i for i in row):
            return True

    for column in zip(*board):
        if all("^" in i for i in column):
            return True
    return False


def unused(board):
    count = 0
    for row in board:
        for num in row:
            if "^" not in num:
                count += int(num)
    return count


part1and2()
