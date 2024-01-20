from math import ceil, sqrt
from collections import defaultdict

def spiral(n):
    k = ceil((sqrt(n)-1)/2)
    t = 2*k+1
    m = t**2 
    t = t-1

    if n >= m - t:
      return k-(m-n),-k
    m = m-t

    if n >= m - t:
      return -k,-k+(m-n)
    m = m-t

    if n >= m - t:
      return -k+(m-n),k

    return k,k-(m-n-t)

# Part 1
x,y = spiral(325489)
print( abs(x)+abs(y) )

grid = defaultdict(int)
grid[spiral(1)] = 1

for i in range(2,1000):
  x,y = spiral(i)
  grid[x,y] = grid[x-1,y+1]+grid[x,y+1]+grid[x+1,y+1]+grid[x-1,y]+grid[x+1,y]+grid[x-1,y-1]+grid[x,y-1]+grid[x+1,y-1]
  if grid[x,y]>325489:
    print(grid[x,y])
    break
