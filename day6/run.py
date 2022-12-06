chars = open("input").read().strip() 

for i in range(len(chars) - 4):
    if len(set(chars[i:i + 4])) == 4:
        print("p1:", i + 4)
        break

for i in range(len(chars) - 14):
    if len(set(chars[i:i + 14])) == 14:
        print("p2:", i + 14)
        break