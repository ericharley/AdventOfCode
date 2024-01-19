import networkx as nx
from itertools import permutations

grid = open('input.txt').read().strip().split('\n')

m = {}
G = nx.Graph()

# Input has a border around it...
for r in range(1,len(grid)-1):
  for c in range(1,len(grid[0])-1):
    if grid[r][c] != '#':
      if grid[r][c] != '.':
        m[grid[r][c]] = (r,c)
      for nr,nc in (r+1,c),(r-1,c),(r,c+1),(r,c-1):
        if grid[nr][nc] != '#':
          G.add_edge((r,c), (nr,nc))

d = {(a,b) : nx.shortest_path_length(G, m[a], m[b]) for a in m for b in m}

def solve(cycle=False):
  min_t = 1000
  for path in permutations('1234567'):
    path = ['0'] + list(path) + (['0'] if cycle else [])
    min_t = min( min_t, sum([d[a,b] for a,b in zip(path,path[1:])]) )
  return(min_t)

# Part 1
print(solve())

# Part 2
print(solve(True))
