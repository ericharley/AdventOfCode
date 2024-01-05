#turn off 199,133 through 461,193
#toggle 322,558 through 977,958
#turn on 226,196 through 599,390

lines = open('input.txt').read().strip().split('\n')
ins = []

f = {
 'on'     : (lambda x : 1),
 'off'    : (lambda x : 0),
 'toggle' : (lambda x : 1-x)
}

# Parse Input
for line in lines:

 if 'turn off' in line:
    op = 'off'
    x1,y1 = map(int, line.split()[2].split(','))
    x2,y2 = map(int, line.split()[4].split(','))

 elif 'turn on' in line:
    op = 'on'
    x1,y1 = map(int, line.split()[2].split(','))
    x2,y2 = map(int, line.split()[4].split(','))

 elif 'toggle' in line:
    op = 'toggle'
    x1,y1 = map(int, line.split()[1].split(','))
    x2,y2 = map(int, line.split()[3].split(','))

 else:
    print('error:', line)
    break

 ins.append((op,x1,y1,x2,y2))

# Part 1
grid = [[0]*1000 for _ in range(1000)]
for (op, x1,y1,x2,y2) in ins:
  op = f[op]
  for r in range(x1, x2+1):
    for c in range(y1, y2+1):
      grid[r][c] = op(grid[r][c])

print( sum([sum(grid[r]) for r in range(len(grid))]) )

# Part 2
f = {
 'on'     : (lambda x : x+1),
 'off'    : (lambda x : max(0,x-1)),
 'toggle' : (lambda x : x+2)
}

grid = [[0]*1000 for _ in range(1000)]
for (op, x1,y1,x2,y2) in ins:
  op = f[op]
  for r in range(x1, x2+1):
    for c in range(y1, y2+1):
      grid[r][c] = op(grid[r][c])

print( sum([sum(grid[r]) for r in range(len(grid))]) )


