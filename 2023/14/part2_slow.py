filename = 'input.txt'
for block in open(filename).read().split("\n\n"):
    grid = block.splitlines()

N = len(grid)
M = len(grid[0])

stones = set()
rocks = set()

for r in range(len(grid)):
  for c in range(len(grid[r])):
    if grid[r][c] == 'O':
       stones.add((r,c))

    if grid[r][c] == '#':
       rocks.add((r,c))

def print_grid():
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      if (r,c) in stones:
        print('O', end='')
      elif (r,c) in rocks:
        print('#', end='')
      else:
        print('.', end='')
    print()
  print()

def move_north():
  # go row by row from 0 to end
  # go column by column from 0 to end
  # if you have a stone then move it up as far as you can go
  for row in range(len(grid)):
    for r,c in [x for x in stones if x[0] == row]:
      stones.remove((r,c))
      new_r = r
      new_c = c
      while new_r > 0:
        if (new_r-1, new_c) in (stones | rocks):
          break
        else:
          new_r -= 1
      stones.add((new_r,new_c))

def move_south():
  # if you have a stone then move it down as far as you can go
  for row in range(N-1,0-1,-1):
    for r,c in [x for x in stones if x[0] == row]:
      stones.remove((r,c))
      new_r = r
      new_c = c
      while new_r < N-1:
        if (new_r+1, new_c) in (stones | rocks):
          break
        else:
          new_r += 1
      stones.add((new_r,new_c))

def move_west():
  # if you have a stone then move it left as far as you can go
  for col in range(M):
    for r,c in [x for x in stones if x[1] == col]:
      stones.remove((r,c))
      new_r = r
      new_c = c
      while new_c > 0:
        if (new_r, new_c-1) in (stones | rocks):
          break
        else:
          new_c -= 1
      stones.add((new_r,new_c))

def move_east():
  # if you have a stone then move it right as far as you can go
  for col in range(M-1,0-1,-1):
    for r,c in [x for x in stones if x[1] == col]:
      stones.remove((r,c))
      new_r = r
      new_c = c
      while new_c < M-1:
        if (new_r, new_c+1) in (stones | rocks):
          break
        else:
          new_c += 1
      stones.add((new_r,new_c))

def do_cycle():
  move_north()
  move_west()
  move_south()
  move_east()

def calc_load():
  total = 0
  for stone in stones:
    total += N - stone[0]
  return total

def fingerprint_field():
  return hash((frozenset(stones),frozenset(rocks)))

T = 1000000000
cycle_count = 0
seen = {}

while cycle_count < T:
 
  key = fingerprint_field()

  # we're at a place we have been before
  if key in seen:
    last_count = seen[key] # cycle count when we were here

    rem = T - cycle_count  # how many more do we have to go
    cycle_length = cycle_count - last_count
    rep = rem // cycle_length

    print('found cycle of length ',cycle_length,' at cycle ', cycle_count)

    cycle_count += rep*cycle_length # If we add these then we get to the same place, equiv to calling do_cycle
    break

  seen[key] = cycle_count
  print(cycle_count, key)
  do_cycle()
  cycle_count+=1


while cycle_count < T:
  do_cycle()
  cycle_count+=1


print(T)
print(cycle_count)
print(calc_load())
