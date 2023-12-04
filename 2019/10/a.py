grid = [ list(line.rstrip()) for line in open("input.txt").readlines() ]
#grid = [ list(line.rstrip()) for line in open("test.txt").readlines() ]
#grid = [ list(line.rstrip()) for line in open("test2.txt").readlines() ]
#grid = [ list(line.rstrip()) for line in open("test5.txt").readlines() ]

g = lambda x,y : x + y*1j

asteroids = set()
for r in range(len(grid)):
  for c in range(len(grid[0])):
    if grid[r][c] == '#':
      asteroids.add(g(c,r))

c = {}
for z1 in asteroids:
  c[z1] = 0
  for z2 in asteroids:
    if z1 == z2:
      continue
    isVisible = True
    for z3 in asteroids:
      if z3 == z2:
        continue
      r = (z1 - z3)/(z3 - z2)
      if (abs(r.imag) == 0.0) and (r.real > 0):
        # z3 is between z1 and z2
        isVisible = False
        break
#      else:
#        # z3 is outside the line segment joining z1 to z2
    if isVisible:
      c[z1] += 1

max_key = max(c, key=c.get)
print(max_key)
print(c[max_key])
