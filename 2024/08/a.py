from itertools import combinations

grid = open('input.txt').read().splitlines()

board  = {(r,c) : grid[r][c] for r,row in enumerate(grid) for c,col in enumerate(row)}
groups = {v : [k for k in board if board[k] == v] for v in board.values() if v != '.'}

# Part 1
antinodes = set()

for k in groups:
  for (x1,y1),(x2,y2) in combinations(groups[k], 2):
    dx,dy = x2-x1,y2-y1
    antinodes.add( (x1-dx,y1-dy) )
    antinodes.add( (x2+dx,y2+dy) )

print(len([a for a in antinodes if a in board]))

# Part 2
antinodes = set()

for k in groups:
  for (x1,y1),(x2,y2) in combinations(groups[k], 2):
    for (x3,y3) in board:
      if x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) == 0:
        antinodes.add((x3,y3))

print(len(antinodes))
