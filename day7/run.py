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


with open("example.txt") as f:
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

# print(list(all_paths))
# [print(f.get_string_path()) for f in files]

for path in all_paths:
    filtered_files = list(filter(lambda f: f.get_string_path().startswith(path), files))
    print(sum([file.get_size() for file in filtered_files]), path)
    file_sizes = [file.get_size() for file in filtered_files]
    sum_of_dir = sum(file_sizes)
    # print(filtered_files, path)

# sum_dir = [file_sizes_per_dir for file_sizes_per_dir in [file_sizes_per_dir for path in all_paths]]
