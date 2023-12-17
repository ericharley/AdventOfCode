grid = open('input.txt').read().split()

N = len(grid)
M = len(grid[0])

nextup = [[{} for i in range(M)] for j in range(N)]
  
for r in range(N):
  for c in range(M):
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

def solve(t,N,M):
    r,c,d = t

    stack = [(r,c,d)]
    seen = {}
    energized = {}

    while stack:
        r, c, d = stack.pop()
        if not((0 <= r < N) and (0 <= c < M)) or (r,c,d) in seen:
            continue

        seen[(r,c,d)] = 1
        energized[(r,c)] = 1
        
        stack += nextup[r][c][d]

    return len(energized)

# Part 1
print(solve((0,0,'>'),N,M))

# Part 2
combos = [(r,0,'>') for r in range(N)]   + \
         [(r,N-1,'<') for r in range(N)] + \
         [(0,c,'v') for c in range(M)]   + \
         [(M-1,c,'^') for c in range(M)]

print(max([solve(t,N,M) for t in combos]))
