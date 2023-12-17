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

#print_grid()

# go row by row from 0 to end
# go column by column from 0 to end
# if you have a stone then move it up as far as you can go
#for r in range(len(grid)):
#  for c in range(len(grid[r])):
#    if (r,c) in stones:
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

#for stone in rounds:
#  s_r = stone[0]
#  s_c = stone[1]
#
#  [x for x in rounds if x[1]==s_c]

#print_grid()

total = 0
for stone in stones:
  total += N - stone[0]
print(total)

