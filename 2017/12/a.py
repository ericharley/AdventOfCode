import networkx as nx

lines = open('input.txt').read().strip().split('\n')

G = nx.Graph()

for line in lines:
  frm,right = line.split(' <-> ')
  tos = right.split(', ')

  G.add_edges_from((frm, to) for to in tos)

# Part 1
print(1+len(nx.descendants(G, '0')))

# Part 2
print(nx.number_connected_components(G))
