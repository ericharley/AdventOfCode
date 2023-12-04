from collections import defaultdict
import re

filename = 'input.txt'
#filename = 'test.txt'

grid = [line for line in open(filename).read().splitlines()]

n = len(grid)

# add padding 
for i in range(n):
  grid[i] = '.' + grid[i] + '.'
grid.insert(0, n*'.')
grid.append(n*'.')

total = 0
for r in range(1, n+1):
  for match in re.finditer(r'\d+', grid[r]):
    a = match.start()
    b = match.end()
    val = int(match.group())

    s = grid[r-1][a-1:b+1] + grid[r][a-1:b+1] + grid[r+1][a-1:b+1]
    l = [x for x in s if x != '.' and not x.isdigit()]
    if len(l) > 0:
       total += val

print(total)

