dirs = open('input.txt').read().strip().split(', ')

# start north
heading = 1j
# start at origin
coord = 0

from collections import defaultdict
visited = set()
m = {'L':1j, 'R':-1j}

visited.add(coord)

for step in dirs:
  dir = step[0]
  n = int(step[1:])

  heading *= m[dir]
  for i in range(n):
    coord += heading
    if coord in visited:
      print(int(abs(coord.real)+abs(coord.imag)))
      exit()
    visited.add(coord)


