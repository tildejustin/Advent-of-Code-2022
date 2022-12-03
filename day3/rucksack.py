import typing

with open("input", "r", encoding="utf8") as file:
    file_lines: typing.List[str] = file.readlines()

file_lines = [line.strip() for line in file_lines]

priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# part 1
# count: int = 0
# for line in file_lines:
#     half_line_len: int = int(len(line)/2)
#     set1: set = set(line[:half_line_len])
#     set2: set = set(line[half_line_len:])
#     common_letter: str = "".join(set1.intersection(set2))
#     count += priorities.index(common_letter)+1

# part 2
count: int = 0
for i in range(0, len(file_lines), 3):
    inventory: typing.List[set] = [set(line) for line in file_lines[i:i+3]]
    # there has got to be a better way to do this
    common_letter: str = "".join(inventory[0].intersection(inventory[1].intersection(inventory[2])))
    count += priorities.index(common_letter)+1

print("count is", count)