import typing

with open("input", "r", encoding="utf8") as file:
    file_lines: typing.List[str] = file.readlines()

priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

count: int = 0
for line in file_lines:
    half_line_len: int = int(len(line)/2)
    set1: set = set(line[:half_line_len])
    set2: set = set(line[half_line_len:])
    common_letter = "".join(set1.intersection(set2))
    # print(priorities.index(common_letter)+1)
    count += priorities.index(common_letter)+1

print("count is", count)
print(priorities.index("Z")+1)