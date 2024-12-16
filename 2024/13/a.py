import re
import math
from functools import cache

@cache
def t(AX,AY,BX,BY,X,Y,cost):

  if X == 0 and Y == 0:
    return cost

  if X < 0 or Y < 0:
    return math.inf

  return min(t(AX,AY,BX,BY,X-AX,Y-AY,cost + 3), t(AX,AY,BX,BY,X-BX,Y-BY,cost + 1))

lines = open('input.txt').read().strip().split('\n\n')
data = [list(map(int, re.findall(r'\d+', x))) for x in lines]

total = 0
for AX,AY,BX,BY,PX,PY in data:
  v = t(AX,AY,BX,BY,PX,PY,0)
  if v != math.inf:
    total += v

print(total)