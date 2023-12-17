from collections import deque

filename = 'input.txt'

grid = open(filename).read().strip().splitlines()

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == "S":
            sr = r
            sc = c
            break
    else:
        continue
    break

loop = {(sr, sc)}
q = deque([(sr, sc)])

grid[sr] = grid[sr].replace('S','|',1)

def add_unless(r,c):
  if (r,c) not in loop:
    q.append((r,c))
    loop.add((r,c))

while q:
  r, c = q.popleft()
  ch = grid[r][c]

  # | is a vertical pipe connecting north and south.
  #r-1, c
  #r+1, c
  if ch == '|':
    add_unless(r-1,c)
    add_unless(r+1,c)

  # - is a horizontal pipe connecting east and west.
  #r, c-1
  #r, c+1
  if ch == '-':
    add_unless(r,c-1)
    add_unless(r,c+1)

  # L is a 90-degree bend connecting north and east.
  #r-1, c
  #r, c+1
  if ch == 'L':
    add_unless(r-1,c)
    add_unless(r,  c+1)

  # J is a 90-degree bend connecting north and west.
  #r, c-1
  #r-1, c
  if ch == 'J':
    add_unless(r,  c-1)
    add_unless(r-1,c)

  # 7 is a 90-degree bend connecting south and west.
  #r, c-1
  #r+1, c
  if ch == '7':
    add_unless(r,  c-1)
    add_unless(r+1,c)

  # F is a 90-degree bend connecting south and east.
  #r, c+1
  #r+1, c
  if ch == 'F':
    add_unless(r,  c+1)
    add_unless(r+1,c)

  # . is ground; there is no pipe in this tile.
  
  # S is the starting position of the animal

def is_inside(r,c):
  # outside := intersects edge an even number of times
  # inside := intersects edge an odd number of times
  if (r,c) in loop:
    return False

  intersections = 0
  for cp in range(c+1, len(grid[r])):
    if (r,cp) in loop and grid[r][cp] in '|LJ':
      intersections += 1

  if intersections % 2 == 1:
    return True

  return False


inside = 0
print(len(loop) // 2)  

for r in range(len(grid)):
 for c in range(len(grid[0])):
   inside += 1 if is_inside(r,c) else 0

print(inside)

def print_grid():
  count = 0
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if (r,c) in loop:
        print(grid[r][c], end='')
      elif is_inside(r,c):
        print('I', end='')
        count += 1
      else:
        print('O', end='')
    print()

#print_grid()
