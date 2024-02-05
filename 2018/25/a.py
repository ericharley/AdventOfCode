import networkx as nx

points = []
for line in open('input.txt').read().strip().splitlines():
  points.append(tuple(map(int, line.split(','))))

def md(s,t):
  return sum(abs(x-y) for x,y in zip(s,t))

G = nx.Graph()

# NB: networkx doesn't consider an isolated vertex a connected component
for a in points:
  for b in points:
    if md(a,b) <= 3:
      G.add_edge(a,b)

print(nx.number_connected_components(G))
