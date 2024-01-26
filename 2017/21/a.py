from itertools import product
from math import sqrt

def flp(grid):
  return list(row[::-1] for row in grid)

def rot(grid):
  grid = list(map("".join, zip(*grid)))
  grid = list(row[::-1] for row in grid)
  return grid

def grid_to_tiles(grid):
  N = len(grid)
  if N % 2 == 0:
    d = 2
  elif N % 3 == 0:
    d = 3

  rows = [slice(r,r+d,1) for r in range(0,N,d)]
  cols = [slice(c,c+d,1) for c in range(0,N,d)]
  return [[x[cs] for x in grid[rs]] for rs, cs in product(rows,cols)]

def tiles_to_grid(tiles):
  N = int(sqrt(len(tiles)))
  output = []
  for r in range(N):
    output += [''.join(a) for a in zip(*tiles[N*r:N*r+N])]
  return output

data = open('input.txt').read().strip().splitlines()

m = {}
for line in data:
 (frm,to) = line.split(' => ')
 m[frm] = to
 key = frm.split('/')
 for _ in range(4):
   key = rot(key)
   m['/'.join(key)] = to
   m['/'.join(flp(key))] = to

grid = ['.#.',
        '..#',
        '###']

def iterate(grid):
  return tiles_to_grid([m['/'.join(tile)].split('/') for tile in grid_to_tiles(grid)])

def on(grid):
    return sum(row.count('#') for row in grid)

for _ in range(18):
  grid = iterate(grid)
  print(_+1,on(grid))
