from collections import defaultdict
import math
import heapq

#grid = open('test.txt').read().split()
#grid = open('test2.txt').read().split()
grid = open('input.txt').read().split()

N = len(grid)
M = len(grid[0])

DIRS = ['W','E','N','S']
MIN_RUN_LEN = 4
MAX_RUN_LEN = 10

# Places you can go
def neighbors(state):
  r,c,dir,run_len = state
  n = []

  def valid(state):
    r,c,_,run_len,old_run_len,is_turn = state
    if not((0 <= r < N) and (0 <= c < M)):
      return False
    if run_len > MAX_RUN_LEN:
      return False
    if is_turn and (old_run_len < MIN_RUN_LEN):
      return False
    return True

  # go Straight
  if dir == 'W':
    n += [(r,c-1,'W',run_len+1,run_len,False)] # West
  elif dir == 'E':
    n += [(r,c+1,'E',run_len+1,run_len,False)] # East
    n += [(r-1,c,'N',1,run_len,True)]  # North
  elif dir == 'N':
    n += [(r-1,c,'N',run_len+1,run_len,False)] # North
  elif dir == 'S':
    n += [(r+1,c,'S',run_len+1,run_len,False)] # South

  # turn Left
  if dir == 'W':
    n += [(r+1,c,'S',1,run_len,True)]  # South
  elif dir == 'E':
    n += [(r-1,c,'N',1,run_len,True)]  # North
  elif dir == 'N':
    n += [(r,c-1,'W',1,run_len,True)] # West
  elif dir == 'S':
    n += [(r,c+1,'E',1,run_len,True)] # East

  # Turn Right
  if dir == 'W':
    n += [(r-1,c,'N', 1,run_len,True)]  # North
  elif dir == 'E':
    n += [(r+1,c,'S', 1,run_len,True)]  # South
  elif dir == 'N':
    n += [(r,c+1,'E', 1,run_len,True)] # East
  elif dir == 'S':
    n += [(r,c-1,'W', 1,run_len,True)] # West

  def reduce(x):
     r,c,dir,run_len,old_run_len,is_turn = x
     return (r,c,dir,run_len)

  n = [reduce(x) for x in n if valid(x)]
  
  return n
  
def heat_loss(state):
   r, c, dir, run_len = state
   return int(grid[r][c])

dist = defaultdict(lambda : math.inf)
seen = {}
prev = {}

dest_states = []
for dir in 'ES':
  for run_len in range(MIN_RUN_LEN, MAX_RUN_LEN+1):
    dest_states += [(N-1,M-1,dir,run_len)]

q = []

start_states = [(0,0,'E',1),(0,0,'S',1)]
for source in start_states:
  dist[source] = 0
  prev[source] = None
  heapq.heappush(q, (dist[source], source))

while q:
    d, current_state = heapq.heappop(q)

    if current_state in dest_states:
      break

    for neighbor in neighbors(current_state):
      if neighbor in seen:
        continue

      dist[neighbor] = dist[current_state] + heat_loss(neighbor)
      prev[neighbor] = current_state
      seen[neighbor] = True
      heapq.heappush(q, (dist[neighbor], neighbor))
        
print(min([dist[d] for d in dest_states]))
