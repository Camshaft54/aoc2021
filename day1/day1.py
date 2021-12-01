file = open('../day1/input.txt', 'r').read()
nums = list(map(int, file.split("\n")))


def part1():
    c = 0
    for i in range(1, len(nums)):
        if int(nums[i]) > int(nums[i - 1]):
            print("increase from " + str(nums[i - 1]) + " to " + str(nums[i]))
            c += 1
    print(c)


def part2():
    c = 0
    sliding = [nums[n] + nums[n + 1] + nums[n + 2] for n in range(len(nums) - 2)]
    for i in range(len(sliding)):
        if sliding[i - 1] < sliding[i]:
            c += 1
    print(c)

part1()
part2()
