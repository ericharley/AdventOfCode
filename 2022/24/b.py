import math
from collections import deque

# one set for each of the four directions of storms
blizzards = [set() for _ in range(4)]

for r, line in enumerate(open(0).read().splitlines()[1:]):
    for c, item in enumerate(line[1:]):
        if item in "<>^v":
            blizzards["<>^v".find(item)].add((r, c))


queue = deque([(0, -1, 0)])
seen = set()
target = (r, c - 1)

# the period in which the whole board repeats
lcm = r * c // math.gcd(r, c)

# part one
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
      queue = []
      break

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
       key = (time % lcm, nr, nc)
       if key not in seen:
         seen.add(key)
         queue.append((time, nr, nc))

queue = deque([(time, r, c-1)])
seen = set()
target = (-1, 0)

# part two
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
      queue = []
      break

    # if we're not at the starting point, and we would go off the board
    # we can't take this move
    if (nr < 0 or nc < 0 or nr >= r or nc >= c) and not (nr, nc) == (r, c-1):
      continue

    fail = False

    # see if an incoming blizard would hit us at the proposed point
    if (nr, nc) != (r, c-1):
      for i, tr, tc in ((0, 0, -1), (1, 0, 1), (2, -1, 0), (3, 1, 0)):
          if ((nr - tr * time) % r, (nc - tc * time) % c) in blizzards[i]:
            fail = True
            break
    
    if not fail:
       key = (nr, nc, time % lcm)
       if key not in seen:
         seen.add(key)
         queue.append((time, nr, nc))

print(time)

queue = deque([(time, -1, 0)])
seen = set()
target = (r, c - 1)

# the periood in which the whole board repeats
lcm = r * c // math.gcd(r, c)

# part one
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
      queue = []
      break

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
       if key not in seen:
         seen.add(key)
         queue.append((time, nr, nc))

