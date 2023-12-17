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

#print(grid)

def add_unless(r,c):
  if (r,c) not in loop:
    q.append((r,c))
    loop.add((r,c))

while q:
  r, c = q.popleft()
  ch = grid[r][c]

#  if ch == 'S':
#    # is it a '|' ?
#    #  (r-1,c) top
#    #  (r+1,c) bottom
#    if grid[r-1][c] in '|7F' and grid[r+1][c] in '|LJ':
#      add_unless(r-1,c)
#      add_unless(r+1,c)
#      break
#
#    # is it a '-' ?
#    #  (r,c-1) left
#    #  (r,c+1) right
#    if grid[r][c-1] in '-LF' and grid[r][c+1] in '-J7':
#      add_unless(r,c-1)
#      add_unless(r,c+1)
#      break
#
#    # is it a 'L' ?
#    #  (r-1,c) left
#    #  (r,c+1) right
#
#    # is it a 'J' ?
#    # is it a '7' ?
#    # is it a 'F' ?
#
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

print(len(loop) // 2)  
