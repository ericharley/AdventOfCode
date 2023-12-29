import sys

sys.setrecursionlimit(10000)

grid = open('input.txt').read().splitlines()
N = len(grid)
M = len(grid[0])

max_len = 0

moves = {}
for r in range(N):
  for c in range(M):
    m = [(r-1, c),(r+1, c),(r, c-1),(r, c+1)]
    m = [(r,c) for (r,c) in m if (0<=r<N and 0<=c<M) and grid[r][c] != '#']
    moves[(r,c)] = set(m)

start = (0, 1)
end = (N-1, M-2)

def f(start, end, path, visited):
  if start == end:
    return 0

  else:
    ct = 1
    while True:
      mvs = [(r,c) for (r,c) in moves[start] if (r,c) not in visited]
      if len(mvs) == 1:
        start = mvs[0]
        ct += 1
        path.append(start)
        visited.add(start)
      else:
        break
    ds = [ f(nxt, end, path + [nxt], set(visited)) for nxt in mvs]

    if ds:
      return ct + max(ds)
    else:
      return -10000

print(f(start, end, [], set()))
