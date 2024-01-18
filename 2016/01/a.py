dirs = open('input.txt').read().strip().split(', ')

# start north
heading = 1j
# start at origin
coord = 0

m = {'L':1j, 'R':-1j}

for step in dirs:
  dir = step[0]
  n = int(step[1:])

  heading *= m[dir]
  coord += heading*n

print(int(abs(coord.real)+abs(coord.imag)))

