import random
import networkx as nx

lines = open('input.txt').read().strip().split('\n')

G = nx.Graph()

for line in lines:
  left, right = line.split(': ')
  right = right.split(' ')

  for v in right:
    G.add_edge(v, left, capacity=1)


cut_value = 0
while cut_value != 3:

  x = random.choice(list(G.nodes()))
  y = random.choice(list(G.nodes()))

  cut_value, partition = nx.minimum_cut(G, x, y)
  S, T = partition

print(len(S)*len(T) )
