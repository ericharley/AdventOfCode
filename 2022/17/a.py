f = open("input.txt")
line = f.readline()
moves = list(line.rstrip())

#pieces = []
#
#[1,1,1,1]
#[1,1,1,1]
#[1,1,1,1]
#[1,1,1,1]
#
#print(moves)

width = 7

field = []

# I want field[0] to be the bottom of the tape
field.append([-1]*width)
field.append(['.']*width)
field.append(['.']*width)
field.append(['.']*width)

# print from top to bottom
# field[0] is the bottom?
def print_field():
 d = { 0 : '.', -1 : '-' , 1 : '@', 2:'#', '.' : '.', '@':'@','#':'#'}
 for i in range(len(field)-1,-1,-1):
   output = ''.join(list(map(lambda x : d[x], field[i])))
   if i == 0:
     print(f'{i:3d} +'+output+'+')
   else:
     print(f'{i:3d} |'+output+'|')     

pieces = [0]*5
pieces[0] = [list('..@@@@.')]
pieces[1] = [list('...@...'), list('..@@@..'), list('...@...')]
pieces[2] = [list('....@..'), list('....@..'), list('..@@@..')]
pieces[3] = [list('..@....'), list('..@....'), list('..@....'), list('..@....')]
pieces[4] = [list('..@@...'), list('..@@...')]
pieces[0].reverse()
pieces[1].reverse()
pieces[2].reverse()
pieces[3].reverse()
pieces[4].reverse()

def print_piece(i):
  piece = pieces[i]
  for i in range(len(piece)):
    print(piece[i])

# piece = pieces[i]
def add_piece_to_field(piece):
  for line in piece:
    field.append(line.copy())

def can_move(dir):
  if dir == '>':
    # starting from the top of the field
    # if all the lines with an @ have a '.' to the right of them
    # then we can move right
    # stop when we hit a line that doesn't have an @
    # return False if there's a @ with a '#' to the right of it, or barrier
    for i in range(len(field)-1,-1,-1):
      line = field[i]
#      if '@' not in line:
#        break
      for i,c in enumerate(line):
        if c == '@':
          if (i == width-1) or (line[i+1] == '#'):
            return False
    return True

  if dir == '<':
    # starting from the top of the field
    # if all the lines with an @ have a '.' to the left of them
    # then we can move left
    # stop when we hit a line that doesn't have an @
    # return False if there's a @ with a '#' to the left of it, or barrier
    for i in range(len(field)-1,-1,-1):
      line = field[i]
#      if '@' not in line:
#        break
      for i,c in enumerate(line):
        if c == '@':
          if (i == 0) or (line[i-1] == '#'):
            return False
    return True

  if dir == 'v':
    # starting from the top of the field
    # if all the lines with an @ have a '.' underneath them
    # then we can move down
    # stop when we hit a line that doesn't have an @
    # return False if there's a @ with a '#' below it, or -1 (floor)
    for i in range(len(field)-1,0,-1):
      line      = field[i]
      line_down = field[i-1]
#      if '@' not in line:
#        break
      for i,c in enumerate(line):
        if c == '@':
          if (line_down[i] == '#') or (line_down[i] == -1):
            return False
    return True

def do_move(dir):
  if not can_move(dir):
    return
  if dir == '>':
    for i in range(len(field)-1,0,-1):
      line      = field[i]
      for i in range(width-1, -1, -1):
        if line[i] == '@':
          line[i] = '.'
          line[i+1] = '@'
  elif dir == '<':
    for i in range(len(field)-1,0,-1):
      line = field[i]
      for i in range(width):
        if line[i] == '@':
          line[i] = '.'
          line[i-1] = '@'
  elif dir == 'v':
    for i in range(len(field)-1):
      line_up   = field[i+1]
      line_down = field[i]
      for i,c in enumerate(line_up):
        if c == '@':
          line_down[i] = '@'
          line_up[i] = '.'

def clean_top():
 while ''.join(field[-1]) == '.......':
   field.pop()

def fix_piece():
  for i in range(len(field)):
    field[i] = list(map(lambda x : '#' if x == '@' else x, field[i]))
 

for move in moves:
  # move
  if move == '>':
    1
  if move == '<':
    1
  # drop

print_field()
print()

t = 0

add_piece_to_field(pieces[t % 5])
t+=1

moves = 300*moves
for move in moves:
 if can_move(move):
    do_move(move)
 
# print(t)
# print_field()
# print()

 if can_move('v'):
   do_move('v')
   clean_top()
 else:
   fix_piece()
   clean_top()
   field.append(['.']*width)   
   field.append(['.']*width)
   field.append(['.']*width)
   add_piece_to_field(pieces[t % 5])
   t+=1

 if t==2023:
   break

# print(t)
# print_field()
# print()

