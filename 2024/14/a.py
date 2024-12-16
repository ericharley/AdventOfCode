import re
from collections import Counter

lines = open('input.txt').readlines()
data = [list(map(int, re.findall(r'-?\d+', x))) for x in lines]

def h(t, data):
  return [((vx*t + px) % 101, (vy*t + py) % 103) for px,py,vx,vy in data]

def quad(k):
  x,y = k
  if x == 50 or y == 51:
    return -1
  return ((0 <= x < 50) + 2*(0 <= y < 51))

# Part 1
Q = Counter(map(quad, h(100, data)))
print(Q[0]*Q[1]*Q[2]*Q[3])

# Part 2
def mean_var(f):
  mean_x = sum(x for x, _ in f) / len(f)
  mean_y = sum(y for _, y in f) / len(f)
  var = sum(((x - mean_x) ** 2 + (y - mean_y) ** 2) for x, y in f) / len(f)
  return var

v = [ (mean_var(h(t,data)),t) for t in range(101*103) ]
_,tree_t = sorted(v)[0]

print(tree_t)