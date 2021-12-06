import os

# file = open('test.txt').read()
file = open("input.txt").read()
fishes = file.split(",")


def calculateFish(n):
    fish = [int(fishes.count(str(d))) for d in range(9)]
    for i in range(n):
        fish.append(fish.pop(0))
        fish[6] += fish[8]
    return sum(fish)


print(f"Part 1: {calculateFish(80)} Part 2: {calculateFish(256)}")
