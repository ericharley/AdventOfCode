import math
from collections import defaultdict

def md(a,b):
  ax,ay = a
  bx,by = b
  return abs(ax-bx) + abs(ay-by)

lines = open('input.txt').read().strip().splitlines()

points = []

min_x, max_x = math.inf, -math.inf
min_y, max_y = math.inf, -math.inf

for line in lines:
  x, y = map(int,line.split(', '))
  points.append((x,y))
  min_x, max_x = min(min_x, x), max(max_x, x)
  min_y, max_y = min(min_y, y), max(max_y, y)

def f(w):
  d = {}
  for x in range(min_x-w,max_x+w):
    for y in range(min_y-w,max_y+w):
      d[x,y] = { (rx,ry) : md((x,y),(rx,ry)) for rx, ry in points }

  pts = defaultdict(int)
  for x,y in d:
    _d = d[x,y]
    m = min(_d, key=_d.get)
    l = [pt for pt in _d if _d[pt] == _d[m]]
    if len(l) == 1:
      pts[l[0]] += 1

  return pts

# Run it twice, bounded regions shouldn't grow
# 
pts1 = f(0)
pts2 = f(1)

print(pts1[max([k for k in pts1 if pts2[k] == pts1[k]],key=pts1.get)])
