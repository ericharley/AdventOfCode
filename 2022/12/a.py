grid = [list(x) for x in open(0).read().strip().splitlines()]

for r, row in enumerate(grid):
    for c, item in enumerate(row):
        if item == "S":
            sr = r
            sc = c
            grid[r][c] = "a"
        if item == "E":
            er = r
            ec = c
            grid[r][c] = "z"

from collections import deque

queue = deque()
queue.append((0, sr, sc))

visited = {(sr, sc)}
while queue: 
    dist, r, c = queue.popleft()
    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
            continue
        if (nr, nc) in visited:
            continue
        if ord(grid[nr][nc]) - ord(grid[r][c]) > 1:
            continue
        if nr == er and nc == ec:
            print(dist + 1)
            exit(0)
        visited.add((nr,nc))
        queue.append((dist+1,nr,nc))
  
