import copy
from functools import reduce


def contains_number(string):
    return any(char.isdigit() for char in string)


class File:
    def __init__(self, fpath: list, fname, fsize):
        self.fpath = fpath
        self.fsize = fsize
        self.fname = fname

    def get_size(self):
        return int(self.fsize)

    def get_path(self):
        return self.fpath

    def get_string_path(self):
        return "/" + "/".join(self.fpath[1:])


with open("input") as f:
    lines: list = f.readlines()
    current_path = []
    files = []
    for line in lines:
        if "$ cd " in line:
            if ".." in line:
                current_path.pop()
                continue
            line.strip()
            current_path.append(line.split()[2])
        elif contains_number(line):
            attributes = line.split()
            files.append(File(copy.deepcopy(current_path), attributes[1], attributes[0]))


all_paths = set()
for file_path in [file.get_string_path() for file in files]:
    all_paths.add(file_path)

# generate inner paths for empty directories
all_paths_copy = copy.deepcopy(all_paths)
for path in all_paths_copy:
    for i in range(1, len(path.split("/"))):
        all_paths.add("/" +  "/".join(path.split("/")[1:i]))

dir_sizes = [sum([file.get_size() for file in filter(lambda f: f.get_string_path().startswith(path), files)]) for path in all_paths]

dir_sizes_two = copy.deepcopy(dir_sizes)

dir_sizes = [dir_size for dir_size in dir_sizes if dir_size <= 100000]
print("part 1:", sum(dir_sizes))

# part 2
# too lazy to write real code
root_size = USED_SPACE = max(dir_sizes_two)
SPACE = 70000000
UNUSED_SPACE  = SPACE - USED_SPACE
NEED_EMPTY = 30000000
NEED = NEED_EMPTY - UNUSED_SPACE

dir_sizes_two = [dir_size for dir_size in dir_sizes_two if dir_size >= NEED]
dir_sizes_two.sort()
print("part 2:", dir_sizes_two[0])