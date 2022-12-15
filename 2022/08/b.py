filename = 'input.txt'

grid = [list(map(int, line)) for line in open(filename).read().splitlines()]

def is_visible(r,c) :
  # A tree is visible if all of the other trees
  # between it and an edge of the grid are 
  # shorter than it

  k = grid[r][c]

  left   = [ grid[r][x] for x in range(c) ]
  right  = [ grid[r][x] for x in range(c + 1, len(grid[r])) ]
  top    = [ grid[x][c] for x in range(r) ]
  bottom = [ grid[x][c] for x in range(r + 1, len(grid)) ]

  return ( all(t < k for t in left) or all(t < k for t in right) or all(t < k for t in top) or all(t < k for t in bottom) )

def scenic_score(r,c):
  k = grid[r][c]
  left   = [ grid[r][x] for x in range(c) ]
  right  = [ grid[r][x] for x in range(c + 1, len(grid[r])) ]
  top    = [ grid[x][c] for x in range(r) ]
  bottom = [ grid[x][c] for x in range(r + 1, len(grid)) ]
  L = R = T = B = 0

  for x in top[::-1]:
    T += 1
    if x >= k:
      break
  for x in left[::-1]:
    L += 1
    if x >= k:
      break
  for x in right:
    R += 1
    if x >= k:
      break
  for x in bottom:
    B += 1
    if x >= k:
      break

  return(T*L*B*R)

t = 0
ss = 0

for r in range(len(grid)):
  for c in range(len(grid[r])):
    if is_visible(r,c) :
      t += 1
    ss = max(ss, scenic_score(r,c))
    

print(t)
print(ss)
