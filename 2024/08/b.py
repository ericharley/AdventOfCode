from itertools import combinations

grid = open('input.txt').read().splitlines()
board  = {complex(r,c) : ch for r,row in enumerate(grid) for c,ch in enumerate(row) }
groups = {v : [k for k in board if board[k] == v] for v in board.values() if v!='.' }

# Part 1
antinodes, antinodes_2 = set(), set()

for freq in groups:
  for z1,z2 in combinations(groups[freq], 2):
    d = z2 - z1
    antinodes   |= {z1 - d, z2 + d} & set(board)
    antinodes_2 |= {z3 for z3 in board if ((z1-z2).conjugate()*(z2-z3)).imag == 0}

print( len(antinodes) )
print( len(antinodes_2) )
