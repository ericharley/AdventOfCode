import networkx as nx
lines = open('input.txt').read().strip().split('\n')

G = nx.Graph()

for line in lines:
  left, right = line.split(': ')
  right = right.split(' ')

  for v in right:
    G.add_edge(v, left, capacity=1.0)

output = nx.betweenness_centrality(G)

sortedDict = list(sorted(output, key=output.get))
print(sortedDict[-6:])
