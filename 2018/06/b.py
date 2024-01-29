import math

lines = open('input.txt').read().strip().splitlines()

def md(a,b):
  ax,ay = a
  bx,by = b
  return abs(ax-bx) + abs(ay-by)

points = []

min_x, max_x = math.inf, -math.inf
min_y, max_y = math.inf, -math.inf

for line in lines:
  x, y = map(int,line.split(', '))
  points.append((x,y))
  min_x, max_x = min(min_x, x), max(max_x, x)
  min_y, max_y = min(min_y, y), max(max_y, y)

number_of_points = len(points)

threshold = 10000
c = 0

# since the sum of the distances must be less than 10000,
# the farthest a point could be is 10000/number_of_points

w = math.ceil(threshold / number_of_points)
lx,ux = min_x-w, max_x+w
ly,uy = min_y-w, max_y+w

for x in range(lx,ux):
  for y in range(ly,uy):
    total = 0
    for rx,ry in points:
      total += md((x,y),(rx,ry))
      if total >= threshold:
        break
    else:
      if total < threshold:
        c += 1

print(c)
