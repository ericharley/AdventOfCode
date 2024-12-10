grid = [line for line in open('input3.txt').read().splitlines()]

def solve(l):
 p = 1
 for dc,dr in l:
   c,w = 0,0
   for r in range(0,len(grid),dr):
     w += 1 if grid[r][c] == '#' else 0
     c = (c + dc) % len(grid[0])
   p *= w
 return p

print( solve([(3,1)]) )
print( solve([(1,1),(3,1),(5,1),(7,1),(1,2)]) )

