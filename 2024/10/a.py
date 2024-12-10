grid = open('input.txt').read().splitlines()
board  = {complex(r,c) : int(ch) for r,row in enumerate(grid) for c,ch in enumerate(row) if ch != '.'}
groups = {v : [k for k in board if board[k] == v] for v in board.values() }

# set of points reachable in 9 steps
def g(trailhead):
  reachable = { trailhead }
  for v in range(1,10):
    reachable = { b for a in reachable for b in groups[v] if abs(b-a)==1 }
  return reachable

# how many ways to get from a to 0
def f(a):
 v = board[a]
 if v == 0:
   return 1

 return sum([f(b) for b in groups[v-1] if abs(b-a) == 1])

# Part 1
print(sum(len(g(trailhead)) for trailhead in groups[0]))

# Part 2
m = {trailend : f(trailend) for trailend in groups[9]}
print(sum(ways for ways in m.values()))
