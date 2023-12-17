filename = 'input.txt'

def find_mirror(grid):
  # find horizontal
  for r in range(1,len(grid)):
    top = grid[:r]
    bottom = grid[r:]
    d = min(len(top),len(bottom))

    if top[::-1][:d] == bottom[:d]:
      return r

  return 0

# part 2
def smudged(grid, num_diff):
  # find horizontal
  for r in range(1,len(grid)):
    top = grid[:r]
    bottom = grid[r:]
    d = min(len(top),len(bottom))

    T = top[::-1][:d]
    B = bottom[:d]
    # see if they match except in exactly one place
    A = T
    differences = sum(a!=b for x,y in zip(T, B) for a,b in zip(x,y))
#    differences = 0
#    for i in range(len(T)):
#      for j in range(len(T[i])):
#        if T[i][j] != B[i][j]:
#          differences += 1
    if differences == num_diff:
      return r

  return 0

total = 0
for block in open(filename).read().split("\n\n"):
    grid = block.splitlines()
 
    # find a mirrorable row
    row = find_mirror(grid)
    total += row*100

    # find a mirrable column by finding the row in the flipped grid
    flipped_grid = list(map(lambda x : ''.join(x), list(zip(*grid))))
    col = find_mirror(flipped_grid)
    total += col

print(total)


total = 0
for block in open(filename).read().split("\n\n"):
    grid = block.splitlines()
 
    # find a mirrorable row
    total += smudged(grid, 1)*100

    # find a mirrable column by finding the row in the flipped grid
    flipped_grid = list(map(lambda x : ''.join(x), list(zip(*grid))))
    total += smudged(flipped_grid, 1)

print(total)


