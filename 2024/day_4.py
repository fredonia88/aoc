import requests
import re

url = 'https://adventofcode.com/2024/day/4/input'
session = '' # get from cookie
res = requests.get(url, cookies={'session': session})
res = res.text.splitlines()

# Part 1
def find_xmas(line):
    return len(re.findall(r'XMAS', line)) + len(re.findall(r'XMAS', line[::-1]))

# search horizontal
occurences = 0
for line in res:
    occurences += find_xmas(line)

# search vertical
for line in [''.join(row) for row in list(zip(*res))]:
    occurences += find_xmas(line)

# search diagonally, left to right
ltr_diag = {}
for r, row in enumerate(res):
    for c, val in enumerate(row):
        ltr_diag.setdefault(r-c, []).append(val)

for line in [val for _, val in ltr_diag.items()]:
    occurences += find_xmas(''.join(line))

# search diagonally, right to left
rtl_diag = {}
for r, row in enumerate(res):
    for c, val in enumerate(row):
        rtl_diag.setdefault(r+c, []).append(val)

for line in [val for _, val in rtl_diag.items()]:
    occurences += find_xmas(''.join(line))

print(occurences)


# Part 2
new_res = [list(row) for row in res]

occurences = 0
for r in range(len(new_res)):
    for c in range(len(new_res[r])):
        if new_res[r][c] == 'A':

            if r-1 < 0 or r+1 > 139:
                continue
            if c-1 < 0 or c+1 > 139:
                continue
            
            ltr = new_res[r-1][c-1] + 'A' + new_res[r+1][c+1]
            rtl = new_res[r-1][c+1] + 'A' + new_res[r+1][c-1]

            if ltr in ('MAS', 'SAM') and rtl in ('MAS', 'SAM'):
                occurences += 1

print(occurences)
