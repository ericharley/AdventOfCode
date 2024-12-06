grid = open('input.txt').read().strip().split('\n')

def g(r,c):
  return c - r*1j

def inv_g(z):
  r = int(z.imag*(-1))
  c = int(z.real)
  return r,c

m = set()
visited = set()

max_rows = len(grid)
max_cols = len(grid[0])

for r in range(max_rows):
  for c in range(max_cols):
    if grid[r][c] == '#':
      m.add( g(r,c) )
    if grid[r][c] == '^':
      starting_pos = g(r,c)
      starting_heading = +1j

      pos = g(r,c)
      heading = +1j


def get_heading_ch(heading):
  if heading == +1:
   return '>'
  if heading == -1:
   return '<'
  if heading == -1j:
   return 'v'
  if heading == +1j:
   return '^'

def print_grid():
  for r in range(max_rows):
    for c in range(max_cols):
       if pos == g(r,c):
         ch = get_heading_ch(heading)
       elif g(r,c) in m:
         ch = '#'
       elif g(r,c) in visited:
         ch = 'X'
       else:
         ch = '.'
       print(ch,end='')
    print()
  print()

def do_move():
  new_pos = pos + heading
  new_heading = heading

  if new_pos in m:
    new_pos = pos
    new_heading = heading * -1j

  return new_pos, new_heading

def on_board():
  r,c = inv_g(pos)
  return (0 <= r < max_rows) and (0 <= c < max_cols)

# Part 1
while on_board():
  visited.add(pos)
  #print_grid()
  pos, heading = do_move()

print(len(visited))

# Part 2
def is_loop():
  return (pos,heading) in visited

orig_path = visited.copy()

pos = starting_pos
heading = starting_heading
visited = set()
t = 0

def do_run():
  global pos
  global heading
  while on_board() and (pos,heading) not in visited:
    visited.add((pos,heading))
    #print_grid()
    pos, heading = do_move()

starting_m = m.copy()
for z in orig_path:
    r,c = inv_g(z)
    new_obs = g(r,c)
    m.add(new_obs)

    pos = starting_pos
    heading = starting_heading
    visited = set()

    do_run()

    if is_loop():
      t += 1

    m = starting_m.copy()


print(t)
