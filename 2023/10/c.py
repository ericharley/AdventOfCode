filename = 'input.txt'

grid = open(filename).read().strip().splitlines()

# add padding around grid
grid.insert(0, '.'*len(grid[0]))
grid.append('.'*len(grid[0]))
for r, row in enumerate(grid):
    grid[r] = '.' + grid[r] + '.'

# find the starting pipe
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == "S":
            sr = r
            sc = c

loop = {(sr, sc)}
q = [(sr, sc)]

# FIX THIS
#                , grid[sr-1][sc],
#grid[sr  ][sc-1], grid[sr  ][sc], grid[sr  ][sc+1]
#                , grid[sr+1][sc],
#
dirs = []
if grid[sr-1][sc] in '|7F':
  dirs.append('north')
if grid[sr+1][sc] in '|LJ':
  dirs.append('south')
if grid[sr][sc+1] in '-J7':
  dirs.append('east')
if grid[sr][sc-1] in '-LF':
  dirs.append('west')
dirs = tuple(dirs)
m = {
 ('north','south') : '|',
 ('north','east') : 'L',
 ('north','west') : 'J',
 ('south','east') : 'F',
 ('south','west') : '7',
 ('east', 'west') : '-',
}

grid[sr] = grid[sr].replace('S',m[dirs],1)


def add_unless(r,c):
  if (r,c) not in loop:
    q.append((r,c))
    loop.add((r,c))
    return True

  return False

points = []

while q:
  r, c = q.pop()
  points.append((r,c))

  if grid[r][c] == '|':
    add_unless(r-1,c)
    add_unless(r+1,c)

  elif grid[r][c] == '-':
    add_unless(r,c-1)
    add_unless(r,c+1)

  elif grid[r][c] == 'L':
    add_unless(r-1,c)
    add_unless(r,  c+1)

  elif grid[r][c] == 'J':
    add_unless(r,  c-1)
    add_unless(r-1,c)

  elif grid[r][c] == '7':
    add_unless(r,  c-1)
    add_unless(r+1,c)

  elif grid[r][c] == 'F':
    add_unless(r,  c+1)
    add_unless(r+1,c)

inside = 0
print(len(loop) // 2)  

def polygonArea(vertices):
  N = len(vertices)

  sum = 0
  for i in range(0, N):
    sum += vertices[i][0] *  vertices[(i+1) % N][1]
    sum -= vertices[i][1] *  vertices[(i+1) % N][0]

  area = abs(sum) // 2

  return area

print(polygonArea(points) - len(loop)//2 +1)
