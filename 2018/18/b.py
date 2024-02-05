from collections import defaultdict

grid = open('input.txt').read().strip().splitlines()
N = len(grid)
trees = set()
lumbers = set()

for r,row in enumerate(grid):
  for c,col in enumerate(row):
    if col == '#':
      lumbers.add((r,c))
    if col == '|':
      trees.add((r,c))

def neighbors(r,c):
  for dr in [-1,0,+1]:
    for dc in [-1,0,+1]:
      nr = r + dr
      nc = c + dc
      if 0 <= nr < N and 0 <= nc < N:
        if not (nr == r and nc == c):
          yield nr,nc

def iterate(trees,lumbers):
  c_trees = defaultdict(int)
  for r,c in trees:
    for nr,nc in neighbors(r,c):
      c_trees[nr,nc] += 1

  c_lumbers = defaultdict(int)
  for r,c in lumbers:
    for nr,nc in neighbors(r,c):
      c_lumbers[nr,nc] += 1

  n_trees = set()
  n_lumbers = set()
 
  for r,c in trees:
    if c_lumbers[r,c] >= 3:
      n_lumbers.add((r,c))
    else:
      n_trees.add((r,c))

  for r,c in lumbers:
    if c_lumbers[r,c] >= 1 and c_trees[r,c] >= 1:
      n_lumbers.add((r,c))

  for r,c in c_trees:
    if c_trees[r,c] >= 3:
      if not (((r,c) in trees) or ((r,c) in lumbers)):
        n_trees.add((r,c))

  return n_trees,n_lumbers

def resource_value(trees, lumbers):
  return len(trees) * len(lumbers)

num_it = 1_000_000_000
cycle_len = 28
cycle_start = 575
if num_it >= cycle_start:
  num_it = cycle_start + ((num_it - cycle_start) % cycle_len)

for i in range(1, num_it + 1):
  trees,lumbers = iterate(trees,lumbers)

  # Part 1
  if i == 10:
    print(resource_value(trees,lumbers))

print(resource_value(trees,lumbers))
