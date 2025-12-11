import bisect
from math import prod
import networkx as nx

lines = open('input.txt').read().strip().split()
data = [tuple(map(int,line.split(','))) for line in lines]

G = nx.Graph()
G.add_nodes_from(data)

def dist(a,b):
  return sum([(i-j)**2 for i,j in zip(a,b)])

sorted_keys = sorted( [(a,b) for a in G for b in G if a < b],
                      key=lambda k: dist(*k))

# Part 1
for a,b in sorted_keys[:1000]:
  G.add_edge(a,b)

sizes = sorted([len(c) for c in nx.connected_components(G)], reverse=True)
print(prod(sizes[:3]))

# Part 2
for a,b in sorted_keys[1000:]:
  G.add_edge(a,b)
  if nx.is_connected(G):
    break

print(a[0]*b[0])
