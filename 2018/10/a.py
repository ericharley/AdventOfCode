import math
import sys

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

def bounding_box(pts):
  max_x = max([x for x,_ in pts])
  max_y = max([y for _,y in pts])
  min_x = min([x for x,_ in pts])
  min_y = min([y for _,y in pts])
  return min_x,min_y,max_x,max_y

def translate(points,t):
  return {(p[0]+v[0]*t, p[1]+v[1]*t) for p,v in points}

lines = open('input.txt').read().strip().splitlines()
data = []
for line in lines:
  line = line.replace('<','(').replace('>',')')
  line = line.replace(' velocity=',',').replace('position','p,v')
  exec(line)
  data.append((p,v))

t = 0
bounding_box_perimeter = math.inf

while True:
  pts = translate(data,t)
  min_x,min_y,max_x,max_y = bounding_box(pts)
 
  if (max_x-min_x)+(max_y-min_y) < bounding_box_perimeter:
    bounding_box_perimeter = (max_x-min_x)+(max_y-min_y)
  else:
    break
  t += 1

t -= 1
pts = translate(data,t)
min_x,min_y,max_x,max_y = bounding_box(pts)

screen = newscreen(max_y-min_y+1, max_x-min_x+1)

for y in range(min_y,max_y+1):
 for x in range(min_x,max_x+1):
   if (x,y) in pts:
     screen[y-min_y][x-min_x] = PXON

printscreen(screen)
print(t)
