from functools import reduce
from operator import xor

data = open('input.txt').read().strip()

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

# Part 1
ns = list(range(256))
lens = list(map(int,data.split(',')))
pos, skip = 0,0

ns,pos,skip = do_round(ns,lens,pos,skip)

print(ns[0]*ns[1])

# Part 2
ns = list(range(256))
lens = [ord(c) for c in data] + [17,31,73,47,23]
pos,skip = 0,0

for _round in range(64):
  ns,pos,skip = do_round(ns,lens,pos,skip)

print(bytes(reduce(xor,ns[i:i+16]) for i in range(0,256,16)).hex())
