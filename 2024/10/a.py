from collections import defaultdict

grid = open('input.txt').read().splitlines()
board  = {(r,c) : int(ch) for r,row in enumerate(grid) for c,ch in enumerate(row) if ch != '.'}
groups = {v : [k for k in board if board[k] == v] for v in board.values() }

def neighbors(a,b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1

s,t = 0,0

for trailhead_id in groups[0]:

  reachable = {(trailhead_id,1)}

  for i in range(9):
    next_reachable = defaultdict(int)
    for trailhead,w in reachable:
      for b in groups[i+1]:
        if neighbors(trailhead,b):
          next_reachable[b] += w

    reachable = { (b,w) for b,w in next_reachable.items() }

  t += len(reachable)
  for _,b in reachable:
    s += b

print(t)
print(s)
