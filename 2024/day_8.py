import requests

url = 'https://adventofcode.com/2024/day/8/input'
session = ''
response = requests.get(url, cookies={'session': session})
grid = response.text.splitlines()

antennas = {}
for row_idx, row in enumerate(grid):
    for col in range(len(row)):
        cell = row[col]
        if cell != '.':
            loc = antennas.get(cell, [])
            loc.append((row_idx, col,))
            antennas[cell] = loc

grid_len = len(grid)
grid_width = len(grid[0])

antinodes = set()
for antenna, locations in antennas.items():
    
    locs = locations.copy()
    while len(locs) > 1:
        for n in range(1, len(locs)):
            l1, l2 = locs[0], locs[n]

            row_diff = l2[0] - l1[0]
            col_diff = l2[1] - l1[1]

            new_l1 = (l1[0] - row_diff, l1[1] - col_diff)
            new_l2 = (l2[0] + row_diff, l2[1] + col_diff)

            if 0 <= new_l1[0] < grid_len and 0 <= new_l1[1] < grid_width:
                antinodes.add(new_l1)
            if 0 <= new_l2[0] < grid_len and 0 <= new_l2[1] < grid_width:
                antinodes.add(new_l2)
        
        locs.pop(0)
print('Part 1 antinode count:', len(antinodes))

antinodes = set()
for antenna, locations in antennas.items():
    
    for location in locations:
        antinodes.add(location)
        
    locs = locations.copy()
    while len(locs) > 1:
        for n in range(1, len(locs)):
            l1, l2 = locs[0], locs[n]

            row_diff = l2[0] - l1[0]
            col_diff = l2[1] - l1[1]

            multiplier = 1
            l1_offgrid = False
            l2_offgrid = False
            while not l1_offgrid or not l2_offgrid:
                new_l1 = (l1[0] - (row_diff * multiplier), (l1[1] - (col_diff * multiplier)))
                new_l2 = (l2[0] + (row_diff * multiplier), l2[1] + (col_diff * multiplier))
                if 0 <= new_l1[0] < grid_len and 0 <= new_l1[1] < grid_width:
                    antinodes.add(new_l1)
                else:
                    l1_offgrid = True
                if 0 <= new_l2[0] < grid_len and 0 <= new_l2[1] < grid_width:
                    antinodes.add(new_l2)
                else:
                    l2_offgrid = True
                
                multiplier += 1
        
        locs.pop(0)
print('Part 2 antinode count:', len(antinodes))