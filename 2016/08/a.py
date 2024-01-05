import collections
import re
import sys
import time

PXOFF = '\u2592'
PXON = '\u2588'

def newscreen(rows=6, cols=50):
    return [ collections.deque([PXOFF for c in range(cols)]) for r in range(rows) ]

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

def rect(screen, x, y):
  # turn on pixels in an x * y square in the top left to PXON
  for c in range(x):
    for r in range(y):
      screen[r][c] = PXON

def rrow(screen, row, dist):
  # turn on pixels in an x * y square in the top left to PXON
  screen[row].rotate(dist)

def rcol(screen, col, dist):
  column = collections.deque([ arow[col] for arow in screen ])
  column.rotate(dist)
  for arow in range(len(screen)):
    screen[arow][col] = column[arow]

lines = open('input.txt').read().strip().split('\n')

screen = newscreen(rows=6, cols=50)
printscreen(screen)
time.sleep(0.10)

for line in lines:
  if 'rect' in line:
    A,B = map(int, line.replace('rect ','').split('x'))
    rect(screen, A, B)

  if 'column' in line:
    A,B = map(int, line.replace('rotate column x=','').split(' by '))
    rcol(screen, A, B)

  if 'row' in line:
    A,B = map(int, line.replace('rotate row y=','').split(' by '))
    rrow(screen, A, B)

  printscreen(screen)
  time.sleep(0.1)

lit = sum([1 for r in screen for c in r if c == PXON])

print(f'\n\nlit pixels: {lit}')
