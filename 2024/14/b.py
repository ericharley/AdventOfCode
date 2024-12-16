import sys
import re
from collections import Counter

lines = open('input.txt').readlines()
data = [list(map(int, re.findall(r'-?\d+', x))) for x in lines]

x_max,y_max = 101,103
x_mid,y_mid = (x_max)//2,(y_max)//2

def h(t,data):
  return [((vx*t + px) % x_max, (vy*t + py) % y_max) for px,py,vx,vy in data]

def quad(k):
  x,y = k
  if x == x_mid or y == y_mid:
    return -1
  return (0 <= x < x_mid) + 2*(0 <= y < y_mid)

# Part 1
Q = Counter(map(quad, h(100,data)))
print(Q[0]*Q[1]*Q[2]*Q[3])

# Part 2
def mean_var(f):
  mean_x = sum(x for x, y in f) / len(f)
  mean_y = sum(y for x, y in f) / len(f)
  var = sum(((x - mean_x) ** 2 + (y - mean_y) ** 2) for x, y in f) / len(f)
  return var

v = [ (mean_var(h(t,data)),t) for t in range(x_max*y_max) ]
_,tree_t = sorted(v)[0]

print(tree_t)

print('Press Enter to Display...')
input()

f = h(tree_t,data)

PXOFF = '\u2592'
PXON = '\u2588'


def printscreen(screen):
    # clear the terminal
    sys.stdout.write('\033c')

    ssize = len(screen[0])

    print('┍{}┑'.format('━' * ssize))
    for row in screen:
        sys.stdout.write('│')
        for px in row:
            sys.stdout.write('{}'.format(px))
        sys.stdout.write('│\n')
    print('┕{}┙'.format('━' * ssize))

def newscreen(rows, cols):
    return [[PXOFF for c in range(cols)] for r in range(rows) ]

screen = newscreen(y_max, x_max)
for y in range(y_max):
   for x in range(x_max):
     if (x,y) in f:
       screen[y][x] = PXON

printscreen(screen)