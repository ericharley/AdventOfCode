from collections import defaultdict
import re

filename = 'input.txt'
#filename = 'test.txt'

grid = [line for line in open(filename).read().splitlines()]

n = len(grid)

total = 0
for i in range(n):
  for match in re.finditer(r'\d+', grid[i]):

    def foo():
      for j in range(match.start(), match.end()):
        for dx in [-1,0,+1]:
          for dy in [-1,0,+1]:
            try:
              g = grid[i + dx][j + dy]
              if not g.isdigit() and g != '.':
                return  int(match.group())
            except IndexError:
              continue
      return 0
    
    total += foo()

print(total)

# Part 2
gears = defaultdict(lambda : [])

for i in range(n):
  for match in re.finditer(r'\d+', grid[i]):

    def foo():
      for j in range(match.start(), match.end()):
        for dx in [-1,0,+1]:
          for dy in [-1,0,+1]:
            try:
              if grid[i + dx][j + dy] == '*':
                return [(i + dx, j + dy), int(match.group())]
            except IndexError:
              continue
      return -1
    
    v = foo()
    if v != -1 :
      loc = v[0]
      val = v[1]
      
      gears[loc].append(val)

total = 0
for loc in gears:
  if len(gears[loc]) == 2:
    total += gears[loc][0]*gears[loc][1]
print(total)

