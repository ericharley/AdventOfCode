f = open("input.txt","r")
lines = f.read().split('\n')
lines.pop()
n = len(lines)
w = len(lines[0])
grid = [ ['.' for i in range(w)] for i in range(n) ]

# cucumbers = set()
east = set()
south = set()

count = 0

for y in range(n):
  for x in range(w):
    if not lines[y][x] == '.':
      grid[y][x] = lines[y][x]
      z = (x + y*1j)
      if lines[y][x] == '>':
        east.add(z)
      else:
        south.add(z)

def print_grid():
  grid = [ ['.' for i in range(w)] for i in range(n) ]
  for cuke in south:
    x = int(cuke.real)
    y = int(cuke.imag)
    grid[y][x] = 'v'
  
  for cuke in east:
    x = int(cuke.real)
    y = int(cuke.imag)
    grid[y][x] = '>'
  
#  if count == 0:
#    print("Initial state:")
#  else:
#    print(f"After {count} step:")

  
  for y in range(n):
    for x in range(w):
      print(grid[y][x], end='')
    print()

def do_step():
  global count
  global east
  global south
  global n
  global w
  
  did_move = False
  
  # east facing
  cukes_moving = set()
  propsed_moves = set()

  for cuke in east:
    # y in range(n), x in range(w):
    x = int(cuke.real) + 1
    y = int(cuke.imag)
    if x == w:
      x = 0
    proposed_move = (x + y*1j)
      
    if (proposed_move in east) or (proposed_move in south):  # blocked
      pass
    else:
      cukes_moving.add(cuke)
      propsed_moves.add(proposed_move)    

  if cukes_moving:
    did_move = True
    
  east = east - cukes_moving
  east = east.union(propsed_moves)

  # south facing
  cukes_moving = set()
  propsed_moves = set()

  for cuke in south:
#    proposed_move = cuke + 1j
    x = int(cuke.real)
    y = int(cuke.imag) + 1
    if y == n:
      y = 0
    proposed_move = (x + y*1j)

    if (proposed_move in east) or (proposed_move in south):  # blocked
      pass
    else:
      cukes_moving.add(cuke)
      propsed_moves.add(proposed_move)    

  if cukes_moving:
    did_move = True

  south = south - cukes_moving
  south = south.union(propsed_moves)

  count += 1
  
  return did_move

#print_grid()
while True:
#  input()
  did_move = do_step()
#  print_grid()
  if not did_move:
#    print('done')
    break
    
print(count)