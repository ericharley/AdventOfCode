from collections import defaultdict

grid = open('input.txt').read().strip().split('\n')
rows,cols = len(grid),len(grid[0])
grid = {(r,c) for r in range(rows) for c in range(cols) if grid[r][c] != '.'}

dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def neighbors(x):
  r,c = x
  for dr,dc in dirs:
    yield r+dr,c+dc

# Part 1
n = defaultdict(int)
for r in range(rows):
 for c in range(cols):
   for dr,dc in dirs:
     n[r,c] += (r+dr,c+dc) in grid

T = sum([n[x]<4 for x in grid])
print(T)

# Part 2
T2 = 0
T2 += T

while T > 0:
 grid = {x for x in grid if n[x] >= 4}
 n = defaultdict(int)
 for r in range(rows):
  for c in range(cols):
    for dr,dc in dirs:
      n[r,c] += (r+dr,c+dc) in grid

 T = sum([n[x]<4 for x in grid])
 T2 += T

print(T2)