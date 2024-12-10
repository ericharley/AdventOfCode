from collections import defaultdict

grid = open('input.txt').read().strip().split('\n')

seats = defaultdict(int)

for r in range(len(grid)):
 for c in range(len(grid[0])):
   if grid[r][c] == 'L':
     seats[(r,c)] = 0

num_steps = 1000

def p():
 for r in range(len(grid)):
  for c in range(len(grid[0])):
    if grid[r][c] == 'L' and seats[(r,c)] == 0:
      print('L',end='')
    if grid[r][c] == 'L' and seats[(r,c)] == 1:
      print('#',end='')
    if grid[r][c] == '.':
      print('.',end='')
  print()
 print()

def neighbors(r,c):
  for dr in [-1,0,+1]:
    for dc in [-1,0,+1]:
      if (r+dr,c+dc) != (r,c):
        if 0 <= r+dr < len(grid) and 0 <= c+dc < len(grid[0]):
          yield (r+dr,c+dc)

for i in range(num_steps):
  ct = defaultdict(int)
  for r,c in seats:
    for nr,nc in neighbors(r,c):
      ct[nr,nc] += seats[(r,c)]
        
  new_seats = {}
  
  for seat in seats:
    if seats[seat] == 0 and ct[seat] == 0:
      new_seats[seat] = 1
    elif seats[seat] == 1 and ct[seat] >= 4:
      new_seats[seat] = 0
    else:
      new_seats[seat] = seats[seat]

  seats = new_seats

print(sum([seats[seat] for seat in seats]))
#print(len(seats))
