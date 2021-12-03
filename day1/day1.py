file = open('i', 'r').read()
nums = list(map(int, file.split("\n")))


def part1():
    c = 0
    for i in range(1, len(nums)):
        if int(nums[i]) > int(nums[i - 1]):
            c += 1
    print(c)


# def part1_short():
#     s=open('i').readlines();print(sum([1if int(s[i-1])<int(a)else 0for i,a in enumerate(s)]))


def part2():
    c = 0
    windows = [nums[i] + nums[i + 1] + nums[i + 2] for i in range(len(nums) - 2)]
    for i in range(len(windows)):
        if windows[i - 1] < windows[i]:
            c += 1
    print(c)


print("Part 1:")
part1()
# part1_short()
print("Part 2:")
part2()
