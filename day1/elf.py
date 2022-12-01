with open("input.txt", "r", encoding="utf8") as file:
    text = file.readlines()

counter = 0
array = [[]]
for number in text:
    if number == "\n":
        array.append([])
    else:
        array[len(array) - 1].append(int(number))


sum_array = list(map(sum, array))
print(max(sum_array))

# part 2
sum_array.sort()
print(sum(sum_array[-3:]))
