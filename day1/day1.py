import typing

with open("input") as f:
    array: typing.List[int] = [
        sum([int(num) for num in i.split("\n") if num != ""])
        for i in f.read().split("\n\n")
    ]

array.sort()
p1: int = array[-1]
p2: int = sum(array[-3:])

print("part 1:", p1)
print("part 2:", p2)
