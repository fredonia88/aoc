import requests

url = 'https://adventofcode.com/2024/day/6/input'
session = ''
res = requests.get(url=url, cookies={'session': session})

board = res.text.splitlines()

def get_guard_pos(board):
    for row_num, row_map in enumerate(board):
        guard_col = row_map.find('^')
        if guard_col != -1:
            return row_num, guard_col

def simulate(game_board, obstruction: tuple=None):

    board = game_board.copy()
    guard_row, guard_col = get_guard_pos(board)
    board[guard_row] = board[guard_row].replace('^', '.')
    
    if obstruction:
        new_row = board[obstruction[0]]
        board[obstruction[0]] = new_row[:obstruction[1]]+'#'+new_row[obstruction[1]+1:]
    
    board_len = len(board)
    board_width = len(board[0])
    moves = set()
    in_loop = False
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_idx = 0
    while True:
        new_guard_row = guard_row + directions[dir_idx][0]
        new_guard_col = guard_col + directions[dir_idx][1]
        move = (new_guard_row, new_guard_col, dir_idx,)
        if move in moves:
            in_loop = True
            break
        elif not (0 <= new_guard_row < board_len and 0 <= new_guard_col < board_width):
            break
        elif board[new_guard_row][new_guard_col] == '.':
            guard_row = new_guard_row
            guard_col = new_guard_col
            moves.add(move)
        else:
            dir_idx = (dir_idx + 1) % 4

    moves = set((move[0], move[1]) for move in moves)
    return moves, in_loop

# board = [
#     "....#.....",
#     ".........#",
#     "..........",
#     "..#.......",
#     ".......#..",
#     "..........",
#     ".#..^.....",
#     "........#.",
#     "#.........",
#     "......#..."
# ]

moves = simulate(board)
print('distinct positions visited:', len(moves[0]))

valid_obstructions = 0
guard_pos = get_guard_pos(board)
for move in moves[0]:
    if guard_pos == move:
        continue
    if simulate(board, move)[1]:
        valid_obstructions += 1

print('valid_obstructions found:', valid_obstructions)