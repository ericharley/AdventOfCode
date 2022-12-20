f = open('input.txt')

grid = set()
grid2 = set()

steps = { }
steps2 = { }

x0 = 0 + 0j
steps[x0] = 0
steps2[x0] = 0

# Part 1
x = x0
moves = f.readline().rstrip().split(',')
for dl in moves:
  d = dl[0]
  l = dl[1:]
  diff = int(l)

  dx = {'L' : -1, 'R' : +1, 'U' : 1j, 'D' : -1j}[d]

  for i in range(diff):
    x += dx
    steps[x] = steps[x-dx] + 1
    grid.add(x)


x = x0
moves = f.readline().rstrip().split(',')
for dl in moves:
  d = dl[0]
  l = dl[1:]
  diff = int(l)
  dx = {'L' : -1, 'R' : +1, 'U' : 1j, 'D' : -1j}[d]
  for i in range(diff):
    x += dx
    steps2[x] = steps2[x-dx] + 1
    grid2.add(x)

     
print(min([int(abs(x.real) + abs(x.imag)) for x in grid.intersection(grid2)]))

# Part 2
print(min([steps[x]+steps2[x] for x in grid.intersection(grid2)]))
