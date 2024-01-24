from functools import reduce
from operator import xor

def do_round(ns,lens,pos,skip):
  N = len(ns)
  for l in lens:
    idx = range(pos,(pos+l))
    ls = [ ns[i % N] for i in idx ]
    ls.reverse()
    for k,i in enumerate(idx):
      ns[i % N] = ls[k]
    pos += (l + skip ) % N
    skip += 1
  return ns,pos,skip

def calc_hash(data):
  ns = list(range(256))
  lens = [ord(c) for c in data] + [17,31,73,47,23]
  pos,skip = 0,0

  for _round in range(64):
    ns,pos,skip = do_round(ns,lens,pos,skip)

  return bytes(reduce(xor,ns[i:i+16]) for i in range(0,256,16)).hex()

def to_bin(hash,k):
  return bin(int(hash,base=16))[2:].zfill(k)

key = 'wenycdww'

## Part 1
#c = sum([to_bin(calc_hash(key + '-' + str(i)),128).count('1') for i in range(128)])
#print(c)

# Part 2
vertices = set()

for r in range(128):
  data = key + '-' + str(r)
  row = to_bin(calc_hash(data),128)
  for c,v in enumerate(row):
    if v == '1':
      vertices.add((r,c))

print(len(vertices))

import networkx as nx
G = nx.Graph()

for r,c in vertices:
  G.add_node((r,c))
  for (nr,nc) in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
    if (nr,nc) in vertices:
      G.add_edge((r,c),(nr,nc))

print(nx.number_connected_components(G))
