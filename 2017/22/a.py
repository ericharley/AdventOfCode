from collections import defaultdict
from copy import copy

lines = open('input.txt').read().strip().splitlines()

init_grid = defaultdict(lambda : '.')
for r,row in enumerate(lines):
  for c,ch in enumerate(row):
    if ch == '#':
      init_grid[c - 1j*r] = '#'

N = len(lines)

CENTER = N//2 - N//2*1j

UP = 1j
RIGHT = -1j
LEFT  = 1j
STRAIGHT = 1
REVERSE = -1

def doit(rule,k):
  grid = copy(init_grid)
  pos = CENTER
  heading = UP
  count = 0

  for _ in range(k):
    grid[pos],dh,dc = rule[grid[pos]]
    heading *= dh
    count += dc
    pos += heading

  return count

# Part 1
rule = {'.':('#',LEFT,1), '#':('.',RIGHT,0)}
print(doit(rule,10000))

# Part 2
rule = {'.':('w',LEFT,0), 'w':('#',STRAIGHT,1), '#':('f',RIGHT,0), 'f':('.',REVERSE,0)}
print(doit(rule,10000000))
