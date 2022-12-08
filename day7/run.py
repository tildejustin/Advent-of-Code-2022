"""
Advent of Code, day 7
tildejustin, 7 Dec. 2022
"""

import typing
from copy import deepcopy


def contains_number(string: str) -> bool:
    """Returns true if any digit of a string is a number, otherwise returns false"""
    return any(char.isdigit() for char in string)


class File:
    """
    Represents a file, with a path, size, and name.
    This isn't necessary for the challenge, I just need class practice

    fields:
        fpath: an array of the path to the file, seperated into individual directories. Starts at /.
        fsize: a (str) representation of the size of the file.
        fname: the file name of the file.

    methods:
        *: take no arguents
        get_size: returns int of the file's size
        get_path: returns path as array
    """

    def __init__(self, fpath: typing.List[str], fname: str, fsize: str):
        self.file_path = fpath
        self.file_size = fsize
        self.file_name = fname

    def get_size(self) -> int:
        return int(self.file_size)

    def get_path(self):
        return self.file_path

    def get_string_path(self):
        return "/" + "/".join(self.file_path[1:])


with open("input", "r", encoding="utf8") as file:
    lines: typing.List[str] = file.readlines()
    current_path: typing.List[str] = []
    files: typing.List[File] = []
    for line in lines:
        # if the line has do to with the directory
        if "$ cd " in line:
            # if we're going back a directory, no need to create a new one
            if ".." in line:
                current_path.pop()
                continue
            # otherwise, add new folder to current path
            current_path.append(line.split()[2])
        # if not a directory, make a new file object
        # this code would be better if it was centered around directories containing file objects
        # instead of files containing their own directories, but oh well
        elif contains_number(line):
            attributes: typing.List[str] = line.split()
            files.append(File(deepcopy(current_path), attributes[1], attributes[0]))


# get every unique path by looping through *every* file.
# again, terrible design
all_paths: set = set()
for file_path in [file.get_string_path() for file in files]:
    all_paths.add(file_path)


# generate inner paths for empty directories
# need copy because i'm mutating all_paths, should just make another variable but whatever
all_paths_copy = deepcopy(all_paths)
for path in all_paths_copy:
    # I couldn't figure out how to do this without range len
    for i in range(1, len(path.split("/"))):
        all_paths.add("/" + "/".join(path.split("/")[1:i]))


# gets the size of every directory (in all_paths) by checking every file against every path
# to see if the path in the file starts with the path in all_paths. I realize how bad this sounds.
dir_sizes: typing.List[int] = [
    sum(
        # list of every size of file that contains that path
        [
            file.get_size()
            for file in filter(lambda f: f.get_string_path().startswith(path), files)
        ]
    )
    # done for every path
    # was a dictionary with path but that was too annoying and not needed anyways
    for path in all_paths
]
dir_sizes_two = dir_sizes


# part 1  solution
dir_sizes = [dir_size for dir_size in dir_sizes if dir_size <= 100000]
print("part 1:", sum(dir_sizes))


# part 2
# too lazy to write real code
root_size = USED_SPACE = max(dir_sizes_two)
SPACE = 70000000
UNUSED_SPACE = SPACE - USED_SPACE
NEED_EMPTY = 30000000
NEED = NEED_EMPTY - UNUSED_SPACE


dir_sizes_two = [dir_size for dir_size in dir_sizes_two if dir_size >= NEED]
dir_sizes_two.sort()
print("part 2:", dir_sizes_two[0])
