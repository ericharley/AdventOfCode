import networkx as nx

grid = open("input.txt").read().strip().splitlines()
rows, cols = len(grid), len(grid[0])

grid = { (r, c) for r in range(rows) for c in range(cols) if grid[r][c] != "." }
dirs = [ (i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i or j ]

G = nx.Graph()
G.add_nodes_from(grid)

for r, c in grid:
  for dr, dc in dirs:
    if (r+dr, c+dc) in grid:
      G.add_edge((r, c), (r+dr, c+dc))

# Part 1
print( sum([G.degree(v) < 4 for v in G]) )

# Part 2
print( len(G)-len(nx.k_core(G, k=4)) )
