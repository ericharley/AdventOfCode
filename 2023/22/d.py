# coordinate differences are either 0 or 1
# a 1x1 cube is x1 == x2, y1 == y2, z1 == z2
#
# 27 cubes
# 145 up/down pieces
# 626 front/back
# 701 side to side pieces
# 1499 pieces
#
# pieces have length 1 to 5
#
#x1 <= x2
#y1 <= y2
#z1 <= z2
#
# the stack is a bag of cubes
# start with the floor cubes being in the bag
# for each piece in the stack by increasing z value
# lower it by one and see if it intersects anything in the bag
# if it does stop
# if it doesn't repeat until it does
# once you can't drop it anymore, it's fixed, add its cubes to the bag

from itertools import product
from queue import PriorityQueue
from collections import defaultdict

pieces = PriorityQueue()

max_x = 0
max_y = 0
max_z = 0

#lines = open('test.txt').read().strip().split('\n')
lines = open('input.txt').read().strip().split('\n')

for line in lines:
  x1,y1,z1 = map(int,line.replace('~',',').split(',')[0:3])
  x2,y2,z2 = map(int,line.replace('~',',').split(',')[3:])
  pieces.put((z1, (x1,y1,z1,x2,y2,z2)))

  max_x = max(max_x, x2)
  max_y = max(max_y, y2)
  max_z = max(max_z, z2)

moves = {}
cube_to_piece = {}
bag = set()
supports = defaultdict(set)
supported_by = defaultdict(set)

floor = 'floor'

# Add the cubes for the floor to the bag
for x,y in product(range(0,max_x+1),range(max_y+1)):
  bag.add((x,y,0))
  cube_to_piece[(x,y,0)] = floor

def get_cubes(piece):
  (x1,y1,z1,x2,y2,z2) = piece
  return product(range(x1,x2+1), range(y1,y2+1), range(z1,z2+1))

def add_piece_to_bag(piece, bag):
  for cube in get_cubes(piece):
    bag.add(cube)

def can_lower(piece, bag):
  for cube in get_cubes(piece):
     (x,y,z) = cube
     if (x,y,z-1) in bag:
       # there's a cube underneath piece at this cube
       # so we can't move
       return False
  return True

def lower_piece(piece):
  (x1,y1,z1,x2,y2,z2) = piece
  return (x1,y1,z1-1,x2,y2,z2-1)

frozen = set()

while not pieces.empty():
  _,p = pieces.get()
  # lower it (q) down until there's at least one cube beneath it 
  q = p
  while can_lower(q, bag):
    q = lower_piece(q)

  # q is the piece after p is lowered until it cannot be lowered further
  if p not in moves:
    moves[p] = q

  # q is the translation of p that abuts a cube in the bag
  # q can now be frozen itself
  add_piece_to_bag(q, bag)

  # find the pieces that this piece rests on by lowering it and finding overlaps
  q_set = set(get_cubes(lower_piece(q)))
  for b in frozen:
    b_set = set(get_cubes(moves[b]))
    if q_set & b_set:
      supported_by[p].add(b)
      supports[b].add(p)

  frozen.add(p)


# Part 1

# a piece can be removed if any piece that it supports has another piece that supports it
count = 0
for piece in moves:
  if not [u for u in supports[piece] if len(supported_by[u]) < 2]:
    count += 1

print(count)

# Part 2

total = 0

#for u in moves:
#  for v in supports[u]:
#    if u != v:
#      s = f'{u} -> {v}'
#      s=s.replace('(','A')
#      s=s.replace(', ','')
#      s=s.replace(')','')
#      print(s)

N = set(moves)
dom = {}

for v in N:
  dom[v] = N.copy()

while True:
  a_change = False
  for n in N :
    old = dom[n]
    S = [dom[p] for p in supported_by[n]]
    if S:
      int_over_pred = set.intersection(*S)
      dom[n] = {n} | int_over_pred
    else:
      dom[n] = {n}
    if old != dom[n]:
      a_change = True

  if not a_change:
    break

t = 0
for u in N:
  t += sum([1 for v in N if v != u and u in dom[v]])
print(t)
