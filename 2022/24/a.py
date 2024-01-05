import math
from collections import deque

# one set for each of the four directions of storms
blizzards = tuple(set() for _ in range(4))

for r, line in enumerate(open(0).read().splitlines()[1:]):
    for c, item in enumerate(line[1:]):
        if item in "<>^v":
            blizzards["<>^v".find(item)].add((r, c))


queue = deque([(0, -1, 0)])
seen = set()
target = (r, c - 1)

lcm = r * c // math.gcd(r, c)
while queue:
  time, cr, cc = queue.popleft()
  time += 1
 
  # for moves in each of the four cardinal directionso
  for dr, dc in ((0, 1), (0, -1), (-1, 0), (1, 0), (0, 0)):
    nr = cr + dr
    nc = cc + dc

    # if we're at the end then we stop
    if (nr, nc) == target:
      print(time)
      exit(0)

    # if we're not at the starting point, and we would go off the board
    # we can't take this move
    if (nr < 0 or nc < 0 or nr >= r or nc >= c) and not (nr, nc) == (-1, 0):
      continue

    fail = False

    # see if an incoming blizard would hit us at the proposed point
    if (nr, nc) != (-1, 0):
      for i, tr, tc in ((0, 0, -1), (1, 0, 1), (2, -1, 0), (3, 1, 0)):
          if ((nr - tr * time) % r, (nc - tc * time) % c) in blizzards[i]:
            fail = True
            break
    
    if not fail:
       key = (nr, nc, time % lcm)
       if key in seen:
         continue
       # else
       seen.add(key)
       queue.append((time, nr, nc))

exit(0)

width = int(max([x.real for x in wall]) + 1)
height = int(max([x.imag for x in wall]) + 1)

start = 1 + 0j
goal = (width-2) + (height-1)*1j

def print_grid():
 for r in range(width):
  for c in range(height):
   z = (c + r*1j)
   if z in wall:
     print('#',end='')
   elif z in [x[0] for x in storms]:
     s = [x[1] for x in storms if x[0] == z]
     if len(s) == 1:
       print(s[0],end='')
     else:
       print(len(s),end='')
   elif z == start:
     print('S', end='')
   elif z == goal:
     print('E', end='')
   else:
     print('.', end='')
  print()

def step_storms(storms):
 pass

exit(0)

#print('== Initial State ==')
#print_grid()
#input()


# do one round
for round in range(10):
 proposed = {}
 for elf in elves:
   # check neighborhood for elves 
   if not any(elf + x in elves for x in neighborhood):
     continue
 
   # propose a move for this elf
   for move in moves:
     # if all the slots are empty for this move then we can propose moving there
     if all((elf + m) not in elves for m in scanmap[move]):
         if (elf+move) in proposed:
           proposed[elf+move].append(elf)
         else:
           proposed[elf + move] = [elf]
         break
 
 for new_loc in proposed:
   if len(proposed[new_loc]) == 1:
     elves.remove(proposed[new_loc][0])
     elves.add(new_loc)
 
 ## cycle the moves list
 moves.append(moves.pop(0))

 #print(f'== End of Round {round+1} ==')
 #print_grid()
 #input()

# all elves have proposed moves
# for all the proposed moves, if only one was proposed...

# c := x position
# r := y position

# -1-1j  0-1j  +1-1j
# -1-0j  0-0j  +1-0j
# -1+1j  0+1j  +1+1j


mx = min(x.real for x in elves)
Mx = max(x.real for x in elves)
my = min(x.imag for x in elves)
My = max(x.imag for x in elves)

print((Mx - mx + 1) * (My - my + 1) - len(elves))
