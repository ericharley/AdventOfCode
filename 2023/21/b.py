grid = open('input.txt').read().splitlines()

sr, sc = next((r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "S")

N = len(grid)
M = len(grid[0])

def bfs(steps):
 seen = {}
 ans = {}
 q = []
 
 q.append((sr,sc,steps))
 
 # Breadth first search on the grid
 while q:
   r,c,s = q.pop(0)
 
   # check parity of square
   # if we have an even number of steps left then we could stay here and go back/forth forever
   # so we could reach here at end of our walk
   if s % 2 == 0:
     ans[(r,c)] = 1
 
   # no more steps to take from here so stop processing
   if s == 0:
     continue
 
   # otherwise, take a step N,E,W,S from here
   # 
   #  NB: don't process a step we've already seen
   #     this keeps us from cycling / processing the interior
   #     we want to only process the frontier
   # 
   for nr,nc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
     if 0 <= nr%N < N and 0 <= nc%M < M and grid[nr%N][nc%M] in 'S.' and (nr,nc) not in seen:
       seen[(nr,nc)] = 1
       q.append((nr,nc,s-1))
 
 return len(ans)

# Part 1
print(bfs(64))

# Part 2
#
# number of reachable squares grows quadratically, unsurprising since area
# but there's special properties in the input:
# 1. the center row and column are obstruction free 
# 2. there's a diamond border that's all free squares ...
#
#
# implies a periodicity to the numbers every time we walk grid_width steps
# 
# if we compute the # seen for 65, 65+131 and 65+131+131 steps then we can
# solve for the quadratic using first and second order differences
#
num_steps = 26501365
grid_width = N
rem = num_steps % grid_width

# Get three values
# 
u = [bfs(rem + k*grid_width) for k in range(3)]

Δ0 = u[0]
Δ1 = u[1] - u[0]
Δ2 = ((u[2] - u[1]) - (u[1] - u[0]))

u = lambda n : Δ2//2*n**2 + (Δ1 - Δ2//2)*n + Δ0

n = num_steps // grid_width
print(u(n))

