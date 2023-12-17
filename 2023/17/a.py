from collections import defaultdict
import math
import heapq

#grid = open('test.txt').read().split()
grid = open('input.txt').read().split()

def print_grid():
 for r, row in enumerate(grid):
  for c, col in enumerate(row):
    print(grid[r][c],end='')
  print()

N = len(grid)
M = len(grid[0])

DIRS = ['W','E','N','S']
MAX_RUN_LEN = 3

# Places you can go
def neighbors(state):
  r,c,dir,run_len = state
  n = []

  # go Straight
  if dir == 'W':
    n += [(r,c-1,'W',run_len+1)] # West
  elif dir == 'E':
    n += [(r,c+1,'E',run_len+1)] # East
  elif dir == 'N':
    n += [(r-1,c,'N',run_len+1)] # North
  elif dir == 'S':
    n += [(r+1,c,'S',run_len+1)] # South

  # turn Left
  if dir == 'W':
    n += [(r+1,c,'S',1)]  # South
  elif dir == 'E':
    n += [(r-1,c,'N',1)]  # North
  elif dir == 'N':
    n += [(r,c-1,'W',1)] # West
  elif dir == 'S':
    n += [(r,c+1,'E',1)] # East

  # Turn Right
  if dir == 'W':
    n += [(r-1,c,'N', 1)]  # North
  elif dir == 'E':
    n += [(r+1,c,'S', 1)]  # South
  elif dir == 'N':
    n += [(r,c+1,'E', 1)] # East
  elif dir == 'S':
    n += [(r,c-1,'W', 1)] # West

  def valid(state):
    r,c,dir,run_len = state
    if not((0 <= r < N) and (0 <= c < M)) or run_len > MAX_RUN_LEN:
      return False
    return True

  n = [x for x in n if valid(x)]
  
  return n
  
def print_grid_with_state(state):
  rr,cc,dir,run_len = state

  for r, row in enumerate(grid):
    for c, col in enumerate(row):

      if r == rr and c == cc:
        print({'N':'^','S':'v','E':'>','W':'<'}[dir],end='')

      else:
        print(grid[r][c],end='')
    print()

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

def heat_loss(state):
   r, c, dir, run_len = state
   return int(grid[r][c])


# r, c, dir, run_len
start_state = (0,0,'E',1)

dist = defaultdict(lambda : math.inf)
seen = {}
prev = {}
source = start_state
dests = [(N-1,M-1,'E',1),(N-1,M-1,'E',2),(N-1,M-1,'E',3), \
         (N-1,M-1,'S',1),(N-1,M-1,'S',2),(N-1,M-1,'S',3)]


dist[source] = 0

q = []
heapq.heappush(q, (dist[source], source))

while q:
    d, current_state = heapq.heappop(q)

    if current_state in dests:
      break

    for neighbor in neighbors(current_state):
      if neighbor in seen:
        continue

      dist[neighbor] = dist[current_state] + heat_loss(neighbor)
      prev[neighbor] = current_state
      seen[neighbor] = True
      heapq.heappush(q, (dist[neighbor], neighbor))
        
print(min([dist[d] for d in dests]))

