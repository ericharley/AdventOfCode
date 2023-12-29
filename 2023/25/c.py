import random
import networkx as nx
lines = open('input.txt').read().strip().split('\n')

G = nx.MultiGraph()

def cut(G):
    while G.number_of_nodes() > 2 :
        u,v = random.choice(list(G.edges()))
        G = nx.contracted_edge(G, (u, v), self_loops=False)
    if G.number_of_edges() == 3:
      print(G.edges())
    return G.number_of_edges()

for line in lines:
  left, right = line.split(': ')
  right = right.split(' ')

  for v in right:
    G.add_edge(v, left, capacity=1.0)

random.seed()
m = 1000
while True:
  c = cut(G)
  if c < m:
    m = c
    print(c)

#import random
#
#while True:
#
#  x = random.choice(list(G.nodes()))
#  y = random.choice(list(G.nodes()))
#
#  cut_value, partition = nx.minimum_cut(G, x, y)
#  reachable, non_reachable = partition
#
#  if len(reachable) != 1 and len(non_reachable) != 1:
#    # print(len(reachable), len(non_reachable), len(reachable)*len(non_reachable) )
#    print(len(reachable)*len(non_reachable) )
#    break
