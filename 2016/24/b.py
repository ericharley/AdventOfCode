import networkx as nx

G = nx.Graph()
m = {}
grid = open('test.txt').read().strip().split('\n')
for r in range(len(grid)):
 for c in range(len(grid[0])):
   if grid[r][c] != '#':
     G.add_node((r,c))
     for nr,nc in (r+1,c),(r-1,c),(r,c+1),(r,c-1):
       if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
         if grid[nr][nc] != '#':
           G.add_edge((r,c), (nr,nc))
   if grid[r][c] not in '#.':
     m[grid[r][c]] = (r,c)

from itertools import permutations
for p in permutations('1234'):
 p = list(p)
 prev_step = '0'
 t = 0
 for step in p:
   t += nx.shortest_path_length(G, source=m[prev_step], target=m[step])
   prev_step = step
 print(t)
