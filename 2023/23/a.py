import random

grid = open('input.txt').read().splitlines()
N = len(grid)
M = len(grid[0])

max_len = 0

for _ in range (10**5):
  start = (0, 1)
  end = (N-1, M-2)

  current = start

  path = []
  visited = {}

  visited[current] = 1

  while current != end:

    (cr, cc) = current

    (nr,nc) = (-1,-1)

    if grid[cr][cc] == '^':  # must go up
      (nr, nc) = (cr-1, cc)
    elif grid[cr][cc] == 'v':  # must go down
      (nr, nc) = (cr+1, cc)
    elif grid[cr][cc] == '>':  # must go right
      (nr, nc) = (cr, cc+1)
    elif grid[cr][cc] == '<':  # must go left
      (nr, nc) = (cr-1, cc)

    if (nr,nc) != (-1,-1) and (nr,nc) in visited:
      break

    moves = [(cr-1, cc),(cr+1, cc),(cr, cc-1),(cr, cc+1)]
    moves = [(r,c) for (r,c) in moves if (0<=r<N and 0<=c<M) and grid[r][c] != '#' and (r,c) not in visited] 
    if moves:
      (nr, nc) = random.choice(moves)
    else:
      break

    path.append((nr,nc))
    visited[(nr,nc)] = 1
  
    current = (nr,nc)

  if current == end and max_len < len(path):
    max_len = max(max_len, len(path))
    print(max_len)

