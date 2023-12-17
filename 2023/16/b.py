def solve(old_beams,N,M):
  energized = set()
  seen = {}

  while True:
    beams = set()
    f = frozenset(energized)
    if f in seen:
      break
    else:
      seen[f] = 1
    for r,c,d in old_beams:
        if (0 <= r < N) and (0 <= c < M):

            energized.add((r,c,d))

            if d == '>':
                if grid[r][c] == '.':
                    #beams.remove((r,c,d))
                    beams.add((r,c+1,'>'))

                elif grid[r][c] == '/':
                    #beams.remove((r,c,d))
                    beams.add((r-1,c,'^'))
                elif grid[r][c] == '\\':
                    #beams.remove((r,c,d))
                    beams.add((r+1,c,'v'))
                elif grid[r][c] == '-':
                    beams.add((r,c+1,'>'))
                elif grid[r][c] == '|':
                    #beams.remove((r,c,d))
                    beams.add((r-1,c,'^'))
                    beams.add((r+1,c,'v'))

            elif d == '<':
                if grid[r][c] == '.':
                    #beams.remove((r,c,d))
                    beams.add((r,c-1,'<'))

                elif grid[r][c] == '/':
                    #beams.remove((r,c,d))
                    beams.add((r+1,c,'v'))
                elif grid[r][c] == '\\':
                    #beams.remove((r,c,d))
                    beams.add((r-1,c,'^'))
                elif grid[r][c] == '-':
                    beams.add((r,c-1,'<'))
                elif grid[r][c] == '|':
                    #beams.remove((r,c,d))
                    beams.add((r-1,c,'^'))
                    beams.add((r+1,c,'v'))

            elif d == '^':
                if grid[r][c] == '.':
                    #beams.remove((r,c,d))
                    beams.add((r-1,c,'^'))

                if grid[r][c] == '/':
                    #beams.remove((r,c,d))
                    beams.add((r,c+1,'>'))
                if grid[r][c] == '\\':
                    #beams.remove((r,c,d))
                    beams.add((r,c-1,'<'))
                if grid[r][c] == '-':
                    #beams.remove((r,c,d))
                    beams.add((r,c+1,'>'))
                    beams.add((r,c-1,'<'))
                if grid[r][c] == '|':
                    beams.add((r-1,c,'^'))

            elif d == 'v':
                
                if grid[r][c] == '.':
                    #beams.remove((r,c,d))
                    beams.add((r+1,c,'v'))

                elif grid[r][c] == '/':
                    #beams.remove((r,c,d))
                    beams.add((r,c-1,'<'))
                elif grid[r][c] == '\\':
                    #beams.remove((r,c,d))
                    beams.add((r,c+1,'>'))
                elif grid[r][c] == '-':
                    #beams.remove((r,c,d))
                    beams.add((r,c+1,'>'))
                    beams.add((r,c-1,'<'))
                elif grid[r][c] == '|':
                    beams.add((r+1,c,'v'))
            
    old_beams = beams

  reduced = set()
  for r,c,d in energized:
    reduced.add((r,c))
  return len(reduced)

grid = open('test.txt').read().split()
#grid = open('input.txt').read().split()

N = 10
M = 10
combos = set()
for r in range(N):
  combos.add((r,0,'>'))
  combos.add((r,N-1,'<'))
for c in range(M):
  combos.add((0,c,'v'))
  combos.add((M-1,c,'^'))

for r,c,d in combos:
  old_beams = set()
  old_beams.add((r,c,d))
  print(solve(old_beams,N,M), (r,c,d))
