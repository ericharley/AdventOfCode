from collections import defaultdict
from functools import reduce

lines = open('input.txt').read().strip().splitlines()

components = []
boosts = set()
n = defaultdict(set)

for line in lines:
  a,b = map(int,line.split('/'))
  if a != b:
    components.append((a,b))
  if a == b:
    boosts.add(a)
  
for part_a in components:
  for part_b in components:
    if part_a != part_b:
      if part_a[0] in part_b:
        n[part_a,part_a[0]].add(part_b)
      if part_a[1] in part_b:
        n[part_a,part_a[1]].add(part_b)

def strength(path):
  return sum([sum(part) for part,_ in path])

def f(path, g):
  last_part,last_port = path[-1]
  moves = n[last_part,last_port] - set([part for part,_ in path])
    
  if not moves:
    boost = sum([2*port for _,port in path if port in boosts])
    return len(path), (strength(path) + boost)

  return reduce(g, [f(path + [(nxt,nxt[last_port==nxt[0]])], g) for nxt in moves])

def max_s(old, new):
  if new[1] > old[1]:
    return new
  return old

starts = [part for part in components if part[0] == 0]
starting_paths = [[(start,start[1])] for start in starts]
for g in [max_s, max]:
  l,s = reduce(g, [f(start, g) for start in starting_paths])
  print(l,s)
