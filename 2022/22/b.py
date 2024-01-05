import re

#filename = "test"
filename = "input"

# input
rows = 200
cols = 150
# test
#rows = 12
#cols = 16

f = open(filename + "_a.txt")
lines = f.readlines()

f = open(filename+"_b.txt")
line = f.readline().rstrip()
moves = re.findall("([0-9]+|[LR])",line)

grid = [[0] * cols for _ in range(rows)]

r = 0
for line in lines:
 line = line.rstrip()
 n = cols - len(list(line))
 grid[r] = list(line) + [' ']*n
 r += 1

start_r = 0
start_c = grid[start_r].index('.')
heading = +1

cr = start_r
cc = start_c

def get_heading_ch():
  if heading == +1:
   return '>'
  if heading == -1:
   return '<'
  if heading == +1j:
   return 'v'
  if heading == -1j:
   return '^'

def print_grid():
  for r in range(rows):
    for c in range(cols):
       if r == cr and c == cc:
         p = get_heading_ch()
         print(p, end='')
       else:
         print(grid[r][c], end='')
    print()

print(heading)
#print_grid()
print()
#input()

def do_move(move):
  global heading
  global cc
  global cr

  if move == 'L':
    heading *= -1j
    print(move, heading)
    #print_grid()
    print()
    #input()

  elif move == 'R':
    heading *= +1j
    print(move, heading)
    #print_grid()
    print()
    #input()

  elif move.isdigit():
    steps = int(move)

    if heading == +1:
      dr =  0
      dc = +1
    if heading == -1:
      dr =  0
      dc = -1
    if heading == +1j:
      dr = +1
      dc =  0
    if heading == -1j:
      dr = -1
      dc =  0

    for step in range(steps):
      pr = (cr + dr)
      pc = (cc + dc)
      pheading = heading

#      # A, going up off the top
#      if cr ==   0 and cc in range(100,150) and heading == -1j:
#        pr = 199
#        pc = cc
#        pheading = -1j
#
#      # A, going down off the bottom
#      if cr == 199 and cc in range(  0, 50) and heading == +1j:
#        pr = 0
#        pc = cc
#        pheading = +1j
#
#      # B, going up off the top
#      if cr ==   0 and cc in range( 50,100) and heading == -1j:
#        pr = 100 + cc
#        pc = 0
#        pheading = +1
#
#      # B, going left off the left side
#      if cr in range(150,200) and cc == 0 and heading ==  -1:
#        pr = 0
#        pc = cr - 100
#        pheading = +1j
#
      if grid[pr][pc] == ' ':
        while grid[pr][pc] == ' ':
          pr = (pr + dr) % len(grid)
          pc = (pc + dc) % len(grid[0])

      if grid[pr][pc] == '#':
        break

      cr = pr
      cc = pc
      heading = pheading

      print(heading)
      #print_grid()
      print()
      #input()

  else:
    print("ack!")
    exit(0)

for move in moves:
  do_move(move)

d = {'>' : 0, 'v' : 1, '<' : 2 , '^' : 3}
password = (cr + 1) * 1000 + 4 * (cc + 1) + d[get_heading_ch()]
print(password)
