import networkx as nx
from collections import defaultdict

lines = open('input.txt').read().strip().split('\n')
parent = {}
pts_to = defaultdict(list)

vertices = set()
edges = set()
weight = {}

for line in lines:
  f = line.replace('(','').replace(')','').replace(',','').split()
  frm = f[0]
  w = int(f[1])
  to = f[3:]
  vertices.add(frm)
  weight[frm] = w

  for t in to:
    vertices.add(t)
    edges.add((frm,t))
    parent[t] = frm
    pts_to[frm].append(t)

  if frm not in parent:
    parent[frm] = frm

while parent[frm] != frm:
  frm = parent[frm]
root = frm

# Part 1
print(root)

# Part 2
def cost(root):
  return weight[root] + sum([cost(b) for b in pts_to[root]])

for b in pts_to[root]:
  print(b, cost(b))
print()

root = 'onnfacs'  
for b in pts_to[root]:
  print(b, cost(b))
print()

root = 'ftaxy'
for b in pts_to[root]:
  print(b, cost(b))
print()

root = 'gexwzw'
for b in pts_to[root]:
  print(b, cost(b))
print()

