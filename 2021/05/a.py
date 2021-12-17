import re
import numpy as np

p = re.compile("^(.*),(.*) -> (.*),(.*)$")

file = open("input.txt", "r")
lines = file.readlines()

a = np.zeros((1000,1000))

for line in lines:

  line = line.rstrip('\n')
  m = p.search(line)
  (x1,y1,x2,y2) = [int(m.group(i)) for i in range(1,5)]

  dx = +1 if (x1 < x2) else (0 if x1 == x2 else -1)
  dy = +1 if (y1 < y2) else (0 if y1 == y2 else -1)

  if (dx != 0) and (dy != 0):
     continue

  while x1 != x2 or y1 != y2:
     a[x1,y1] += 1
     x1 += dx
     y1 += dy
  a[x1,y1] += 1


print( np.sum(a > 1) )
