with open('inputs/day_1.txt', 'r') as file:
    leftcol = []
    rightcol = []
    for line in file:
        leftcol.append(int(line[:5]))
        rightcol.append(int(line[8:13]))

leftcol.sort()
rightcol.sort()

distance = 0
for i in range(0, 1000):
    distance += abs(leftcol[i] - rightcol[i])

print(distance)