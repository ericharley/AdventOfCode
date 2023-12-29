import networkx as nx
lines = open('input.txt').read().strip().split('\n')

G = nx.Graph()

for line in lines:
  left, right = line.split(': ')
  right = right.split(' ')

  for v in right:
    G.add_edge(v, left, capacity=1.0)

groups = list(nx.k_edge_components(G, 4))
a = len(groups[0])
b = len(groups[1])
 
print(a*b)
