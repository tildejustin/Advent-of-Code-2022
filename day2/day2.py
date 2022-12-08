import typing

with open("input", "r", encoding="utf8") as file:
    text = file.readlines()

ROCK: int = 1
PAPER: int = 2
SCISSOR: int = 3

LOSE_CONDITION: int = 1
DRAW_CONDITION: int = 2
WIN_CONDITION: int = 3

DRAW: int = 3
WIN: int = 6


def substitute(line: str) -> typing.List[int]:
    line = (
        line.replace("A", "1")
        .replace("X", "1")
        .replace("B", "2")
        .replace("Y", "2")
        .replace("C", "3")
        .replace("Z", "3")
        .strip()
    )
    line_list = [int(line[0]), int(line[2])]
    # print(line)
    return line_list


text: typing.List[int] = [i.strip() for i in text]
text = list(map(substitute, text))

p1: int = 0
for item in text:
    one = item[0]
    two = item[1]
    p1 += two
    if one == two:
        p1 += DRAW
    elif one == ROCK and two == PAPER:
        p1 += WIN
    elif one == PAPER and two == SCISSOR:
        p1 += WIN
    elif one == SCISSOR and two == ROCK:
        p1 += WIN

p2: int = 0
for item in text:
    one = item[0]
    two = item[1]
    # I don't understand that modulus stuff
    if two == LOSE_CONDITION:
        if one == ROCK:
            p2 += SCISSOR
        if one == PAPER:
            p2 += ROCK
        if one == SCISSOR:
            p2 += PAPER
    if two == DRAW_CONDITION:
        p2 += one
        p2 += DRAW
    if two == WIN_CONDITION:
        if one == ROCK:
            p2 += PAPER
        elif one == PAPER:
            p2 += SCISSOR
        elif one == SCISSOR:
            p2 += ROCK
        p2 += WIN

print("part 1 is", p1)
print("part 2 is", p2)
