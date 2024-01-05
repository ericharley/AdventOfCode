from collections import defaultdict

def neighbors(t):
  (x,y,z,w) = t

  for dx in [-1,0,+1]:
    for dy in [-1,0,+1]:
      for dz in [-1,0,+1]:
        for dw in [-1,0,+1]:
          if not dx == dy == dz == dw == 0:
            yield (x + dx, y + dy, z + dz, w + dw)

#set of all active cubes, x,y,z,w 4-tuple
p = set()

#filename = 'test.txt'
filename = 'input.txt'

grid = open(filename).read().strip().split('\n')
for r,line in enumerate(grid):
  for c,s in enumerate(line):
    if s == '#':
      p.add((r,c,0,0))

N = 6
for i in range(N):

  #for each active cube, add one to the count for all its 26 neighbors
  c = defaultdict(int)

  for t in p:
    for nxt in neighbors(t):
      c[nxt] += 1

  np = set()

  for t in p:
    # If a cube is active and exactly 2 or 3 of its neighbors are also active,
    # the cube remains active. 
    if 2 <= c[t] <= 3:
      np.add(t)
    # Otherwise, the cube becomes inactive.

  for t in c:
    # If a cube is inactive but exactly 3 of its neighbors are active,
    # the cube becomes active.
    if c[t] == 3 and t not in p:
      np.add(t)
    # Otherwise, the cube remains inactive.

  p = np

print(len(p))
