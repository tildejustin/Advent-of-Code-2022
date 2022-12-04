import string, typing

file_lines: typing.List[str] = [line.strip() for line in open("input").readlines()]

p1: int = 0
for line in file_lines:
    half_line_len: int = len(line)//2
    set1: set = set(line[:half_line_len])
    set2: set = set(line[half_line_len:])
    common_letter: str = "".join(set1.intersection(set2))
    p1 += string.ascii_letters.index(common_letter)+1

# part 2
p2: int = 0
for i in range(0, len(file_lines), 3):
    inventory: typing.List[set] = [set(line) for line in file_lines[i:i+3]]
    # there has got to be a better way to do this
    common_letter: str = "".join(set.intersection(*inventory))
    p2 += string.ascii_letters.index(common_letter)+1

print("count is", p1, p2)