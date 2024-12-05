grid = open('input.txt').read().strip().split('\n')

max_col = len(grid[0])
max_row = len(grid)
cols = ['' for _ in range(max_col)]
rows = ['' for _ in range(max_row)]
fdiag = ['' for _ in range(max_row + max_col - 1)]
bdiag = ['' for _ in range(len(fdiag))]

for r in range(max_row):
  for c in range(max_col):
    cols[c] += grid[r][c]
    rows[r] += grid[r][c]
    fdiag[c+r] += grid[r][c]
    bdiag[c-r+max_row-1] += grid[r][c]

data = (cols+rows+fdiag+bdiag)

# Part 1
print( sum([x.count('XMAS')+x.count('SAMX') for x in data]) )

# Part 2
t = 0
for r in range(1,len(grid)-1):
  for c in range(1,len(grid[0])-1):
    s = ''.join([grid[r][c],grid[r-1][c-1],grid[r-1][c+1],grid[r+1][c-1],grid[r+1][c+1]])
    if s in ['AMSMS','ASMSM','AMMSS','ASSMM']:
      t += 1

print(t)
