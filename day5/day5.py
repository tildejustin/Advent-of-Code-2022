import copy, typing

# read each part of the instructions into a 2d list [[1,2,4],[3,2,6],[2,3,5]...]
commands: typing.List[list] = []
for line in open("input").readlines()[10:]:
    l: typing.List[str] = line.split(" ")
    a: typing.List[int] = [int(l[1]), int(l[3]), int(l[5])]
    commands.append(a)

# read board into a list of lists used as fifo queues
board: typing.List[list] = [[] for i in range(9)]
for line in open("input").readlines()[:8]:
    nums: typing.List[int] = [num for num in range(35) if num % 4 == 1]
    # print([line[index] for index in nums])
    for i, j in enumerate(nums):
        if line[j] != " ":
            board[i].insert(0,line[j])

# board for each part
# FUCK YOU SHALLOW COPY
board2 = copy.deepcopy(board)
print(board, "\n")

# part 1
for x,y,z in commands:
    for i in range(x):
        board[z - 1].append(board[y - 1].pop())
p1 = "".join([line[len(line)-1] for line in board])

# part 2
for x,y,z in commands:
    # print(x, board2[y - 1][-x:], "from", board2[y-1], "to", board2[z-1])
    board2[z - 1].extend(board2[y - 1][-x:])
    board2[y - 1] = board2[y - 1][:-x]
    # print("result", board2[y-1], board2[z-1])
p2 = "".join([line[len(line)-1] for line in board2])

# print board vertically
def printboard(board: typing.List[list]) -> None:
    largest = max(list(map(len, board)))
    for i in range(largest - 1, - 1, -1):
        for array in board:
            try:
                print(array[i] , end="")
            except IndexError:
                print(" ", end="")
            print(" ", end="")
        print()
    print()


printboard(board)
printboard(board2)


print("part 1:", p1)
print("part 2:", p2)