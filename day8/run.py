"""
Advent of Code 2022 - Day 8
tildejustin, 8 Dec. 2022
"""

from time import perf_counter

with open("input", encoding="utf8") as file:
    forest = [[int(num) for num in line.strip()] for line in file.readlines()]

time1 = perf_counter()
part1 = 0
for index_y, current_strip in enumerate(forest):
    for index_x, current_tree in enumerate(current_strip):
        left = right = up = down = False
        # left
        for tree in current_strip[:index_x]:
            if tree >= current_tree:
                left = True
        # right
        for tree in current_strip[index_x + 1 :]:
            if tree >= current_tree:
                right = True
        # up
        for strip in forest[:index_y]:
            if strip[index_x] >= current_tree:
                up = True
        # down
        for strip in forest[index_y + 1 :]:
            if strip[index_x] >= current_tree:
                down = True
        if not left or not right or not up or not down:
            part1 += 1
time2 = perf_counter()

time3 = perf_counter()
part2 = 0
for index_y, current_strip in enumerate(forest):
    for index_x, current_tree in enumerate(current_strip):
        left = 0
        for tree in reversed(current_strip[:index_x]):
            if tree >= current_tree:
                left += 1
                break
            left += 1
        right = 0
        for tree in current_strip[index_x + 1 :]:
            if tree >= current_tree:
                right += 1
                break
            right += 1
        up = 0
        for strip in reversed(forest[:index_y]):
            if strip[index_x] >= current_tree:
                up += 1
                break
            up += 1
        down = 0
        for strip in forest[index_y + 1 :]:
            if strip[index_x] >= current_tree:
                down += 1
                break
            down += 1
        senic_score = up * down * right * left
        if senic_score > part2:
            part2 = senic_score
time4 = perf_counter()

print("Part 1:", part1)
print("Part 2:", part2)
print("Time one perf:", time2 - time1)
print("Time one perf:", time4 - time3)
