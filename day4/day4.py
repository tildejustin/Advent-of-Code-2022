with open("input") as file:
    lines = file.readlines()

# look and weep
# how tf does this work?
parts = [[[int(num) for num in dashed_string.split("-")] for dashed_string in line.split(",")] for line in lines]
print(parts)
# parts[0] = [int(num) for num in parts[0].split("-")]
# parts[1] = [int(num) for num in parts[1].split("-")]


p1 = 0
for part in parts:
    if (part[0][0] <= part[1][0] and part[0][1] >= part[1][1]) or (part[1][0] <= part[0][0] and part[1][1] >= part[0][1]):
        p1 += 1

p2 = 0
for part in parts:
    # reverted to my primal ways with sets, couldn't quickly intuit the answer with basic checking like I was doing with part 1
    # https://www.youtube.com/watch?v=TKxINN7bNmw explains how it should have been done :/
    if len(set(range(part[0][0], part[0][1]+1)).intersection(set(range(part[1][0], part[1][1]+1)))) > 0:
        p2 += 1

print("part 1 ans is", p1)
print("part 2 ans is", p2)