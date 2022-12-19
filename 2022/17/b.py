#f = open("test.txt")
f = open("input.txt")
line = f.readline()
moves = list(line.rstrip())

width = 7

field = []

# I want field[0] to be the bottom of the tape
field.append([-1]*width)

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

def get_height():
  return len(field) - 1

def print_piece(i):
  piece = pieces[i]
  for i in range(len(piece)):
    print(piece[i])

# piece = pieces[i]
def add_piece_to_field(piece):
  field.append(['.']*width)
  field.append(['.']*width)
  field.append(['.']*width)
  for line in piece:
    field.append(line.copy())

def can_move(dir):
  has_seen_at = False
  if dir == '>':
    # starting from the top of the field
    # if all the lines with an @ have a '.' to the right of them
    # then we can move right
    # stop when we hit a line that doesn't have an @
    # return False if there's a @ with a '#' to the right of it, or barrier
    for i in range(len(field)-1,-1,-1):
      line = field[i]
      if has_seen_at and '@' not in line:
        break
      for i,c in enumerate(line):
        if c == '@':
          has_seen_at = True
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
      if has_seen_at and '@' not in line:
        break
      for i,c in enumerate(line):
        if c == '@':
          has_seen_at = True
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
      if has_seen_at and '@' not in line:
        break
      for i,c in enumerate(line):
        if c == '@':
          has_seen_at = True
          if (line_down[i] == '#') or (line_down[i] == -1):
            return False
    return True

def do_move(dir):
  if not can_move(dir):
    return
  if dir == '>':
    for i in range(len(field)-1,max(len(field)-100,0),-1):
      line      = field[i]
      for i in range(width-1, -1, -1):
        if line[i] == '@':
          line[i] = '.'
          line[i+1] = '@'
  elif dir == '<':
    for i in range(len(field)-1,max(len(field)-100,0),-1):
      line = field[i]
      for i in range(width):
        if line[i] == '@':
          line[i] = '.'
          line[i-1] = '@'
  elif dir == 'v':
    for i in range(max(len(field)-100,0), len(field)-1):
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
 

rock_count = 0
move_idx = 0
move_len = len(moves)

seen = {}
def fingerprint_field(top_k):
  return hash(':'.join(map(lambda x : ''.join(x), field[-top_k:])))

# send a new rock down
add_piece_to_field(pieces[rock_count % 5])


T = 1000000000000
#T = 2022
offset = 0
while rock_count < T:
#   add_piece_to_field(pieces[rock_count % 5])
   move = moves[move_idx]
   move_idx = (move_idx + 1) % move_len

   if can_move(move):
      do_move(move)
  
   if can_move('v'):
     do_move('v')
     clean_top()
 
   else: #can't move
 
     fix_piece()
     rock_count += 1
     clean_top()
  
     if rock_count == T:
       break
  
     # make key
     rock_idx = rock_count % 5
     # idea is to keep track of the board state, if we're in a place where
     # we're going to place the same rock in the same sequence of moves
     # and we're at the same place in the board's configuration then we can
     # simply cycle what we've done to build up the height to where we want
     # and then simulate the remaining 
     # NB: look back of 30 is a hack, smallest value here is input dependent
     fingerprint = fingerprint_field(min(30,len(field)-1))
     key = (move_idx, rock_idx, fingerprint)
     if key in seen:
       # hit
       last_rock_count, last_height = seen[key]
       rem = T - rock_count
       rep = rem // (rock_count - last_rock_count)
       offset = rep * (get_height() - last_height)
       rock_count += rep * (rock_count - last_rock_count)
       seen = {}

     seen[key] = (rock_count, get_height())
     # if key has been seen then finish computation

     # otherwise continue on
     add_piece_to_field(pieces[rock_count % 5])

clean_top() 
print(get_height() + offset)

