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

  n = [(r,c,dir,run_len) for r,c,dir,run_len,old_run_len,is_turn in n if valid((r,c,dir,run_len,old_run_len,is_turn))]
  
  return n
  
def heat_loss(state):
   r, c, dir, run_len = state
   return int(grid[r][c])

def h(state):
   r, c, dir, run_len = state
   return abs(N-1 - r) + abs(M-1 - c)

dist = defaultdict(lambda : math.inf)
seen = {}
prev = {}

dest_states = []
for dir in 'ES':
  for run_len in range(MIN_RUN_LEN, MAX_RUN_LEN+1):
    dest_states += [(N-1,M-1,dir,run_len)]
#dest_states = [(N-1,M-1,'E',4),(N-1,M-1,'E',5),(N-1,M-1,'E',6), \
#               (N-1,M-1,'E',7),(N-1,M-1,'E',8),(N-1,M-1,'E',9), \
#               (N-1,M-1,'E',10), \
#               (N-1,M-1,'S',4),(N-1,M-1,'S',5),(N-1,M-1,'S',6), \
#               (N-1,M-1,'S',7),(N-1,M-1,'S',8),(N-1,M-1,'S',9), \
#               (N-1,M-1,'S',10)]

q = []

start_states = [(0,0,'E',1),(0,0,'S',1)]
for source in start_states:
  dist[source] = 0
  prev[source] = None
  seen[source] = True
  heapq.heappush(q, (dist[source], source))

while q:
    d, current_state = heapq.heappop(q)

    if current_state in dest_states:
      break

    for neighbor in neighbors(current_state):
      if neighbor in seen:
        continue

      dist[neighbor] = dist[current_state] + heat_loss(neighbor)
      priority = dist[neighbor] + h(neighbor)
      prev[neighbor] = current_state
      seen[neighbor] = True
      heapq.heappush(q, (priority, neighbor))

print(min([dist[d] for d in dest_states]))

min_dist = math.inf
for d in dest_states:
  if dist[d] < min_dist:
     min_state = d
     min_dist = dist[d]

#print(min_dist, min_state)

curr_state = min_state
path = []
while curr_state in prev:
   path += [curr_state]
   curr_state = prev[curr_state]
path.reverse()
path.pop(0)
#print(path)

def print_grid_with_path(states):
  l = []
  m = {}
  for r,c,dir,run_len in states:
    l.append((r,c))
    m[(r,c)] = {'N':'^','S':'v','E':'>','W':'<'}[dir]

  for r, row in enumerate(grid):
    for c, col in enumerate(row):
  
      if (r,c) in l:
        print(m[(r,c)],end='')
      
      else:
        print(grid[r][c],end='')
    print()

print_grid_with_path(path)
print(len(seen))
