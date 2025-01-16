with open('inputs/day_1.txt', 'r') as file:
    leftcol = []
    rightcol = []
    for line in file:
        leftcol.append(int(line[:5]))
        rightcol.append(int(line[8:13]))

leftcol.sort()
rightcol.sort()

# part 1: calculate distance
distance = 0
for i in range(0, 1000):
    distance += abs(leftcol[i] - rightcol[i])
print('distance between lists:', distance)

# part 2: calculate similarity
leftcol = list(set(leftcol))
leftdict = {col: 0 for col in leftcol}
for n in leftdict.keys():
    for i in rightcol:
        if i > n:
            break
        else:
            if i == n:
                leftdict[n] += 1
val = 0
for k, v in leftdict.items():
    val += k * v

print('similarity score:', val)