import requests
import re

url = 'https://adventofcode.com/2024/day/3/input'
session = '' # extract from cookie

res = requests.get(url=url, cookies={'session': session})

### Part 1
memory = res.text.splitlines()
product = 0
for section in memory:
    searching = True
    while searching:
        match = re.search(r'mul\(\d{1,3},\d{1,3}\)', section)
        if match:
            mul = section[match.start()+4:match.end()-1]
            x, y = map(int, mul.split(','))
            product += x * y
            section = section[match.end():]
        else:
            searching = False

print(product)


### Part 2
pattern = re.compile(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)")

def process(memory):
    product = 0
    do = True
    
    for section in memory:
        for match in pattern.finditer(section):
            token = match.group()
            print(token)
            
            if token == "do()":
                do = True
            elif token == "don't()":
                do = False
            else: 
                if do:
                    x, y = map(int, token[4:-1].split(","))
                    product += x * y
                    
    return product

memory = res.text.splitlines()
print(process(memory))
