from collections import defaultdict

grid = open('input.txt').read().strip().split('\n')

# Part 1
def groups(data, func):
  grouping = defaultdict(str)
  for y in range(len(data)):
    for x in range(len(data[y])):
      grouping[func(x, y)] += data[y][x]
  return list(map(grouping.get, sorted(grouping)))

data = groups(grid, lambda x, y: x) \
     + groups(grid, lambda x, y: y) \
     + groups(grid, lambda x, y: x + y) \
     + groups(grid, lambda x, y: x - y)

print( sum([x.count('XMAS')+x.count('SAMX') for x in data]) )

# Part 2
t = 0
for r in range(1,len(grid)-1):
  for c in range(1,len(grid[0])-1):
    s = grid[r][c] + grid[r-1][c-1] + grid[r-1][c+1] + grid[r+1][c-1] + grid[r+1][c+1]
    if s in ['AMSMS','ASMSM','AMMSS','ASSMM']:
      t += 1

print(t)
