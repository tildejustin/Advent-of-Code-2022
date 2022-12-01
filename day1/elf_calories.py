with open("input", "r", encoding="utf8") as file:
    text = file.readlines()

counter: int = 0
array: list = [[]]
for number in text:
    if number == "\n":
        array.append([])
    else:
        # always adds to the latest array
        array[len(array) - 1].append(int(number))


sum_array: list = list(map(sum, array))
print(max(sum_array))

# part 2
sum_array.sort()
print(sum(sum_array[-3:]))
