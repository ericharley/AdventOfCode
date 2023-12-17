#grid = open('test.txt').read().split()
grid = open('input.txt').read().split()

#for r,row in enumerate(grid):
#  if r == 0:
#    print(' ', ''.join(map(str,range(10))))
#  print(r,row)

#for r, row in enumerate(grid):
#  for c, col in enumerate(row):
#    print(r,c,grid[r][c])

old_beams = {(0,0,'>')}

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
        if (0 <= r < 110) and (0 <= c < 110):

#            if (r,c,d) in energized:
#               break

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

#print(old_beams)
#print(len(energized))
#for r,c,d in beams:

reduced = set()
for r,c,d in energized:
  reduced.add((r,c))
print(len(reduced))

#> : right,
#< : left,
#^ : up,
#v : down
