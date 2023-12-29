import networkx as nx
import random

grid = open('input.txt').read().splitlines()

start = (0, grid[0].index("."))
end = (len(grid) - 1, grid[-1].index("."))

points = [start, end]

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == "#":
            continue
        neighbors = 0
        for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "#":
                neighbors += 1
        if neighbors >= 3:
            points.append((r, c))

graph = {pt: {} for pt in points}

for sr, sc in points:
    stack = [(0, sr, sc)]
    seen = {(sr, sc)}

    while stack:
        n, r, c = stack.pop()
        
        if n != 0 and (r, c) in points:
            graph[(sr, sc)][(r, c)] = n
            continue

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "#" and (nr, nc) not in seen:
                stack.append((n + 1, nr, nc))
                seen.add((nr, nc))

G = nx.Graph()
for v in graph:
  for n in graph[v]:
    G.add_edge(v,n,weight=graph[v][n])

#print(graph)
max_len = 0
for path in nx.all_simple_paths(G, start, end):
#  print(path)
  t = 0
  for i,v in enumerate(path[1:]):
    t += graph[path[i]][path[i+1]]
  if max_len < t:
    max_len = t
    print(len(path), max_len)

