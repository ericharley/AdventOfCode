from collections import deque

def solve(t,N,M):

    r,c,d = t

    q = deque([(r,c,d)])
    seen = set()

    while q:
        r, c, d = q.popleft()

        if (r,c,d) in seen or not( (0 <= r < N) and (0 <= c < M) ):
            continue

        seen.add((r,c,d))

        if d == '>':
            if grid[r][c] == '.':
                q.append((r,c+1,'>'))
            elif grid[r][c] == '/':
                q.append((r-1,c,'^'))
            elif grid[r][c] == '\\':
                q.append((r+1,c,'v'))
            elif grid[r][c] == '-':
                q.append((r,c+1,'>'))
            elif grid[r][c] == '|':
                q.append((r-1,c,'^'))
                q.append((r+1,c,'v'))

        elif d == '<':
            if grid[r][c] == '.':
                q.append((r,c-1,'<'))
            elif grid[r][c] == '/':
                q.append((r+1,c,'v'))
            elif grid[r][c] == '\\':
                q.append((r-1,c,'^'))
            elif grid[r][c] == '-':
                q.append((r,c-1,'<'))
            elif grid[r][c] == '|':
                q.append((r-1,c,'^'))
                q.append((r+1,c,'v'))

        elif d == '^':
            if grid[r][c] == '.':
                q.append((r-1,c,'^'))
            if grid[r][c] == '/':
                q.append((r,c+1,'>'))
            if grid[r][c] == '\\':
                q.append((r,c-1,'<'))
            if grid[r][c] == '-':
                q.append((r,c+1,'>'))
                q.append((r,c-1,'<'))
            if grid[r][c] == '|':
                q.append((r-1,c,'^'))

        elif d == 'v':
            if grid[r][c] == '.':
                q.append((r+1,c,'v'))
            elif grid[r][c] == '/':
                q.append((r,c-1,'<'))
            elif grid[r][c] == '\\':
                q.append((r,c+1,'>'))
            elif grid[r][c] == '-':
                q.append((r,c+1,'>'))
                q.append((r,c-1,'<'))
            elif grid[r][c] == '|':
                q.append((r+1,c,'v'))
                
    reduced = set()
    for r,c,d in seen:
        reduced.add((r,c))
    return len(reduced)

grid = open('test.txt').read().split()
#grid = open('input.txt').read().split()

Num_rows = len(grid)
Num_columns = len(grid[0])

nextup = [[{} for i in range(Num_columns)] for j in range(Num_rows)]
  
for r in range(Num_rows):
  for c in range(Num_columns):
      if grid[r][c] == '.':
         nextup[r][c]['>'] = [(r,c+1,'>')]
         nextup[r][c]['<'] = [(r,c-1,'<')]
         nextup[r][c]['^'] = [(r-1,c,'^')]
         nextup[r][c]['v'] = [(r+1,c,'v')]
      if grid[r][c] == '/':
         nextup[r][c]['>'] = [(r-1,c,'^')]
         nextup[r][c]['<'] = [(r+1,c,'v')]
         nextup[r][c]['^'] = [(r,c+1,'>')]
         nextup[r][c]['v'] = [(r,c-1,'<')]
      if grid[r][c] == '\\':
         nextup[r][c]['>'] = [(r+1,c,'v')]
         nextup[r][c]['<'] = [(r-1,c,'^')]
         nextup[r][c]['^'] = [(r,c-1,'<')]
         nextup[r][c]['v'] = [(r,c+1,'>')]
      if grid[r][c] == '|':
         nextup[r][c]['>'] = [(r-1,c,'^'),(r+1,c,'v')]
         nextup[r][c]['<'] = [(r-1,c,'^'),(r+1,c,'v')]
         nextup[r][c]['^'] = [(r-1,c,'^')]
         nextup[r][c]['v'] = [(r+1,c,'v')]
      if grid[r][c] == '-':
         nextup[r][c]['>'] = [(r,c+1,'>')]
         nextup[r][c]['<'] = [(r,c-1,'<')]
         nextup[r][c]['^'] = [(r,c-1,'<'),(r,c+1,'>')]
         nextup[r][c]['v'] = [(r,c-1,'<'),(r,c+1,'>')]


combos = []
for r in range(Num_rows):
  combos.append((r,0,'>'))
  combos.append((r,Num_rows-1,'<'))
for c in range(Num_columns):
  combos.append((0,c,'v'))
  combos.append((Num_columns-1,c,'^'))

print(max([solve(t,Num_rows,Num_columns) for t in combos]))



