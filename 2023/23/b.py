import random

grid = open('input.txt').read().splitlines()
N = len(grid)
M = len(grid[0])

max_len = 0

for i in range (10**7):
  start = (0, 1)
  end = (N-1, M-2)

  current = start

  path = []
  visited = {}

  visited[current] = 1

  while current != end:

    (cr, cc) = current

    moves = [(cr-1, cc),(cr+1, cc),(cr, cc-1),(cr, cc+1)]
    moves = [(r,c) for (r,c) in moves if (0<=r<N and 0<=c<M) and grid[r][c] != '#' and (r,c) not in visited]
    if moves:
      if len(moves) == 1:
        (nr, nc) = moves[0]
      else:
        (nr, nc) = random.choice(moves)
    else:
      break

    current = (nr,nc)
    path.append((nr,nc))
    visited[(nr,nc)] = 1

  if current == end and max_len < len(path):
    max_len = max(max_len, len(path))
    #print(path)
    print(max_len)

