import typing

with open("input", "r", encoding="utf8") as file:
    text = file.readlines()

ROCK: int = 1
PAPER: int = 2
SCISSOR: int = 3

DRAW: int = 3
WIN: int = 6


def substitute(line: str) -> typing.List[int]:
    # print(line)
    line = line.replace("A", "1")
    line = line.replace("X", "1")
    line = line.replace("B", "2")
    line = line.replace("Y", "2")
    line = line.replace("C", "3")
    line = line.replace("Z", "3")
    line = line.strip()
    line_list = [int(line[0]), int(line[2])]
    # print(line)
    return line_list


count: int = 0
for line in text:
    numbers: str = substitute(line)
    one = numbers[0]
    two = numbers[1]
    count += two
    if one == two:
        count += DRAW
    elif one == ROCK and two == PAPER:
        count += WIN
    elif one == PAPER and two == SCISSOR:
        count += WIN
    elif one == SCISSOR and two == ROCK:
        count += WIN

print("Count is", count)
